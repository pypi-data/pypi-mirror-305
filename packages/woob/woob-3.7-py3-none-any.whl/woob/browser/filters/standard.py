# Copyright(C) 2014 Romain Bignon
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

from __future__ import annotations

import datetime
import re
import pycountry
from typing import Any
from collections.abc import Iterator
from decimal import Decimal, InvalidOperation
from itertools import islice
from numbers import Number
from urllib.parse import parse_qs, urlparse

from dateutil.parser import parse as parse_date
from dateutil.tz import gettz
from lxml.etree import ElementBase as LXMLElement

from woob.browser.url import URL
from woob.capabilities.base import Currency as BaseCurrency
from woob.capabilities.base import empty
from woob.tools.misc import clean_text

from .base import _NO_DEFAULT, Filter, FilterError, ItemNotFound, _Filter, debug

__all__ = [
    'Filter', 'FilterError', 'RegexpError', 'FormatError',
    'AsyncLoad', 'Async', 'Base', 'Decode', 'Env', 'RawText',
    'CleanText', 'Lower', 'Upper', 'Title', 'Currency', 'NumberFormatError',
    'CleanDecimal', 'Slugify', 'Type', 'Field', 'Regexp', 'Map', 'MapIn',
    'DateTime', 'FromTimestamp', 'Date', 'DateGuesser', 'Time', 'Duration',
    'MultiFilter', 'CombineDate', 'Format', 'BrowserURL', 'Join', 'MultiJoin',
    'Eval', 'QueryValue', 'Coalesce', 'CountryCode',
]


class RegexpError(FilterError):
    pass


class FormatError(FilterError):
    pass


class AsyncLoad(Filter):
    """Load a page asynchronously for later use.

    Often used in combination with :class:`Async` filter.
    """

    def __call__(self, item):
        link = self.select(self.selector, item)
        return item.page.browser.async_open(link) if link else None


class Async(Filter):
    """Selector that uses another page fetched earlier.

    Often used in combination with :class:`AsyncLoad` filter.
    Requires that the other page's URL is matched with a Page by the Browser.

    Example::

        class item(ItemElement):
            load_details = Field('url') & AsyncLoad

            obj_description = Async('details') & CleanText('//h3')
    """

    def __init__(self, name, selector=None):
        super(Async, self).__init__()
        self.selector = selector
        self.name = name

    def __and__(self, o):
        if isinstance(o, type) and issubclass(o, _Filter):
            o = o()
        self.selector = o
        return self

    def __call__(self, item):
        if item.loaders[self.name] is None:
            return None

        return self.select(self.selector, self.loaded_page(item).doc)

    def filter(self, *args):
        raise AttributeError()

    def loaded_page(self, item):
        result = item.loaders[self.name].result()
        assert result.page is not None, 'The loaded url %s hasn\'t been matched by an URL object' % result.url
        return result.page


class Base(Filter):
    """
    Change the base element used in filters.

    >>> Base(Env('header'), CleanText('./h1'))  # doctest: +SKIP
    """

    def __call__(self, item):
        base = self.select(self.base, item)
        if isinstance(base, list):
            assert len(base) == 1, 'If using a list, there must be one element only'
            base = base[0]
        return self.select(self.selector, base)

    def __init__(self, base, selector=None, default=_NO_DEFAULT):
        super(Base, self).__init__(selector, default)
        self.base = base


class Decode(Filter):
    """
    Filter that aims to decode urlencoded strings

    >>> Decode(Env('_id'))  # doctest: +ELLIPSIS
    <woob.browser.filters.standard.Decode object at 0x...>
    >>> from .html import Link
    >>> Decode(Link('./a'))  # doctest: +ELLIPSIS
    <woob.browser.filters.standard.Decode object at 0x...>
    """

    def __call__(self, item):
        self.encoding = item.page.ENCODING if item.page.ENCODING else 'utf-8'
        return self.filter(self.select(self.selector, item))

    @debug()
    def filter(self, txt):
        try:
            try:
                from urllib.parse import unquote
                txt = unquote(txt, self.encoding)
            except ImportError:
                from urllib import unquote
                txt = unquote(txt.encode('ascii')).decode(self.encoding)
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass

        return txt


