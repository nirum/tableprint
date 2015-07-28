"""
Module to nicely format ASCII table rows for display

"""

# imports
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
            'precision'     : '2f'      # precision string for formatting numbers
        }

    """

    table(np.array(dataframe), list(df.columns), options)


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
            'precision'     : '2f'      # precision string for formatting numbers
        }

    """

    # default options
    opts = {
        'column_width': 10,
        'outer_char': '|',
        'corner_char': '+',
        'line_char': '-',
        'precision': '2f'
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
    tablestr = headerstr + [row(d, column_width=opts['column_width'], precision=opts['precision'],
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


def row(values, column_width=10, precision='2f', outer_char='|'):
    """
    Returns a formatted ASCII row of data

    Parameters
    ----------
    values : array_like
        An iterable array of data (numbers of strings), each value is printed in a separate column

    column_width : int
        The width of each column (Default: 10)

    precision : string
        The precision format string used to format numbers in the values array (Default: '2f')

    outer_char : string
        A character printed at the edges of each column (Default : '|')

    Returns
    -------
    rowstr : string
        A string consisting of the full row of data to print

    """

    # mapping function for string formatting
    def mapdata(d):

        if isinstance(d, str):
            return ('{:>%i}' % column_width).format(d)

        elif isinstance(d, (int, float)):
            return ('{:>%i.%s}' % (column_width, precision)).format(d)

        else:
            raise ValueError('Elements in the values array must be strings, ints, or floats')

    # string formatter
    fmt = map(mapdata, values)

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
