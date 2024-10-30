# Copyright(C) 2010-2013  Christophe Benz, Julien Hebert
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


from collections import OrderedDict
from pathlib import Path
import os
import sys
import subprocess
import warnings

try:
    import tty
    import termios
except ImportError:
    PROMPT = '--Press return to continue--'

    def readch():
        return sys.stdin.readline()
else:
    PROMPT = '--Press a key to continue--'

    def readch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        tty.setcbreak(fd)
        try:
            c = sys.stdin.read(1)
            # XXX do not read magic number
            if c == '\x03':
                raise KeyboardInterrupt()
            return c
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

from woob.capabilities.base import BaseObject
from woob.tools.application.pretty import colored, NC, BOLD
from woob.tools.misc import guess_encoding, classproperty


__all__ = ['IFormatter', 'MandatoryFieldsNotFound']


class MandatoryFieldsNotFound(Exception):
    def __init__(self, missing_fields):
        super().__init__('Mandatory fields not found: %s.' % ', '.join(missing_fields))


class IFormatter:
    # Tuple of fields mandatory to not crash
    MANDATORY_FIELDS = None
    # Tuple of displayed field. Set to None if all available fields are
    # displayed
    DISPLAYED_FIELDS = None

    @classproperty
    def BOLD(self):
        warnings.warn(
            'Use woob.tools.application.pretty.BOLD instead.\n'
            'That\'s also better to use woob.tools.application.pretty.colored.',
            DeprecationWarning,
            stacklevel=2
        )
        return BOLD

    @classproperty
    def NC(self):
        warnings.warn(
            'Use woob.tools.application.pretty.NC instead.\n'
            'That\'s also better to use woob.tools.application.pretty.colored.',
            DeprecationWarning,
            stacklevel=2
        )
        return NC

    def colored(self, string, color, attrs=None, on_color=None):
        if (
            self.outfile != sys.stdout
            or not self.outfile.isatty()
            or os.getenv("NO_COLOR") is not None
        ):
            return string

        if isinstance(attrs, str):
            attrs = [attrs]
        return colored(string, color, on_color=on_color, attrs=attrs)

    def __init__(self, display_keys=True, display_header=True, outfile=None):
        self.display_keys = display_keys
        self.display_header = display_header
        self.interactive = False
        self.print_lines = 0
        self.termrows = 0
        self.termcols = None
        if outfile is None:
            outfile = sys.stdout
        self.outfile = outfile
        # XXX if stdin is not a tty, it seems that the command fails.

        if sys.stdout.isatty() and sys.stdin.isatty():
            if sys.platform == 'win32':
                from ctypes import windll, create_string_buffer

                h = windll.kernel32.GetStdHandle(-12)
                csbi = create_string_buffer(22)
                res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

                if res:
                    import struct
                    (bufx, bufy, curx, cury, wattr,
                     left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                    self.termrows = right - left + 1
                    self.termcols = bottom - top + 1
                else:
                    self.termrows = 80  # can't determine actual size - return default values
                    self.termcols = 80
            else:
                stty_output = subprocess.check_output(["stty", "size"]).split()
                self.termrows = int(stty_output[0])
                self.termcols = int(stty_output[1])

    def output(self, formatted):
        if isinstance(self.outfile, (str, Path)):
            encoding = guess_encoding(sys.stdout)
            with open(self.outfile, "a+", encoding=encoding, errors='replace') as outfile:
                outfile.write(formatted + os.linesep)

        else:
            for line in formatted.split('\n'):
                if self.termrows and (self.print_lines + 1) >= self.termrows:
                    self.outfile.write(PROMPT)
                    self.outfile.flush()
                    readch()
                    self.outfile.write('\b \b' * len(PROMPT))
                    self.print_lines = 0

                plen = len(line.replace(BOLD, '').replace(NC, ''))

                print(line, file=self.outfile)

                if self.termcols:
                    self.print_lines += int(plen/self.termcols) + 1
                else:
                    self.print_lines += 1

    def start_format(self, **kwargs):
        pass

    def flush(self):
        pass

    def format(self, obj, selected_fields=None, alias=None):
        """
        Format an object to be human-readable.
        An object has fields which can be selected.

        :param obj: object to format
        :type obj: BaseObject or dict
        :param selected_fields: fields to display. If None, all fields are selected
        :type selected_fields: tuple
        :param alias: an alias to use instead of the object's ID
        :type alias: str
        """
        if isinstance(obj, BaseObject):
            if selected_fields:  # can be an empty list (nothing to do), or None (return all fields)
                obj = obj.copy()
                for name, value in list(obj.iter_fields()):
                    if name not in selected_fields:
                        delattr(obj, name)

            if self.MANDATORY_FIELDS:
                missing_fields = set(self.MANDATORY_FIELDS) - set([name for name, value in obj.iter_fields()])
                if missing_fields:
                    raise MandatoryFieldsNotFound(missing_fields)

            formatted = self.format_obj(obj, alias)
        else:
            try:
                obj = OrderedDict(obj)
            except ValueError:
                raise TypeError('Please give a BaseObject or a dict')

            if selected_fields:
                obj = obj.copy()
                for name, value in list(obj.items()):
                    if name not in selected_fields:
                        obj.pop(name)

            if self.MANDATORY_FIELDS:
                missing_fields = set(self.MANDATORY_FIELDS) - set(obj)
                if missing_fields:
                    raise MandatoryFieldsNotFound(missing_fields)

            formatted = self.format_dict(obj)

        if formatted:
            self.output(formatted)
        return formatted

    def format_obj(self, obj, alias=None):
        """
        Format an object to be human-readable.
        Called by format().
        This method has to be overridden in child classes.

        :param obj: object to format
        :type obj: BaseObject
        :rtype: str
        """
        return self.format_dict(obj.to_dict())

    def format_dict(self, obj):
        """
        Format a dict to be human-readable.

        :param obj: dict to format
        :type obj: dict
        :rtype: str
        """
        raise NotImplementedError()

    def format_collection(self, collection, only):
        """
        Format a collection to be human-readable.

        :param collection: collection to format
        :type collection: BaseCollection
        :rtype: str
        """
        if only is False or collection.basename in only:
            if collection.basename and collection.title:
                self.output('%s~ (%s) %s (%s)%s' %
                     (self.BOLD, collection.basename, collection.title, collection.backend, self.NC))
            else:
                self.output('%s~ (%s) (%s)%s' %
                     (self.BOLD, collection.basename, collection.backend, self.NC))


class PrettyFormatter(IFormatter):
    def format_obj(self, obj, alias):
        title = self.get_title(obj)
        desc = self.get_description(obj)

        if alias is not None:
            result = '%s %s %s (%s)' % (self.colored('%2s' % alias, 'red', 'bold'),
                                         self.colored('—', 'cyan', 'bold'),
                                         self.colored(title, 'yellow', 'bold'),
                                         self.colored(obj.backend, 'blue', 'bold'))
        else:
            result = '%s %s %s' % (self.colored(obj.fullid, 'red', 'bold'),
                                    self.colored('—', 'cyan', 'bold'),
                                    self.colored(title, 'yellow', 'bold'))

        if desc is not None:
            result += '%s\t%s' % (os.linesep, self.colored(desc, 'white'))

        return result

    def get_title(self, obj):
        raise NotImplementedError()

    def get_description(self, obj):
        return None