class Env(_Filter):
    """
    Filter to get environment value of the item.

    It is used for example to get page parameters, or when there is a parse()
    method on ItemElement.
    """

    def __init__(self, name, default=_NO_DEFAULT):
        super(Env, self).__init__(default)
        self.name = name

    def __call__(self, item):
        try:
            return item.env[self.name]
        except KeyError:
            return self.default_or_raise(ItemNotFound('Environment variable %s not found' % self.name))


class RawText(Filter):
    """Get raw text from an element.

    Unlike :class:`CleanText`, whitespace is kept as is.
    """

    def __init__(self, selector=None, children=False, default=_NO_DEFAULT):
        """
        :param children: whether to get text from children elements of the select elements
        :type children: bool
        """

        super(RawText, self).__init__(selector, default=default)
        self.children = children

    @debug()
    def filter(self, el):
        if isinstance(el, (tuple, list)):
            return ' '.join([self.filter(e) for e in el])

        if self.children:
            text = el.text_content()
        else:
            text = el.text

        if text is None:
            result = self.default
        else:
            result = str(text)

        return result


class CleanText(Filter):
    """
    Get a cleaned text from an element.

    It first replaces all tabs and multiple spaces
    (including newlines if ``newlines`` is True)
    to one space and strips the result string.

    The result is coerced into str, and optionally normalized
    according to the ``normalize`` argument.

    Then it replaces all symbols given in the ``symbols`` argument.

    >>> CleanText().filter('coucou ') == u'coucou'
    True
    >>> CleanText().filter(u'coucou\xa0coucou') == u'coucou coucou'
    True
    >>> CleanText(newlines=True).filter(u'coucou\\r\\n coucou ') == u'coucou coucou'
    True
    >>> CleanText(newlines=False).filter(u'coucou\\r\\n coucou ') == u'coucou\\ncoucou'
    True
    """

    def __init__(self, selector=None, symbols='', replace=[], children=True, newlines=True, transliterate=False, normalize='NFC', **kwargs):
        """
        :param symbols: list of strings to remove from text
        :type symbols: list
        :param replace: optional pairs of text replacements to perform
        :type replace: list[tuple[str, str]]
        :param children: whether to get text from children elements of the select elements
        :type children: bool
        :param newlines: if True, newlines will be converted to space too
        :type newlines: bool
        :param normalize: Unicode normalization to perform
        :type normalize: str or None
        :param transliterate: Transliterates unicode characters into ASCII characters
        :type transliterate: bool
        """

        super(CleanText, self).__init__(selector, **kwargs)
        self.symbols = symbols
        self.toreplace = replace
        self.children = children
        self.newlines = newlines
        self.normalize = normalize
        self.transliterate = transliterate

    @debug()
    def filter(self, txt):
        if txt is None:
            return self.default_or_raise(FilterError('The text cannot be None'))
        elif isinstance(txt, int):
            txt = str(txt)
        elif isinstance(txt, (tuple, list)):
            txt = ' '.join(
                self.clean(item, newlines=self.newlines, children=self.children)
                for item in txt
            )

        txt = self.clean(txt, self.children, self.newlines, self.normalize, self.transliterate)
        txt = self.remove(txt, self.symbols)
        txt = self.replace(txt, self.toreplace)
        return txt

    @classmethod
    def clean(cls, txt, children=True, newlines=True, normalize='NFC', transliterate=False):
        """
        Cleans the text. The children argument is ignored with Selenium.
        """
        if isinstance(txt, LXMLElement):
            if children:
                txt = list(txt.itertext())
            else:
                txt = list(txt.xpath('./text()'))
            txt = ' '.join(txt)  # 'foo   bar '
        elif not isinstance(txt, str):
            txt = ' '.join(txt.itertext())

        return clean_text(
            txt,
            remove_newlines=newlines,
            normalize=normalize,
            transliterate=transliterate,
        )

    @classmethod
    def remove(cls, txt, symbols):
        for symbol in symbols:
            txt = txt.replace(symbol, '')
        return txt.strip()

    @classmethod
    def replace(cls, txt, replace):
        for before, after in replace:
            txt = txt.replace(before, after)
        return txt


