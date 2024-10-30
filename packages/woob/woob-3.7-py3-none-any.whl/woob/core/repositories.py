# Copyright(C) 2010-2023 Romain Bignon
#
# This file is part of woob.
#
# woob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# woob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with woob. If not, see <http://www.gnu.org/licenses/>.


import importlib
import posixpath
import shutil
import re
import sys
import os
import subprocess
import hashlib
from compileall import compile_dir
from contextlib import closing, contextmanager
from datetime import datetime
from io import BytesIO, StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile, mkdtemp
from urllib.request import getproxies
from configparser import RawConfigParser, DEFAULTSECT
import tarfile

import packaging.version
from packaging.specifiers import SpecifierSet

from woob.browser.browsers import Browser
from woob.browser.profiles import Woob as WoobProfile
from woob.exceptions import BrowserHTTPError, BrowserHTTPNotFound, ModuleInstallError
from woob.tools.log import getLogger
from woob.tools.misc import get_backtrace, to_unicode, find_exe
from woob.tools.packaging import parse_requirements

from .modules import LoadedModule, _add_in_modules_path


@contextmanager
def open_for_config(filename):
    f = NamedTemporaryFile(
        mode='w', encoding='utf-8', dir=os.path.dirname(filename), delete=False
    )
    with f:
        yield f
    os.replace(f.name, filename)


class ModuleInfo:
    """
    Information about a module available on a repository.
    """

    def __init__(self, name):
        self.name = name

        # path to the local directory containing this module.
        self.path = None
        self.url = None
        self.repo_url = None
        self.signed = False

        self.version = 0
        self.capabilities = ()
        self.dependencies = ()
        self.description = ''
        self.maintainer = ''
        self.license = ''
        self.icon = ''
        self.woob_spec = None

    def load(self, items):
        self.version = int(items['version'])
        self.capabilities = items['capabilities'].split()
        self.dependencies = items.get('dependencies', '').split()
        self.description = to_unicode(items['description'])
        self.maintainer = to_unicode(items['maintainer'])
        self.license = to_unicode(items['license'])
        self.icon = items['icon'].strip() or None
        self.woob_spec = SpecifierSet(items.get('woob_spec', ''))

    def has_caps(self, *caps):
        """Return True if module implements at least one of the caps."""
        if len(caps) == 1 and isinstance(caps[0], (list, tuple)):
            caps = caps[0]
        for c in caps:
            if type(c) == type:
                c = c.__name__
            if c in self.capabilities:
                return True
        return False

    def is_installed(self):
        return self.path is not None

    def is_local(self):
        return self.url is None

    def dump(self):
        return (('version', self.version),
                ('capabilities', ' '.join(self.capabilities)),
                ('dependencies', ' '.join(self.dependencies)),
                ('description', self.description),
                ('maintainer', self.maintainer),
                ('license', self.license),
                ('icon', self.icon or ''),
                ('woob_spec', str(self.woob_spec)),
               )


class RepositoryUnavailable(Exception):
    """
    Repository in not available.
    """


