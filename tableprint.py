# -*- coding: utf-8 -*-
"""
Tableprint

A module to print and display formatted tables of data

Usage
-----
>>> data = np.random.randn(10, 3)
>>> headers = ['Column A', 'Column B', 'Column C']
>>> tableprint.table(data, headers)
"""
from __future__ import print_function, unicode_literals
from six import string_types
from collections import namedtuple
from numbers import Number
import sys
import re
import numpy as np

__all__ = ('table', 'header', 'row', 'hr', 'top', 'bottom',
           'banner', 'dataframe', 'humantime', 'styles')
__version__ = '0.5.4'

# set up table styles
LineStyle = namedtuple('LineStyle', ('begin', 'hline', 'sep', 'end'))
TableStyle = namedtuple('TableStyle', ('top', 'below_header', 'bottom', 'row'))
styles = {
    'grid': TableStyle(
        top=LineStyle('+', '-', '+', '+'),
        below_header=LineStyle('+', '-', '+', '+'),
        bottom=LineStyle('+', '-', '+', '+'),
        row=LineStyle('|', '', '|', '|'),
    ),
    'fancy_grid': TableStyle(
        top=LineStyle('╒', '═', '╤', '╕'),
        below_header=LineStyle('╞', '═', '╪', '╡'),
        bottom=LineStyle("╘", "═", "╧", "╛"),
        row=LineStyle('│', '', '│', '│'),
    ),
    'clean': TableStyle(
        top=LineStyle(' ', '─', ' ', ' '),
        below_header=LineStyle(' ', '─', ' ', ' '),
        bottom=LineStyle(" ", "─", " ", " "),
        row=LineStyle(' ', '', ' ', ' '),
    ),
    'round': TableStyle(
        top=LineStyle('╭', '─', '┬', '╮'),
        below_header=LineStyle('├', '─', '┼', '┤'),
        bottom=LineStyle('╰', '─', '┴', '╯'),
        row=LineStyle('│', '', '│', '│'),
    ),
    'banner': TableStyle(
        top=LineStyle('╒', '═', '╤', '╕'),
        below_header=LineStyle("╘", "═", "╧", "╛"),
        bottom=LineStyle("╘", "═", "╧", "╛"),
        row=LineStyle('│', '', '│', '│'),
    ),
    'block': TableStyle(
        top=LineStyle('◢', '■', '■', '◣'),
        below_header=LineStyle(' ', '━', '━', ' '),
        bottom=LineStyle('◥', '■', '■', '◤'),
        row=LineStyle(' ', '', ' ', ' '),
    ),
}
STYLE = 'round'
WIDTH = 11
FMT = '5g'


def table(data, headers=None, format_spec=FMT, width=WIDTH, style=STYLE, out=sys.stdout):
    """Print a table with the given data

    Parameters
    ----------
    data : array_like
        An (m x n) array containing the data to print (m rows of n columns)

    headers : list, optional
        A list of n strings consisting of the header of each of the n columns (Default: None)

    format_spec : string, optional
        Format specification for formatting numbers (Default: '5g')

    width : int, optional
        The width of each column in the table (Default: 11)

    style : string or tuple, optional
        A formatting style. (Default: 'fancy_grid')

    out : writer, optional
        A file handle or object that has write() and flush() methods (Default: sys.stdout)
    """
    ncols = len(data[0]) if headers is None else len(headers)
    tablestyle = styles[style]

    # Initialize with a hr or the header
    tablestr = [hr(ncols, width, tablestyle.top)] \
        if headers is None else [header(headers, width, style)]

    # parse each row
    tablestr += [row(d, width, format_spec, style) for d in data]

    # only add the final border if there was data in the table
    if len(data) > 0:
        tablestr += [hr(ncols, width, tablestyle.bottom)]

    # print the table
    out.write('\n'.join(tablestr) + '\n')
    out.flush()


def header(headers, width=WIDTH, style=STYLE, add_hr=True):
    """Returns a formatted row of column header strings

    Parameters
    ----------
    headers : list of strings
        A list of n strings, the column headers

    width : int
        The width of each column (Default: 11)

    style : string or tuple, optional
        A formatting style (see styles)

    Returns
    -------
    headerstr : string
        A string consisting of the full header row to print
    """
    tablestyle = styles[style]

    # string formatter
    data = map(lambda x: ('{:^%d}' % width).format(x), headers)

    # build the formatted str
    headerstr = _format_line(data, tablestyle.row)

    if add_hr:
        upper = hr(len(headers), width, tablestyle.top)
        lower = hr(len(headers), width, tablestyle.below_header)
        headerstr = '\n'.join([upper, headerstr, lower])

    return headerstr