class Lower(CleanText):
    """Extract text with :class:`CleanText` and convert to lower-case."""

    @debug()
    def filter(self, txt):
        txt = super(Lower, self).filter(txt)
        return txt.lower()


class Upper(CleanText):
    """Extract text with :class:`CleanText` and convert to upper-case."""

    @debug()
    def filter(self, txt):
        txt = super(Upper, self).filter(txt)
        return txt.upper()


class Title(CleanText):
    """Extract text with :class:`CleanText` and apply title() to it."""

    @debug()
    def filter(self, txt):
        txt = super(Title, self).filter(txt)
        return txt.title()


class Currency(CleanText):
    @debug()
    def filter(self, txt):
        txt = super(Currency, self).filter(txt)
        if empty(txt):
            return self.default_or_raise(FormatError("Unable to parse %r" % txt))
        return BaseCurrency.get_currency(txt)


class CountryCode(CleanText):
    """
    Filter to get the country ISO 3166-1 alpha-2 code from the country name
    """
    @debug()
    def filter(self, txt: str) -> Any:
        """Get the country code from the name of the country

        :param txt: Country name
        :type txt: str
        :raises FormatError: if the Country name is not found

        >>> CountryCode().filter('france')
        'fr'
        >>> CountryCode(default= 'll').filter('Greez')
        'll'
        """
        txt = super().filter(txt)
        if empty(txt):
            return self.default_or_raise(FormatError("Unable to parse %r" % txt))
        try:
            alpha_2_code = pycountry.countries.lookup(txt).alpha_2.lower()
        except LookupError:
            # Country not found
            return self.default_or_raise(FormatError('Country not recognized: %r' % txt))

        return alpha_2_code


class NumberFormatError(FormatError, InvalidOperation):
    pass


class CleanDecimal(CleanText):
    """
    Get a cleaned Decimal value from an element.

    `replace_dots` is False by default. A dot is interpreted as a decimal separator.

    If `replace_dots` is set to True, we remove all the dots. The ',' is used as decimal
    separator (often useful for French values)

    If `replace_dots` is a tuple, the first element will be used as the thousands separator,
    and the second as the decimal separator.

    See https://en.wikipedia.org/wiki/Thousands_separator#Examples_of_use

    For example, for the UK style (as in 1,234,567.89):

    >>> CleanDecimal('./td[1]', replace_dots=(',', '.'))  # doctest: +SKIP
    """

    def __init__(self, selector=None, replace_dots=False, sign=None, legacy=True, default=_NO_DEFAULT):
        """
        :param sign: function accepting the text as param and returning the sign
        """

        super(CleanDecimal, self).__init__(selector, default=default)
        self.replace_dots = replace_dots
        self.sign = sign
        self.legacy = legacy
        if not legacy:
            thousands_sep, decimal_sep = self.replace_dots
            self.matching = re.compile(r'([+-]?)\s*(\d[\d%s%s]*|%s\d+)' % tuple(map(re.escape, (thousands_sep, decimal_sep, decimal_sep))))
            self.thousand_check = re.compile(r'^[+-]?\d{1,3}(%s\d{3})*(%s\d*)?$' % tuple(map(re.escape, (thousands_sep, decimal_sep))))
            self.is_scientific_notation = re.compile(r'([+-]?)(\d+(?:[.,]\d*)?[eE][+-]?\d+)')

    @debug()
    def filter(self, text):
        if type(text) in (float, int):
            text = str(text)

        if empty(text):
            return self.default_or_raise(FormatError('Unable to parse %r' % text))

        original_text = text = super(CleanDecimal, self).filter(text)

        text = text.replace('\u2212', '-')

        if self.legacy:
            if self.replace_dots:
                if type(self.replace_dots) is tuple:
                    thousands_sep, decimal_sep = self.replace_dots
                else:
                    thousands_sep, decimal_sep = '.', ','
                text = text.replace(thousands_sep, '').replace(decimal_sep, '.')

            text = re.sub(r'[^\d\-\.]', '', text)
        else:
            thousands_sep, decimal_sep = self.replace_dots

            matches = self.matching.findall(text)
            if not matches:
                return self.default_or_raise(NumberFormatError('There is no number to parse'))
            elif len(matches) > 1:
                matches = self.is_scientific_notation.findall(text)
                if not matches:
                    return self.default_or_raise(NumberFormatError('There should be exactly one number to parse'))

            text = '%s%s' % (matches[0][0], matches[0][1].strip())

            if thousands_sep and thousands_sep in text and not self.thousand_check.match(text):
                return self.default_or_raise(NumberFormatError('Thousands separator is misplaced in %r' % text))

            text = text.replace(thousands_sep, '').replace(decimal_sep, '.')

        try:
            v = Decimal(text)
        except InvalidOperation as e:
            return self.default_or_raise(NumberFormatError(e))
        else:
            if self.sign is not None:
                if callable(self.sign):
                    v *= self.sign(original_text)
                elif self.sign == '+':
                    return abs(v)
                elif self.sign == '-':
                    return -abs(v)
                else:
                    raise TypeError("'sign' should be a callable or a sign string")
            return v

    @classmethod
    def US(cls, *args, **kwargs):
        kwargs['legacy'] = False
        kwargs['replace_dots'] = (',', '.')
        return cls(*args, **kwargs)

    @classmethod
    def French(cls, *args, **kwargs):
        kwargs['legacy'] = False
        kwargs['replace_dots'] = (' ', ',')
        return cls(*args, **kwargs)

    @classmethod
    def SI(cls, *args, **kwargs):
        kwargs['legacy'] = False
        kwargs['replace_dots'] = (' ', '.')
        return cls(*args, **kwargs)

    @classmethod
    def Italian(cls, *args, **kwargs):
        kwargs['legacy'] = False
        kwargs['replace_dots'] = ('.', ',')
        return cls(*args, **kwargs)


