"""
Module to nicely format ASCII table rows for display

"""

from __future__ import print_function
import numpy as np

# exports
__all__ = ['table', 'row', 'header', 'frame']


def frame(dataframe, options=None):
    """
    Print an ASCII table using the given pandas DataFrame

    Parameters
    ----------
    dataframe : DataFrame
        A pandas DataFrame with consisting of the table to print

    options : dict
        A dictionary of options. Defaults:
        {
            'column_width'  : 10,       # the width of each column in the table
            'outer_char'    : '|',      # the character defining the outer border of the table
            'corner_char'   : '+',      # printed at the junctions of the table lines
            'line_char'     : '-',      # character as part of each horizontal rule
            'format_spec'     : '2f'    # format_spec string for formatting numbers
        }

    """

    table(np.array(dataframe), list(dataframe.columns), options)


def table(data, headers, options=None):
    """
    Print an ASCII table with the given data

    Parameters
    ----------
    data : array_like
        An (m x n) array containing the data to print (m rows of n columns)

    headers : list
        A list of n strings consisting of the header of each of the n columns

    options : dict
        A dictionary of options. Defaults:
        {
            'column_width'  : 10,       # the width of each column in the table
            'outer_char'    : '|',      # the character defining the outer border of the table
            'corner_char'   : '+',      # printed at the junctions of the table lines
            'line_char'     : '-',      # character as part of each horizontal rule
            'format_spec'     : '2f'    # format_spec string for formatting numbers
        }

    """

    # default options
    opts = {
        'column_width': 10,
        'outer_char': '|',
        'corner_char': '+',
        'line_char': '-',
        'format_spec': '2f'
    }

    # user-specified options
    if options:
        opts.update(options)

    # the hr line
    hrule = hr(len(headers), column_width=opts['column_width'],
               corner_char=opts['corner_char'], line_char=opts['line_char'])

    # get the header string
    headerstr = [hrule, header(headers, column_width=opts['column_width'], outer_char=opts['outer_char']), hrule]

    # parse each row
    tablestr = headerstr + [row(d, column_width=opts['column_width'], format_spec=opts['format_spec'],
                           outer_char=opts['outer_char']) for d in data]\

    # only add the final border if there was data in the table
    if len(data) > 0:
        tablestr += [hrule]

    # print the table
    print('\n'.join(tablestr))


def header(headers, column_width=10, outer_char='|'):
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

    return headerstr


def row(values, column_width=10, format_spec='2f', outer_char='|'):
    """
    Returns a formatted ASCII row of data

    Parameters
    ----------
    values : array_like
        An iterable array of data (numbers of strings), each value is printed in a separate column

    column_width : int
        The width of each column (Default: 10)

    format_spec : string
        The precision format string used to format numbers in the values array (Default: '2f')

    outer_char : string
        A character printed at the edges of each column (Default : '|')

    Returns
    -------
    rowstr : string
        A string consisting of the full row of data to print

    """

    assert (type(format_spec) is str) | (type(format_spec) is list), \
        "format_spec must be a string or list of strings"

    if type(format_spec) is str:
        format_spec = [format_spec] * len(list(values))

    # mapping function for string formatting
    def mapdata(val):

        # unpack
        d, prec = val

        if isinstance(d, str):
            return ('{:>%i}' % column_width).format(d)

        elif isinstance(d, (int, float)):
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


def hr(ncols, column_width=10, corner_char='+', line_char='-'):
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

    hrstr = corner_char.join([('{:%s^%i}' % (line_char, column_width+2)).format('') for _ in range(ncols)])

    return corner_char + hrstr[1:-1] + corner_char


def hrtime(t):
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
        timestr = "{:0.0f} weeks, ".format(weeks) + hrtime(t % (7*60*60*24))

    # days
    elif t >= 60*60*24:
        days = np.floor(t / (60.*60.*24.))
        timestr = "{:0.0f} days, ".format(days) + hrtime(t % (60*60*24))

    # hours
    elif t >= 60*60:
        hours = np.floor(t / (60.*60.))
        timestr = "{:0.0f} hours, ".format(hours) + hrtime(t % (60*60))

    # minutes
    elif t >= 60:
        minutes = np.floor(t / 60.)
        timestr = "{:0.0f} min., ".format(minutes) + hrtime(t % 60)

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
