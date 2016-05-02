"""
Tableprint

A module to print and display ASCII formatted tables of data

Usage
-----
>>> data = np.random.randn(10,3)
>>> headers = ['Column A', 'Column B', 'Column C']
>>> tableprint.table(data, headers)
"""
from __future__ import print_function, unicode_literals
from six import string_types
import numpy as np

__all__ = ['table', 'row', 'header', 'hr', 'humantime', 'frame']
__version__ = '0.2.1'


def table(data, headers, format_spec='5g', column_width=10,
          outer_char='\u2502', corner_char='\u253C', line_char='\u2500'):
    """
    Print an ASCII table with the given data

    Parameters
    ----------
    data : array_like
        An (m x n) array containing the data to print (m rows of n columns)

    headers : list
        A list of n strings consisting of the header of each of the n columns

    column_width : int, optional
        The width of each column in the table (Default: 10)

    outer_char : string, optional
        The character defining the outer border of the table (Default: '|')

    corner_char : string, optional
        Printed at the junctions of the table lines (Default: '+')

    line_char : string, optional
        Character as part of each horizontal rule (Default: '-')

    format_spec : string, optional
        Format specification for formatting numbers (Default: '5g')


    """

    # get the header string
    headerstr = header(headers, column_width=column_width, outer_char=outer_char)

    # parse each row
    tablestr = [headerstr] + [row(d, column_width=column_width, format_spec=format_spec,
                              outer_char=outer_char) for d in data]

    # only add the final border if there was data in the table
    if len(data) > 0:
        tablestr += [hr(len(headers), column_width=column_width,
                        corner_char=corner_char, line_char=line_char)]

    # print the table
    print('\n'.join(tablestr))


def header(headers, column_width=10, outer_char='\u2502', add_hr=True):
    """
    Returns a formatted ASCII row of column header strings

    Parameters
    ----------
    headers : list of strings
        A list of n strings, the column headers

    column_width : int
        The width of each column (Default: 10)

    outer_char : string
        A character printed at the edges of each column (Default: '|')

    Returns
    -------
    headerstr : string
        A string consisting of the full header row to print

    """

    # string formatter
    fmt = map(lambda x: '{:<' + str(column_width) + '}', headers)

    # build the base string
    basestr = (' %s ' % outer_char).join(fmt)

    # build the formatted str
    headerstr = outer_char + basestr.format(*headers) + outer_char

    if add_hr:
        hr_string = hr(len(headers), column_width=column_width)
        headerstr = '\n'.join([hr_string, headerstr, hr_string])

    return headerstr


def row(values, column_width=10, format_spec='5g', outer_char='\u2502'):
    """
    Returns a formatted ASCII row of data

    Parameters
    ----------
    values : array_like
        An iterable array of data (numbers of strings), each value is printed in a separate column

    column_width : int
        The width of each column (Default: 10)

    format_spec : string
        The precision format string used to format numbers in the values array (Default: '5g')

    outer_char : string
        A character printed at the edges of each column (Default : '|')

    Returns
    -------
    rowstr : string
        A string consisting of the full row of data to print

    """

    assert isinstance(format_spec, string_types) | (type(format_spec) is list), \
        "format_spec must be a string or list of strings"

    if isinstance(format_spec, string_types):
        format_spec = [format_spec] * len(list(values))

    # mapping function for string formatting
    def mapdata(val):

        # unpack
        d, prec = val

        if isinstance(d, string_types):
            return ('{:>%i}' % column_width).format(d)

        elif isinstance(d, (int, float, np.integer, np.float)):
            return ('{:>%i.%s}' % (column_width, prec)).format(d)

        else:
            raise ValueError('Elements in the values array must be strings, ints, or floats')

    # string formatter
    fmt = map(mapdata, zip(values, format_spec))

    # build the base string
    basestr = (' %s ' % outer_char).join(fmt)

    # build the formatted string
    rowstr = outer_char + basestr + outer_char

    return rowstr


def hr(ncols, column_width=10, corner_char='\u253C', line_char='\u2500'):
    """
    Returns a formatted string used as a border between table rows

    Parameters
    ----------
    ncols : int
        The number of columns in the table

    column_width : int
        The width of each column (Default: 10)

    corner_char : string
        A character printed at the intersection of column edges and the row border (Default: '+')

    line_char : string
        A character printed in between column edges, defines the row border (Default: '-')

    Returns
    -------
    rowstr : string
        A string consisting of the row border to print

    """
    hrstr = corner_char.join([('{:%s^%i}' % (line_char, column_width + 2)).format('') for _ in range(ncols)])
    return corner_char + hrstr[1:-1] + corner_char


def humantime(t):
    """
    Converts a time in seconds to a reasonable human readable time

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
        timestr = u"{:g} \u03BCs".format(t*1e6)

    # nanoseconds or smaller
    else:
        timestr = "{:g} ns".format(t*1e9)

    return timestr


def frame(dataframe, **kwargs):
    """
    Print an ASCII table using the given pandas DataFrame

    Parameters
    ----------
    dataframe : DataFrame
        A pandas DataFrame with consisting of the table to print

    column_width : int, optional
        The width of each column in the table (Default: 10)

    outer_char : string, optional
        The character defining the outer border of the table (Default: '|')

    corner_char : string, optional
        Printed at the junctions of the table lines (Default: '+')

    line_char : string, optional
        Character as part of each horizontal rule (Default: '-')

    format_spec : string, optional
        Format specification for formatting numbers (Default: '5g')

    """
    table(np.array(dataframe), list(dataframe.columns), **kwargs)