class Slugify(Filter):
    @debug()
    def filter(self, label):
        label = re.sub(r'[^A-Za-z0-9]', ' ', label.lower()).strip()
        label = re.sub(r'\s+', '-', label)
        return label


class Type(Filter):
    """
    Get a cleaned value of any type from an element text.
    The type_func can be any callable (class, function, etc.).
    By default an empty string will not be parsed but it can be changed
    by specifying minlen=False. Otherwise, a minimal length can be specified.

    >>> Type(CleanText('./td[1]'), type=int)  # doctest: +SKIP

    >>> Type(type=int).filter(42)
    42
    >>> Type(type=int).filter('42')
    42
    >>> Type(type=int, default='NaN').filter('')
    'NaN'
    >>> Type(type=list, minlen=False, default=list('ab')).filter('')
    []
    >>> Type(type=list, minlen=0, default=list('ab')).filter('')
    ['a', 'b']
    """

    def __init__(self, selector=None, type=None, minlen=0, default=_NO_DEFAULT):
        super(Type, self).__init__(selector, default=default)
        self.type_func = type
        self.minlen = minlen

    @debug()
    def filter(self, txt):
        if isinstance(txt, self.type_func):
            return txt
        if empty(txt):
            return self.default_or_raise(FormatError('Unable to parse %r' % txt))
        if self.minlen is not False and len(txt) <= self.minlen:
            return self.default_or_raise(FormatError('Unable to parse %r' % txt))
        try:
            return self.type_func(txt)
        except ValueError as e:
            return self.default_or_raise(FormatError('Unable to parse %r: %s' % (txt, e)))


class Field(_Filter):
    """
    Get the attribute of object.

    Example::

        obj_foo = CleanText('//h1')
        obj_bar = Field('foo')

    will make "bar" field equal to "foo" field.
    """

    def __init__(self, name):
        super(Field, self).__init__()
        self.name = name

    def __call__(self, item):
        return item.use_selector(getattr(item, 'obj_%s' % self.name), key=self._key)