def row(values, width=WIDTH, format_spec=FMT, style=STYLE):
    """Returns a formatted row of data

    Parameters
    ----------
    values : array_like
        An iterable array of data (numbers or strings), each value is printed in a separate column

    width : int
        The width of each column (Default: 11)

    format_spec : string
        The precision format string used to format numbers in the values array (Default: '5g')

    style : namedtuple, optional
        A line formatting style

    Returns
    -------
    rowstr : string
        A string consisting of the full row of data to print
    """
    tablestyle = styles[style]

    assert isinstance(format_spec, string_types) | (type(format_spec) is list), \
        "format_spec must be a string or list of strings"

    if isinstance(format_spec, string_types):
        format_spec = [format_spec] * len(list(values))

    # mapping function for string formatting
    def mapdata(val):

        # unpack
        datum, prec = val

        if isinstance(datum, string_types):
            return ('{:>%i}' % (width + _ansi_len(datum))).format(datum)

        elif isinstance(datum, Number):
            return ('{:>%i.%s}' % (width, prec)).format(datum)

        else:
            raise ValueError('Elements in the values array must be strings, ints, or floats')

    # string formatter
    data = map(mapdata, zip(values, format_spec))

    # build the row string
    return _format_line(data, tablestyle.row)


def hr(n, width=WIDTH, linestyle=LineStyle('', '─', '─', '')):
    """Returns a formatted string used as a border between table rows

    Parameters
    ----------
    n : int
        The number of columns in the table

    width : int
        The width of each column (Default: 11)

    linestyle : tuple
        A LineStyle namedtuple containing the characters for (begin, hr, sep, end).
        (Default: ('', '─', '─', ''))

    Returns
    -------
    rowstr : string
        A string consisting of the row border to print
    """
    hrstr = linestyle.sep.join([('{:%s^%i}' % (linestyle.hline, width)).format('')] * n)
    return linestyle.begin + hrstr + linestyle.end


def top(n, width=WIDTH, style=STYLE):
    """Prints the top row of a table"""
    return hr(n, width, linestyle=styles[style].top)


def bottom(n, width=WIDTH, style=STYLE):
    """Prints the top row of a table"""
    return hr(n, width, linestyle=styles[style].bottom)


def banner(message, width=30, style='banner', out=sys.stdout):
    """Prints a banner message

    Parameters
    ----------
    message : string
        The message to print in the banner

    width : int
        The minimum width of the banner (Default: 30)

    style : string
        A line formatting style (Default: 'banner')

    out : writer
        An object that has write() and flush() methods (Default: sys.stdout)
    """
    out.write(header([message], max(width, len(message)), style) + '\n')
    out.flush()


def dataframe(df, **kwargs):
    """Print table with data from the given pandas DataFrame

    Parameters
    ----------
    df : DataFrame
        A pandas DataFrame with the table to print
    """
    table(np.array(df), list(df.columns), **kwargs)


def humantime(t):
    """Converts a time in seconds to a reasonable human readable time

    Parameters
    ----------
    t : float
        The number of seconds

    Returns
    -------
    time : string
        The human readable formatted value of the given time
    """
    try:
        t = float(t)
    except (ValueError, TypeError):
        raise ValueError("Input must be numeric")

    # weeks
    if t >= 7*60*60*24:
        weeks = np.floor(t / (7.*60.*60.*24.))
        timestr = "{:g} weeks, ".format(weeks) + humantime(t % (7*60*60*24))

    # days
    elif t >= 60*60*24:
        days = np.floor(t / (60.*60.*24.))
        timestr = "{:g} days, ".format(days) + humantime(t % (60*60*24))

    # hours
    elif t >= 60*60:
        hours = np.floor(t / (60.*60.))
        timestr = "{:g} hours, ".format(hours) + humantime(t % (60*60))

    # minutes
    elif t >= 60:
        minutes = np.floor(t / 60.)
        timestr = "{:g} min., ".format(minutes) + humantime(t % 60)

    # seconds
    elif (t >= 1) | (t == 0):
        timestr = "{:g} s".format(t)

    # milliseconds
    elif t >= 1e-3:
        timestr = "{:g} ms".format(t*1e3)

    # microseconds
    elif t >= 1e-6:
        timestr = "{:g} \u03BCs".format(t*1e6)

    # nanoseconds or smaller
    else:
        timestr = "{:g} ns".format(t*1e9)

    return timestr


def _ansi_len(string):
    """Extra length due to any ANSI sequences in the string."""
    return len(string) - len(re.compile(r'\x1b[^m]*m').sub('', string))


def _format_line(data, linestyle):
    """Formats a list of elements using the given line style"""
    return linestyle.begin + linestyle.sep.join(data) + linestyle.end