class Repository:
    """
    Represents a repository.
    """
    INDEX = 'modules.list'
    KEYDIR = '.keys'
    KEYRING = 'trusted.gpg'

    def __init__(self, url):
        self.url = url
        self.name = ''
        self.update = 0
        self.maintainer = ''
        self.local = None
        self.signed = False
        self.key_update = 0
        self.obsolete = False
        self.logger = getLogger(f'{__name__}.repository')
        self.errors = {}

        self.modules = {}

        if self.url.startswith('file://'):
            self.local = True
        elif re.match('https?://.*', self.url):
            self.local = False
        else:
            # This is probably a file in ~/.woob/repositories/, we
            # don't know if this is a local or a remote repository.
            with open(self.url, 'r', encoding='utf-8') as fp:
                self.parse_index(fp)

    def __repr__(self):
        return f'<Repository {self.name}>'

    def localurl2path(self):
        """
        Get a local path of a file:// URL.
        """
        assert self.local is True

        if self.url.startswith('file://'):
            return self.url[len('file://'):]
        return self.url

    def retrieve_index(self, browser, repo_path):
        """
        Retrieve the index file of this repository. It can use network
        if this is a remote repository.

        :param repo_path: path to save the downloaded index file (if any).
        :type repo_path: str or None
        """
        built = False
        if self.local:
            # Repository is local, open the file.
            filename = os.path.join(self.localurl2path(), self.INDEX)
            try:
                fp = open(filename, 'r', encoding='utf-8')
            except IOError:
                # This local repository doesn't contain a built modules.list index.
                self.name = Repositories.url2filename(self.url)
                self.build_index(self.localurl2path(), filename)
                built = True
                fp = open(filename, 'r', encoding='utf-8')
        else:
            # This is a remote repository, download file
            try:
                fp = StringIO(browser.open(posixpath.join(self.url, self.INDEX)).text)
            except BrowserHTTPError as e:
                raise RepositoryUnavailable(str(e)) from e

        self.parse_index(fp)
        fp.close()

        # this value can be changed by parse_index
        if self.local and not built:
            # Always rebuild index of a local repository.
            self.build_index(self.localurl2path(), filename)

        # Save the repository index in ~/.woob/repositories/
        if repo_path:
            self.save(repo_path, private=True)

    def retrieve_keyring(self, browser, keyring_path, progress):
        # ignore local
        if self.local:
            return

        keyring = Keyring(keyring_path)
        # prevent previously signed repos from going unsigned
        if not self.signed and keyring.exists():
            raise RepositoryUnavailable('Previously signed repository can not go unsigned')
        if not self.signed:
            return

        if not keyring.exists() or self.key_update > keyring.version:
            # This is a remote repository, download file
            try:
                keyring_data = browser.open(posixpath.join(self.url, self.KEYRING)).content
                sig_data = browser.open(posixpath.join(self.url, self.KEYRING + '.sig')).content
            except BrowserHTTPError as e:
                raise RepositoryUnavailable(str(e)) from e
            if keyring.exists():
                if not keyring.is_valid(keyring_data, sig_data):
                    raise InvalidSignature('the keyring itself')
                progress.progress(0.0, 'The keyring was updated (and validated by the previous one).')
            elif not progress.prompt(
                f'The repository {self.url} isn\'t trusted yet.\n'
                f'Fingerprint of keyring is {hashlib.sha1(keyring_data).hexdigest()}\n'
                'Are you sure you want to continue?'
            ):
                raise RepositoryUnavailable('Repository not trusted')
            keyring.save(keyring_data, self.key_update)
            progress.progress(0.0, str(keyring))

    def parse_index(self, fp):
        """
        Parse index of a repository

        :param fp: file descriptor to read
        :type fp: buffer
        """
        config = RawConfigParser()
        config.read_file(fp)

        # Read default parameters
        items = dict(config.items(DEFAULTSECT))
        try:
            self.name = items['name']
            self.update = int(items['update'])
            self.maintainer = items['maintainer']
            self.signed = bool(int(items.get('signed', '0')))
            self.key_update = int(items.get('key_update', '0'))
            self.obsolete = bool(int(items.get('obsolete', '0')))
        except KeyError as e:
            raise RepositoryUnavailable(f'Missing global parameters in repository: {e}') from e
        except ValueError as e:
            raise RepositoryUnavailable(f'Incorrect value in repository parameters: {e}') from e

        if len(self.name) == 0:
            raise RepositoryUnavailable('Name is empty')

        if 'url' in items:
            self.url = items['url']
            self.local = self.url.startswith('file://')
        elif self.local is None:
            raise RepositoryUnavailable('Missing "url" key in settings')

        # Load modules
        self.modules.clear()
        for section in config.sections():
            module = ModuleInfo(section)
            module.load(dict(config.items(section)))
            if not self.local:
                module.url = posixpath.join(self.url, f'{module.name}.tar.gz')
                module.repo_url = self.url
                module.signed = self.signed
            self.modules[section] = module

    def build_index(self, path, filename):
        """
        Rebuild index of modules of repository.

        :param path: path of the repository
        :type path: str
        :param filename: file to save index
        :type filename: str
        """
        self.logger.debug('Rebuild index')
        self.modules.clear()
        self.errors.clear()

        _add_in_modules_path(path)

        if os.path.isdir(os.path.join(path, self.KEYDIR)):
            self.signed = True
            self.key_update = self.get_tree_mtime(os.path.join(path, self.KEYDIR), True)
        else:
            self.signed = False
            self.key_update = 0

        for name in sorted(os.listdir(path)):
            module_path = os.path.join(path, name)

            # Check for special cases.
            if (
                name.startswith('.')  # ".", "..", and private files and dirs
                or name.startswith('_') or name.endswith('_')
                or name == self.KEYDIR
            ):
                continue

            # Check if the module is indeed a module.
            if os.path.isdir(module_path):
                if not os.path.exists(os.path.join(module_path, '__init__.py')):
                    continue
            else:
                basename = os.path.basename(module_path).casefold()
                if not basename.endswith('.py') or len(basename) < 3:
                    continue

                name = name[:-3]

            try:
                pymodule = importlib.import_module(f'woob_modules.{name}')
                module = LoadedModule(pymodule)
            except Exception as e:  # noqa
                self.logger.warning('Unable to build module %s: [%s] %s', name, type(e).__name__, e)
                bt = get_backtrace(e)
                self.logger.debug(bt)
                self.errors[name] = bt
            else:
                m = ModuleInfo(module.name)
                m.version = self.get_tree_mtime(module_path)
                m.capabilities = list({c.__name__ for c in module.iter_caps()})
                m.dependencies = module.dependencies
                m.description = module.description
                m.maintainer = module.maintainer
                m.license = module.license
                m.icon = module.icon or ''

                module_path = Path(module.path)
                if not os.path.isdir(module_path):
                    module_path = module_path.parent

                requirements = parse_requirements(module_path / 'requirements.txt')
                m.woob_spec = requirements.get('woob', '')

                self.modules[module.name] = m

        self.update = int(datetime.now().strftime('%Y%m%d%H%M'))
        self.save(filename)

    @staticmethod
    def get_tree_mtime(path, include_root=False):
        mtime = 0
        if include_root or not os.path.isdir(path):
            mtime = int(datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y%m%d%H%M'))
        for root, _, files in os.walk(path):
            for f in files:
                if f.endswith('.pyc'):
                    continue
                m = int(datetime.fromtimestamp(os.path.getmtime(os.path.join(root, f))).strftime('%Y%m%d%H%M'))
                mtime = max(mtime, m)

        return mtime

    def save(self, filename, private=False):
        """
        Save repository into a file (modules.list for example).

        :param filename: path to file to save repository.
        :type filename: str
        :param private: if enabled, save URL of repository.
        :type private: bool
        """
        config = RawConfigParser()
        config.set(DEFAULTSECT, 'name', self.name)
        config.set(DEFAULTSECT, 'update', self.update)
        config.set(DEFAULTSECT, 'maintainer', self.maintainer)
        config.set(DEFAULTSECT, 'signed', int(self.signed))
        config.set(DEFAULTSECT, 'key_update', self.key_update)
        if private:
            config.set(DEFAULTSECT, 'url', self.url)

        for module in self.modules.values():
            config.add_section(module.name)
            for key, value in module.dump():
                config.set(module.name, key, value)

        with open_for_config(filename) as f:
            config.write(f)


class Versions:
    VERSIONS_LIST = 'versions.list'

    def __init__(self, path):
        self.path = path
        self.versions = {}

        config_filename = os.path.join(self.path, self.VERSIONS_LIST)
        try:
            with open(config_filename, 'r', encoding='utf-8') as fp:
                config = RawConfigParser()
                config.read_file(fp, config_filename)

                # Read default parameters
                for key, value in config.items(DEFAULTSECT):
                    self.versions[key] = int(value)
        except IOError:
            pass

    def get(self, name):
        return self.versions.get(name, None)

    def set(self, name, version):
        self.versions[name] = int(version)
        self.save()

    def save(self):
        config = RawConfigParser()
        for name, version in self.versions.items():
            config.set(DEFAULTSECT, name, version)

        with open_for_config(os.path.join(self.path, self.VERSIONS_LIST)) as fp:
            config.write(fp)


class IProgress:
    def progress(self, percent, message):
        raise NotImplementedError()

    def error(self, message):
        raise NotImplementedError()

    def prompt(self, message):
        raise NotImplementedError()

    def __repr__(self):
        return f'<{self.__class__.__name__}>'


class PrintProgress(IProgress):
    def progress(self, percent, message):
        print('=== [%3.0f%%] %s' % (percent*100, message), file=sys.stderr)

    def error(self, message):
        print(f'ERROR: {message}', file=sys.stderr)

    def prompt(self, message):
        print(f'{message} (Y/n): *** ASSUMING YES ***', file=sys.stderr)
        return True


class SubProgress(IProgress):
    def __init__(self, target, steps):
        self.target = target
        self.steps = steps
        self.current = 0

    def progress(self, percent, message):
        return self.target.progress((self.current + percent) / self.steps, message)

    def __getattr__(self, attr):
        return getattr(self.target, attr)


def recursive_deps(direct_deps, key, result=None):
    """
    take a dict of direct dependencies and get all dependencies of an element

    >>> recursive_deps({1: {2, 3}, 2: {3}, 3: {4}, 4: set()}, 1)
    {2, 3, 4}
    """

    if result is None:
        result = set()

    for sub in direct_deps[key]:
        if sub not in result:
            result.add(sub)
            recursive_deps(direct_deps, sub, result)
    return result


class DepList(list):
    def move_value_after(self, val, afters):
        # push an element after all its dependencies

        for pos in range(len(self) - 1, -1, -1):
            if self[pos] == val:
                # already after
                return
            if self[pos] in afters:
                break
        else:
            raise AssertionError()

        current = self.index(val)

        self.insert(pos + 1, val)
        del self[current]


def dependency_sort(deps_rules):
    """
    >>> dependency_sort({1: {2}, 2: {4}, 3: set(), 4: {3}})
    [3, 4, 2, 1]
    """
    # naive but maybe good enough?

    result = DepList(deps_rules)
    deps_rules = dict(deps_rules)

    for key in deps_rules:
        deps = recursive_deps(deps_rules, key)
        result.move_value_after(key, deps)

    return result


DEFAULT_SOURCES_LIST = \
"""# List of woob repositories
#
# The entries below override the entries above (with
# backends of the same name).

https://updates.woob.tech/%(version)s/main/

# DEVELOPMENT
# If you want to hack on woob modules, you may add a
# reference to sources, for example:
#file:///home/rom1/src/woob/woob_modules/
"""


class Repositories:
    SOURCES_LIST = 'sources.list'
    MODULES_DIR = 'modules'
    MODULES_SUBDIR = 'woob_modules'
    REPOS_DIR = 'repositories'
    KEYRINGS_DIR = 'keyrings'
    ICONS_DIR = 'icons'

    SHARE_DIRS = [MODULES_DIR, REPOS_DIR, KEYRINGS_DIR, ICONS_DIR]

    def __init__(self, workdir, datadir, version):
        self.logger = getLogger(f"{__name__}.repositories")
        self.version = version

        self.browser = None

        self.workdir = workdir
        self.datadir = datadir
        self.sources_list = os.path.join(self.workdir, self.SOURCES_LIST)
        self.modules_dir = os.path.join(self.datadir, self.MODULES_DIR, self.version, self.MODULES_SUBDIR)
        self.repos_dir = os.path.join(self.datadir, self.REPOS_DIR)
        self.keyrings_dir = os.path.join(self.datadir, self.KEYRINGS_DIR)
        self.icons_dir = os.path.join(self.datadir, self.ICONS_DIR)

        self.create_dir(self.datadir)
        self.create_dir(self.modules_dir)
        self.create_namespace_package(self.modules_dir)
        self.create_dir(self.repos_dir)
        self.create_dir(self.keyrings_dir)
        self.create_dir(self.icons_dir)

        self.versions = Versions(self.modules_dir)

        self.repositories = []

        if not os.path.exists(self.sources_list):
            with open_for_config(self.sources_list) as f:
                f.write(DEFAULT_SOURCES_LIST)
            self.update()
        else:
            self.load()

    def load_browser(self):
        class WoobBrowser(Browser):
            PROFILE = WoobProfile(self.version)
        if self.browser is None:
            self.browser = WoobBrowser(
                logger=getLogger('browser', parent=self.logger),
                proxy=getproxies())

    def create_dir(self, name):
        if not os.path.exists(name):
            os.makedirs(name)
        elif not os.path.isdir(name):
            self.logger.error('"%s" is not a directory', name)

    namespace_package_content = "from pkgutil import extend_path\n__path__ = extend_path(__path__, __name__)\n"

    def create_namespace_package(self, path):
        pypath = os.path.join(path, '__init__.py')
        if os.path.exists(pypath):
            with open(pypath, 'r', encoding='utf-8') as fd:
                create_file = (fd.read() != self.namespace_package_content)
        else:
            create_file = True

        if create_file:
            with open(pypath, 'wt', encoding='utf-8') as fd:
                fd.write(self.namespace_package_content)

    def _extend_module_info(self, repo, info):
        if repo.local:
            info.path = repo.localurl2path()
        elif self.versions.get(info.name) is not None:
            info.path = self.modules_dir

        return info

    def get_all_modules_info(self, caps=None):
        """
        Get all ModuleInfo instances available.

        :param caps: filter on capabilities:
        :type caps: list[str]
        :rtype: dict[:class:`ModuleInfo`]
        """
        modules = {}
        for repos in reversed(self.repositories):
            for name, info in repos.modules.items():
                if name not in modules and (not caps or info.has_caps(caps)):
                    modules[name] = self._extend_module_info(repos, info)
        return modules

    def get_module_info(self, name):
        """
        Get ModuleInfo object of a module.

        It tries all repositories from last to first, and set
        the 'path' attribute of ModuleInfo if it is installed.
        """
        for repos in reversed(self.repositories):
            if name in repos.modules:
                m = repos.modules[name]
                self._extend_module_info(repos, m)
                return m
        return None

    def load(self):
        """
        Load repositories from ~/.local/share/woob/repositories/.
        """
        self.repositories = []
        for name in sorted(os.listdir(self.repos_dir)):
            path = os.path.join(self.repos_dir, name)
            try:
                repository = Repository(path)
                self.repositories.append(repository)
            except RepositoryUnavailable as e:
                print(f'Unable to load repository {name} ({e}), try to update repositories.', file=sys.stderr)

    def get_module_icon_path(self, module):
        return os.path.join(self.icons_dir, f'{module.name}.png')

    def retrieve_icon(self, module):
        """
        Retrieve the icon of a module and save it in ~/.local/share/woob/icons/.
        """
        self.load_browser()
        if not isinstance(module, ModuleInfo):
            module = self.get_module_info(module)

        dest_path = self.get_module_icon_path(module)

        icon_url = module.icon
        if not icon_url:
            if module.is_local():
                icon_path = os.path.join(module.path, module.name, 'favicon.png')
                if module.path and os.path.exists(icon_path):
                    shutil.copy(icon_path, dest_path)
                return

            icon_url = module.url.replace('.tar.gz', '.png')

        try:
            icon = self.browser.open(icon_url)
        except BrowserHTTPNotFound:
            pass  # no icon, no problem
        else:
            with open(dest_path, 'wb') as fp:
                fp.write(icon.content)

    def _parse_source_list(self):
        l = []
        with open(self.sources_list, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip() % {'version': packaging.version.Version(self.version).major}
                m = re.match('(file|https?)://.*', line)
                if m:
                    l.append(line)
        return l

    def update_repositories(self, progress=PrintProgress()):
        """
        Update list of repositories by downloading them
        and put them in ~/.local/share/woob/repositories/.

        :param progress: observer object.
        :type progress: :class:`IProgress`
        """
        self.load_browser()

        self.repositories = []
        for name in os.listdir(self.repos_dir):
            os.remove(os.path.join(self.repos_dir, name))

        gpg_found = Keyring.find_gpg() or Keyring.find_gpgv()
        for line in self._parse_source_list():
            progress.progress(0.0, f'Getting {line}')
            repository = Repository(line)
            filename = self.url2filename(repository.url)
            prio_filename = '%02d-%s' % (len(self.repositories), filename)
            repo_path = os.path.join(self.repos_dir, prio_filename)
            keyring_path = os.path.join(self.keyrings_dir, filename)
            try:
                repository.retrieve_index(self.browser, repo_path)
                if gpg_found:
                    repository.retrieve_keyring(self.browser, keyring_path, progress)
                else:
                    progress.error('Cannot find gpg or gpgv to check for repository authenticity.\n'
                                   'You should install GPG for better security.')
            except RepositoryUnavailable as e:
                progress.error(f'Unable to load repository: {e}')
            else:
                self.repositories.append(repository)
                if repository.obsolete:
                    last_update = datetime.strptime(str(repository.update), '%Y%m%d%H%M').strftime('%Y-%m-%d')
                    progress.error(
                        f'This repository does not receive updates anymore (since {last_update}).\n'
                        'Your woob version is probably obsolete and should be upgraded.'
                    )

    def check_repositories(self):
        """
        Check if sources.list is consistent with repositories
        """
        l = []
        for line in self._parse_source_list():
            repository = Repository(line)
            filename = self.url2filename(repository.url)
            prio_filename = '%02d-%s' % (len(l), filename)
            repo_path = os.path.join(self.repos_dir, prio_filename)
            if not os.path.isfile(repo_path):
                return False
            l.append(repository)
        return True

    def _is_module_updatable(self, info):
        return not info.is_local() and info.is_installed() and self.versions.get(info.name) != info.version

    def _is_module_installable(self, info):
        return not info.is_local() and not info.is_installed()

    def _get_all_dependencies(self, modules):
        modules = list(modules)
        direct_deps = {}

        i = 0
        while i < len(modules):
            current = modules[i]

            for dep_name in current.dependencies:
                if dep_name in direct_deps:
                    # already handled
                    continue

                dep = self.get_module_info(dep_name)
                if not dep:
                    raise ModuleInstallError(f'Module "{dep_name}" does not exist')
                modules.append(dep)

            direct_deps[current.name] = set(current.dependencies)

            i += 1

        # install most depended-on first
        sorted_names = dependency_sort(direct_deps)
        return [self.get_module_info(name) for name in sorted_names]

    def update(self, progress=PrintProgress()):
        """
        Update repositories and install new packages versions.

        :param progress: observer object.
        :type progress: :class:`IProgress`
        """
        self.update_repositories(progress)

        to_update = []
        for info in self.get_all_modules_info().values():
            if self._is_module_updatable(info):
                to_update.append(info)

        to_update = self._get_all_dependencies(to_update)
        to_update = [info for info in to_update if self._is_module_updatable(info) or self._is_module_installable(info)]

        if len(to_update) == 0:
            progress.progress(1.0, 'All modules are up-to-date.')
            return

        proxy_progress = SubProgress(progress, len(to_update))

        for n, info in enumerate(to_update):
            proxy_progress.current = n
            try:
                self._install_one_module(info, proxy_progress)
            except ModuleInstallError as e:
                proxy_progress.progress(1.0, str(e))

    def install(self, module, progress=PrintProgress()):
        if isinstance(module, ModuleInfo):
            info = module
        elif isinstance(module, str):
            progress.progress(0.0, f'Looking for module {module}')
            info = self.get_module_info(module)
            if not info:
                raise ModuleInstallError(f'Module "{module}" does not exist')
        else:
            raise ValueError(f'"module" parameter might be a ModuleInfo object or a string, not {module}')

        to_install = self._get_all_dependencies([info])
        to_install = [
            subinfo
            for subinfo in to_install
            if self._is_module_updatable(subinfo)
            or self._is_module_installable(subinfo)
        ]

        proxy_progress = SubProgress(progress, len(to_install))

        for n, info in enumerate(to_install):
            proxy_progress.current = n
            self._install_one_module(info, proxy_progress)

    def _install_one_module(self, module, progress):
        """
        Install a module.

        :param module: module to install
        :type module: :class:`str` or :class:`ModuleInfo`
        :param progress: observer object
        :type progress: :class:`IProgress`
        """
        if self.version not in module.woob_spec:
            raise ModuleInstallError(
                f"Module requires woob {module.woob_spec}, but you use woob {self.version}'.\n"
                "Hint: use 'woob update' or install a newer version of woob"
            )

        self.load_browser()

        if module.is_local():
            raise ModuleInstallError('%s is available on local.' % module.name)

        module_dir = os.path.join(self.modules_dir, module.name)
        installed = self.versions.get(module.name)
        if installed is None or not os.path.exists(module_dir):
            progress.progress(0.2, 'Module %s is not installed yet' % module.name)
        elif module.version > installed:
            progress.progress(0.2, 'A new version of %s is available' % module.name)
        else:
            raise ModuleInstallError('The latest version of %s is already installed' % module.name)

        progress.progress(0.3, 'Downloading module...')
        try:
            tardata = self.browser.open(module.url).content
        except BrowserHTTPError as e:
            raise ModuleInstallError('Unable to fetch module: %s' % e)

        # Check signature
        if module.signed and (Keyring.find_gpg() or Keyring.find_gpgv()):
            progress.progress(0.5, 'Checking module authenticity...')
            sig_data = self.browser.open(posixpath.join(module.url + '.sig')).content
            keyring_path = os.path.join(self.keyrings_dir, self.url2filename(module.repo_url))
            keyring = Keyring(keyring_path)
            if not keyring.exists():
                raise ModuleInstallError('No keyring found, please update repos.')
            if not keyring.is_valid(tardata, sig_data):
                raise ModuleInstallError('Invalid signature for %s.' % module.name)

        # Extract module from tarball.
        if os.path.isdir(module_dir):
            shutil.rmtree(module_dir)
        progress.progress(0.7, 'Setting up module...')

        # TODO: remove tar.extractall() when not needed to prevent from potential archive attacks
        with closing(tarfile.open('', 'r:gz', BytesIO(tardata))) as tar:
            tar.extractall(self.modules_dir)  # nosec

        if not os.path.isdir(module_dir):
            raise ModuleInstallError(f'The archive for {module.name} looks invalid.')
        # Precompile
        compile_dir(module_dir, quiet=True)

        self.versions.set(module.name, module.version)

        progress.progress(0.9, 'Downloading icon...')
        self.retrieve_icon(module)

        progress.progress(1.0, f'Module {module.name} has been installed!')

    @staticmethod
    def url2filename(url):
        """
        Get a safe file name for an URL.

        All non-alphanumeric characters are replaced by _.
        """
        return ''.join([l if l.isalnum() else '_' for l in url])

    def __iter__(self):
        for repository in self.repositories:
            yield repository

    @property
    def errors(self):
        errors = {}
        for repository in self:
            errors.update(repository.errors)
        return errors


class InvalidSignature(Exception):
    def __init__(self, filename):
        self.filename = filename
        super(InvalidSignature, self).__init__(f'Invalid signature for {filename}')


class Keyring:
    EXTENSION = '.gpg'

    def __init__(self, path):
        self.path = path + self.EXTENSION
        self.vpath = path + '.version'
        self.version = 0

        if self.exists():
            with open(self.vpath, 'r', encoding='utf-8') as f:
                self.version = int(f.read().strip())
        else:
            if os.path.exists(self.path):
                os.remove(self.path)
            if os.path.exists(self.vpath):
                os.remove(self.vpath)

    def exists(self):
        if not os.path.exists(self.vpath):
            return False
        if os.path.exists(self.path):
            # Check the file is not empty.
            # This is because there was a bug creating empty keyring files.
            with open(self.path, 'rb') as fp:
                if len(fp.read().strip()):
                    return True
        return False

    def save(self, keyring_data, version):
        with open(self.path, 'wb') as fp:
            fp.write(keyring_data)
        self.version = version
        with open_for_config(self.vpath) as fp:
            fp.write(str(version))

    @staticmethod
    def find_gpgv():
        return find_exe('gpgv2') or find_exe('gpgv')

    @staticmethod
    def find_gpg():
        return find_exe('gpg2') or find_exe('gpg')

    def is_valid(self, data, sigdata):
        """
        Check if the data is signed by an accepted key.
        data and sigdata should be strings.
        """
        gpg = self.find_gpg()
        gpgv = self.find_gpgv()

        if gpg:
            gpg_homedir = mkdtemp(prefix='woob_gpg_')
            verify_command = [
                gpg, '--verify', '--no-options',
                '--no-default-keyring', '--quiet',
                '--homedir', gpg_homedir
            ]
        elif gpgv:
            verify_command = [gpgv]

        with NamedTemporaryFile(suffix='.sig', delete=False) as sigfile:
            temp_filename = sigfile.name
            return_code = None
            out = ''
            err = ''
            try:
                sigfile.write(sigdata)
                sigfile.flush()  # very important
                sigfile.close()
                assert isinstance(data, bytes)
                # Yes, all of it is necessary
                with subprocess.Popen(verify_command + [
                        '--status-fd', '1',
                        '--keyring', os.path.realpath(self.path),
                        os.path.realpath(sigfile.name),
                        '-'
                    ],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE) as proc:

                    out, err = proc.communicate(data)
                    return_code = proc.returncode
            finally:
                os.unlink(temp_filename)
                if gpg:
                    shutil.rmtree(gpg_homedir)

            if return_code or b'GOODSIG' not in out or b'VALIDSIG' not in out:
                print(out, err, file=sys.stderr)
                return False
        return True

    def __str__(self):
        if self.exists():
            with open(self.path, 'rb') as f:
                h = hashlib.sha1(f.read()).hexdigest()
            return f'Keyring version {self.version}, checksum {h}'
        return 'NO KEYRING'