# Based on nth from https://docs.python.org/2/library/itertools.html
def nth(iterable, n, default=None):
    "Returns the nth item or a default value, n can be negative, or '*' for all"
    if n == '*':
        return iterable
    if n < 0:
        iterable = reversed(list(iterable))
        n = abs(n) - 1
    return next(islice(iterable, n, None), default)


def ordinal(n):
    "To have some readable debug information: '*' => all, 0 => 1st, 1 => 2nd..."
    if n == '*':
        return 'all'
    i = abs(n)
    n = n - 1 if n < 0 else n + 1
    return str(n) + ('th' if i > 2 else ['st', 'nd', 'rd'][i])


class Regexp(Filter):
    r"""
    Apply a regex.

    >>> from lxml.html import etree
    >>> doc = etree.fromstring('<html><body><p>Date: <span>13/08/1988</span></p></body></html>')
    >>> Regexp(CleanText('//p'), r'Date: (\d+)/(\d+)/(\d+)', '\\3-\\2-\\1')(doc) == u'1988-08-13'
    True

    >>> (Regexp(CleanText('//body'), r'(\d+)', nth=1))(doc) == u'08'
    True
    >>> (Regexp(CleanText('//body'), r'(\d+)', nth=-1))(doc) == u'1988'
    True
    >>> (Regexp(CleanText('//body'), r'(\d+)', template='[\\1]', nth='*'))(doc) == [u'[13]', u'[08]', u'[1988]']
    True
    >>> (Regexp(CleanText('//body'), r'Date:.*'))(doc) == u'Date: 13/08/1988'
    True
    >>> (Regexp(CleanText('//body'), r'^(?!Date:).*', default=None))(doc)
    >>>
    """

    def __init__(self, selector=None, pattern=None, template=None, nth=0, flags=0, default=_NO_DEFAULT):
        super(Regexp, self).__init__(selector, default=default)
        if pattern is None:
            raise FilterError('Missing pattern parameter')
        self.pattern = pattern

        self._regex = re.compile(pattern, flags)
        self.template = template
        self.nth = nth

    def expand(self, m):
        if self.template is None:
            try:
                return next(g for g in m.groups() if g is not None)
            except StopIteration:
                return m.string
        return self.template(m) if callable(self.template) else m.expand(self.template)

    @debug()
    def filter(self, txt):
        """
        :raises: :class:`RegexpError` if `pattern` was not found
        """

        if isinstance(txt, (tuple, list)):
            txt = ' '.join([t.strip() for t in txt.itertext()])

        m = None
        try:
            m = self._regex.search(txt) if self.nth == 0 else \
                nth(self._regex.finditer(txt), self.nth)
        except TypeError:
            msg = '%r is not a string or bytes-like object' % txt
            return self.default_or_raise(RegexpError(msg))

        if not m:
            if len(txt) > 1024:
                txt = txt[:1021] + "..."
            msg = 'Unable to find %s %s in %r' % (ordinal(self.nth), self.pattern, txt)
            return self.default_or_raise(RegexpError(msg))

        if isinstance(m, Iterator):
            return list(map(self.expand, m))

        return self.expand(m)


class Map(Filter):
    """Map selected value to another value using a dict.

    Example::

        TYPES = {
            'Concert': CATEGORIES.CONCERT,
            'Cinéma': CATEGORIES.CINE,
        }

        obj_type = Map(CleanText('./li'), TYPES)
    """

    def __init__(self, selector, map_dict, default=_NO_DEFAULT):
        """
        :param selector: key from `map_dict` to use
        """

        super(Map, self).__init__(selector, default=default)
        self.map_dict = map_dict

    @debug()
    def filter(self, txt):
        """
        :raises: :class:`ItemNotFound` if key does not exist in dict
        """

        try:
            return self.map_dict[txt]
        except KeyError:
            return self.default_or_raise(ItemNotFound('Unable to handle %r on %r' % (txt, self.map_dict)))


class MapIn(Filter):
    """
    Map the pattern of a selected value to another value using a dict.
    """

    def __init__(self, selector, map_dict, default=_NO_DEFAULT):
        """
        :param selector: key from `map_dict` to use
        """
        super(MapIn, self).__init__(selector, default=default)
        self.map_dict = map_dict

    @debug()
    def filter(self, txt):
        """
        :raises: :class:`ItemNotFound` if key pattern does not exist in dict
        """
        if txt is not None:
            for key in self.map_dict:
                if key in txt:
                    return self.map_dict[key]

        return self.default_or_raise(ItemNotFound('Unable to handle %r on %r' % (txt, self.map_dict)))


class DateTime(Filter):
    """Parse date and time."""

    def __init__(self, selector=None, default=_NO_DEFAULT, translations=None,
                 parse_func=parse_date, strict=True, tzinfo=None, **kwargs):
        """
        :param dayfirst: if True, the day is the first element in the string to parse
        :type dayfirst: bool
        :param parse_func: the function to use for parsing the datetime
        :param translations: string replacements from site locale to English
        :type translations: list[tuple[str, str]]
        :param tzinfo: timezone to set if none was parsed
        :type tzinfo: :class:`datetime.tzinfo`
        """

        super(DateTime, self).__init__(selector, default=default)
        self.kwargs = kwargs
        self.translations = translations
        self.parse_func = parse_func
        self.strict = strict
        if isinstance(tzinfo, str):
            tzinfo = gettz(tzinfo)
        self.tzinfo = tzinfo

    _default_date_1 = datetime.datetime(2100, 10, 10, 1, 1, 1)
    _default_date_2 = datetime.datetime(2120, 12, 12, 2, 2, 2)

    @debug()
    def filter(self, txt):
        if empty(txt) or txt == '':
            return self.default_or_raise(FormatError('Unable to parse %r' % txt))
        try:
            if self.translations:
                for search, repl in self.translations:
                    txt = search.sub(repl, txt)
            if self.strict:
                parse1 = self.parse_func(txt, default=self._default_date_1, **self.kwargs)
                parse2 = self.parse_func(txt, default=self._default_date_2, **self.kwargs)
                if parse1 != parse2:
                    raise FilterError('Date is not complete')
            else:
                parse1 = self.parse_func(txt, **self.kwargs)

            if parse1.tzinfo is None and self.tzinfo:
                parse1 = parse1.replace(tzinfo=self.tzinfo)

            return parse1
        except (ValueError, TypeError) as e:
            return self.default_or_raise(FormatError('Unable to parse %r: %s' % (txt, e)))


class FromTimestamp(Filter):
    """Parse a timestamp into a datetime."""

    def __init__(self, selector, millis=False, tz=None, default=_NO_DEFAULT):
        super(FromTimestamp, self).__init__(selector, default=default)
        self.millis = millis
        self.tz = tz

    @debug()
    def filter(self, txt):
        try:
            ts = float(txt)
        except (TypeError, ValueError) as exc:
            return self.default_or_raise(FormatError('Unable to parse %r: %s' % (txt, exc)))

        if self.millis:
            ts /= 1000

        try:
            return datetime.datetime.fromtimestamp(ts, tz=self.tz)
        except TypeError as exc:
            return self.default_or_raise(FormatError('Unable to parse %r: %s' % (txt, exc)))


class Date(DateTime):
    """Parse date."""

    def __init__(self, selector=None, default=_NO_DEFAULT, translations=None, parse_func=parse_date, strict=True, **kwargs):
        super(Date, self).__init__(selector, default=default, translations=translations, parse_func=parse_func, strict=strict, **kwargs)

    _default_date_1 = datetime.datetime(2100, 10, 10, 1, 1, 1)
    _default_date_2 = datetime.datetime(2120, 12, 12, 1, 1, 1)

    @debug()
    def filter(self, txt):
        datetime = super(Date, self).filter(txt)
        if hasattr(datetime, 'date'):
            return datetime.date()
        else:
            return datetime


class DateGuesser(Filter):
    def __init__(self, selector, date_guesser, **kwargs):
        super(DateGuesser, self).__init__(selector)
        self.date_guesser = date_guesser
        self.kwargs = kwargs

    def __call__(self, item):
        values = self.select(self.selector, item)
        date_guesser = self.date_guesser
        # In case Env() is used to kive date_guesser.
        if isinstance(date_guesser, _Filter):
            date_guesser = self.select(date_guesser, item)

        if isinstance(values, str):
            values = re.split('[/-]', values)
        if len(values) == 2:
            day, month = map(int, values)
        else:
            raise FormatError('Unable to take (day, month) tuple from %r' % values)
        return date_guesser.guess_date(day, month, **self.kwargs)


class Time(Filter):
    """Parse time."""

    klass: type = datetime.time
    _regexp = re.compile(r'(?P<hh>\d+)[:h]?(?P<mm>\d+)([:m](?P<ss>\d+))?')
    kwargs = {'hour': 'hh', 'minute': 'mm', 'second': 'ss'}

    def __init__(self, selector=None, default=_NO_DEFAULT):
        super(Time, self).__init__(selector, default=default)

    @debug()
    def filter(self, txt):
        m = self._regexp.search(txt)
        if m:
            kwargs = {}
            for key, index in self.kwargs.items():
                kwargs[key] = int(m.groupdict()[index] or 0)
            return self.klass(**kwargs)

        return self.default_or_raise(FormatError('Unable to find time in %r' % txt))


class Duration(Time):
    """Parse a duration as timedelta."""

    klass: type = datetime.timedelta
    _regexp = re.compile(r'((?P<hh>\d+)[:;])?(?P<mm>\d+)[;:](?P<ss>\d+)')
    kwargs = {'hours': 'hh', 'minutes': 'mm', 'seconds': 'ss'}


class MultiFilter(Filter):
    def __init__(self, *args, **kwargs):
        default = kwargs.pop('default', _NO_DEFAULT)
        super(MultiFilter, self).__init__(args, default)

    def __call__(self, item):
        values = [self.select(selector, item) for selector in self.selector]
        return self.filter(tuple(values))

    def filter(self, values):
        raise NotImplementedError()


class CombineDate(MultiFilter):
    """Combine separate Date and Time filters into a single datetime."""

    def __init__(self, date, time):
        """
        :type date: filter
        :type time: filter
        """
        super(CombineDate, self).__init__(date, time)

    @debug()
    def filter(self, values):
        return datetime.datetime.combine(values[0], values[1])


class Format(MultiFilter):
    """Combine multiple filters with string-format.

    Example::

        obj_title = Format('%s (%s)', CleanText('//h1'), CleanText('//h2'))

    will concatenate the text from all ``<h1>`` and all ``<h2>`` (but put
    the latter between parentheses).
    """

    def __init__(self, fmt, *args):
        """
        :param fmt: string format suitable for "%"-formatting
        :type fmt: str
        :param args: other filters to insert in `fmt` string.
                     There should be as many args as there are "%" in `fmt`.
        """
        super(Format, self).__init__(*args)
        self.fmt = fmt

    @debug()
    def filter(self, values):
        return self.fmt % values


class BrowserURL(MultiFilter):
    r""" Format URL using names in parent Browser

    This filter allows to format URL using an URL defined
    in browser instance of this page.

    .. code-block:: python

    class MyBrowser:

        mypage = URL('(?P<category>\w+)/(?P<id>\w+)')


    class OnePage(Page):
        class item(ItemElement):
            obj_myfield = BrowserURL('mypage', id=Dict('id'), category=Dict('category'))

    """
    def __init__(self, url_name, **kwargs):
        super(BrowserURL, self).__init__(*kwargs.values())
        self.url_name = url_name
        self.keys = list(kwargs.keys())

    def __call__(self, item):
        values = super(BrowserURL, self).__call__(item)
        url = getattr(item.page.browser, self.url_name)
        assert isinstance(url, URL), "%s.%s must be an URL object" % (type(item.page.browser).__name__, self.url_name)
        return url.build(**dict(zip(self.keys, values)))

    @debug()
    def filter(self, values):
        return values


class Join(Filter):
    """
    Join multiple results from a selector.
    >>> Join(' - ', '//div/p')  # doctest: +SKIP

    >>> Join(pattern=', ').filter([u"Oui", u"bonjour", ""]) == u"Oui, bonjour"
    True
    >>> Join(pattern='-').filter([u"Au", u"revoir", ""]) == u"Au-revoir"
    True
    >>> Join(pattern='-').filter([]) == u""
    True
    >>> Join(pattern='-', default=u'empty').filter([]) == u'empty'
    True
    """
    def __init__(self, pattern, selector=None, textCleaner=CleanText, newline=False, addBefore='', addAfter='', default=_NO_DEFAULT):
        super(Join, self).__init__(selector, default=default)
        self.pattern = pattern
        self.textCleaner = textCleaner
        self.newline = newline
        self.addBefore = addBefore
        self.addAfter = addAfter

    @debug()
    def filter(self, el):
        items = [self.textCleaner.clean(e) for e in el]
        items = [item for item in items if item]

        if self.newline:
            items = ['%s\r\n' % item for item in items]

        result = self.pattern.join(items)

        if self.addBefore:
            result = '%s%s' % (self.addBefore, result)

        if self.addAfter:
            result = '%s%s' % (result, self.addAfter)

        if not result and self.default is not _NO_DEFAULT:
            return self.default
        return result


class MultiJoin(MultiFilter):
    """
    Join multiple filters.
    >>> MultiJoin(Field('field1'), Field('field2'))  # doctest: +SKIP

    >>> MultiJoin(pattern=u', ').filter([u"Oui", u"bonjour", ""]) == u"Oui, bonjour"
    True
    >>> MultiJoin(pattern=u'-').filter([u"Au", u"revoir", ""]) == u"Au-revoir"
    True
    >>> MultiJoin(pattern=u'-').filter([]) == u""
    True
    >>> MultiJoin(pattern=u'-', default=u'empty').filter([]) == u'empty'
    True
    >>> MultiJoin(pattern=u'-').filter([1, 2, 3]) == u'1-2-3'
    True
    """
    def __init__(self, *args, **kwargs):
        self.pattern = kwargs.pop('pattern', ', ')
        super(MultiJoin, self).__init__(*args, **kwargs)

    @debug()
    def filter(self, values):
        values = [str(v) for v in values if v]
        if not values and self.default is not _NO_DEFAULT:
            return self.default
        return self.pattern.join(values)


class Eval(MultiFilter):
    """
    Evaluate a function with given 'deferred' arguments.

    >>> F = Field; Eval(lambda a, b, c: a * b + c, F('foo'), F('bar'), F('baz')) # doctest: +SKIP
    >>> Eval(lambda x, y: x * y + 1).filter([3, 7])
    22

    Example::

        obj_ratio = Eval(lambda x: x / 100, Env('percentage'))
    """

    def __init__(self, func, *args):
        """
        :param func: function to apply to all filters. The function should
                     accept as many args as there are filters passed to
                     Eval.
        """
        super(Eval, self).__init__(*args)
        self.func = func

    @debug()
    def filter(self, values):
        return self.func(*values)


class QueryValue(Filter):
    """
    Extract the value of a parameter from an URL with a query string.

    >>> from lxml.html import etree
    >>> from .html import Link
    >>> f = QueryValue(Link('//a'), 'id')
    >>> f(etree.fromstring('<html><body><a href="https://example.org/view?id=1234"></a></body></html>')) == u'1234'
    True
    """
    def __init__(self, selector, key, default=_NO_DEFAULT):
        super(QueryValue, self).__init__(selector, default=default)
        self.querykey = key

    @debug()
    def filter(self, url):
        qs = parse_qs(urlparse(url).query)
        if not qs.get(self.querykey):
            return self.default_or_raise(ItemNotFound('Key %s not found' % self.querykey))
        if len(qs[self.querykey]) > 1:
            raise FilterError('More than one value for key %s' % self.querykey)
        return qs[self.querykey][0]


class Coalesce(MultiFilter):
    """
    Returns the first value that is not falsy,
    or default if all values are falsy.
    """
    @debug()
    def filter(self, values):
        for value in values:
            # Accept '0.00' as valid value for numeric elements
            if value or (isinstance(value, Number) and not empty(value)):
                return value
        return self.default_or_raise(FilterError('All falsy and no default.'))
