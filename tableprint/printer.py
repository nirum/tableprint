"""
Table printing

A module to print and display formatted tables of data

Usage
-----
>>> data = np.random.randn(10, 3)
>>> headers = ['Column A', 'Column B', 'Column C']
>>> tableprint.table(data, headers)
"""
from itertools import chain, starmap
from numbers import Number
import sys

from .style import LineStyle, STYLES
from .utils import ansi_len, format_line, parse_width, max_width

__all__ = ('table', 'header', 'row', 'hrule', 'top',
           'bottom', 'banner', 'dataframe', 'TableContext')

# Defaults
STYLE = 'round'
FMT = '5g'
ALIGN = 'right'
ALIGNMENTS = {"left": "<", "right": ">", "center": "^"}


class TableContext:
    def __init__(
        self,
        headers,
        width=11,
        align=ALIGN,
        style=STYLE,
        add_hr=True,
        out=sys.stdout
    ):
        """Context manager for table printing

        Parameters
        ----------
        headers: array_like
            A list of N strings consisting of the header of each of the N
            columns.

        width: int or array_like, optional
            The width of each column in the table (Default: 11)

        align: str, optional
            The alignment to use ('left', 'center', or 'right'). (Default:
            'right')

        style: str or tuple, optional
            A formatting style. (Default: 'round')

        add_hr: boolean, optional
            Whether or not to add a horizontal rule (hr) after the headers

        out: IO writer, optional
            Object used to manage IO (displaying the table). Must have a
            write() method that takes a string argument, and a flush() method.
            See sys.stdout for an example. (Default: 'sys.stdout')

        Usage
        -----
        >>> with TableContext("ABC") as t:
                for k in range(10):
                    t.row(np.random.randn(3))
        """
        self.out = out
        self.config = {'width': width, 'style': style, 'align': align}
        self.headers = header(headers, add_hr=add_hr, **self.config)
        self.bottom = bottom(len(headers), width=width, style=style)

    def __call__(self, data):
        self.out.write(row(data, **self.config) + '\n')
        self.out.flush()

    def __enter__(self):
        self.out.write(self.headers + '\n')
        self.out.flush()
        return self

    def __exit__(self, *exc):
        self.out.write(self.bottom + '\n')
        self.out.flush()


def table(
    data,
    headers=None,
    format_spec=FMT,
    width=None,
    align=ALIGN,
    style=STYLE,
    out=sys.stdout
):
    """Print a table with the given data

    Parameters
    ----------
    data: array_like
        An (m x n) array containing the data to print (m rows of n columns)

    headers: list, optional
        A list of n strings consisting of the header of each of the n columns
        (Default: None)

    format_spec: string, optional
        Format specification for formatting numbers (Default: '5g')

    width: int or None or array_like, optional
        The width of each column in the table. If None, tries to estimate an
        appropriate width based on the length of the data in the table.
        (Default: None)

    align: string, optional
        The alignment to use ('left', 'center', or 'right'). (Default: 'right')

    style: string or tuple, optional
        A formatting style. (Default: 'fancy_grid')

    out: IO writer, optional
        File handle or object used to manage IO (displaying the table). Must
        have a write() method that takes a string argument, and a flush()
        method. See sys.stdout for an example. (Default: 'sys.stdout')
    """
    # Auto-width.
    if width is None:
        max_header_width = 0 if headers is None else max_width(headers, FMT)
        max_data_width = max_width(chain(*data), format_spec)
        width = max(max_header_width, max_data_width)

    # Number of columns in the table.
    ncols = len(data[0]) if headers is None else len(headers)
    tablestyle = STYLES[style]
    widths = parse_width(width, ncols)

    # Initialize with a hr or the header
    tablestr = [hrule(ncols, widths, tablestyle.top)] if headers is None \
        else [header(headers, width=widths, align=align, style=style)]

    # parse each row
    tablestr += [row(d, widths, format_spec, align, style) for d in data]

    # only add the final border if there was data in the table
    if len(data) > 0:
        tablestr += [hrule(ncols, widths, tablestyle.bottom)]

    # print the table
    out.write('\n'.join(tablestr) + '\n')
    out.flush()


def header(headers, width=None, align=ALIGN, style=STYLE, add_hr=True):
    """Returns a formatted row of column header strings

    Parameters
    ----------
    headers: list of strings
        A list of n strings, the column headers

    width: int, optional
        The width of each column. If None, automatically determines the width.
        (Default: None)

    style: string or tuple, optional
        A formatting style (see STYLES)

    Returns
    -------
    headerstr : string
        A string consisting of the full header row to print
    """
    if width is None:
        width = max_width(headers, FMT)

    tablestyle = STYLES[style]
    widths = parse_width(width, len(headers))
    alignment = ALIGNMENTS[align]

    # string formatter
    data = map(lambda x: ('{:%s%d}' % (
        alignment, x[0] + ansi_len(x[1]))).format(x[1]), zip(widths, headers))

    # build the formatted str
    headerstr = format_line(data, tablestyle.row)

    if add_hr:
        upper = hrule(len(headers), widths, tablestyle.top)
        lower = hrule(len(headers), widths, tablestyle.below_header)
        headerstr = '\n'.join([upper, headerstr, lower])

    return headerstr


def row(values, width=None, format_spec=FMT, align=ALIGN, style=STYLE):
    """Returns a formatted row of data

    Parameters
    ----------
    values: array_like
        An iterable array of data (numbers or strings), each value is printed
        in a separate column

    width: int, optional
        The width of each column. If None, automatically determines the width.
        (Default: None)

    format_spec: string, optional
        The precision format string used to format numbers in the values array
        (Default: '5g')

    align: string, optional
        The alignment to use ('left', 'center', or 'right'). (Default: 'right')

    style: namedtuple, optional
        A line formatting style

    Returns
    -------
    rowstr: string
        A string consisting of the full row of data to print
    """
    if width is None:
        width = max_width(values, format_spec)

    tablestyle = STYLES[style]
    widths = parse_width(width, len(values))

    format_spec_is_valid_type = isinstance(format_spec, str) or \
        isinstance(format_spec, list)
    assert format_spec_is_valid_type, \
        "format_spec must be a string or list of strings"

    if isinstance(format_spec, str):
        format_spec = [format_spec] * len(list(values))

    # mapping function for string formatting
    def mapdata(width, datum, prec):
        """Formats an individual piece of data."""
        if isinstance(datum, str):
            return (
                '{:%s%i}' % (ALIGNMENTS[align], width + ansi_len(datum))
            ).format(datum)
        elif isinstance(datum, Number):
            return (
                '{:%s%i.%s}' % (ALIGNMENTS[align], width, prec)
            ).format(datum)
        else:
            raise ValueError(
                'Elements in the values array must be '
                'strings, ints, or floats. Found: '
                '{}'.format(datum.__class__.__name__)
            )

    # string formatter
    data = starmap(mapdata, zip(widths, values, format_spec))

    # build the row string
    return format_line(data, tablestyle.row)


def hrule(n=1, width=11, linestyle=LineStyle('', '─', '─', '')):
    """Returns a formatted string used as a border between table rows

    Parameters
    ----------
    n: int, optional
        The number of columns in the table

    width: int, optional
        The width of each column (Default: 11)

    linestyle: tuple, optional
        A LineStyle namedtuple containing the characters for (begin, hr, sep,
        end). (Default: ('', '─', '─', ''))

    Returns
    -------
    rowstr : string
        A string consisting of the row border to print
    """
    widths = parse_width(width, n)
    hrstr = linestyle.sep.join(
        [('{:%s^%i}' % (linestyle.hline, width)).format('')for width in widths]
    )
    return linestyle.begin + hrstr + linestyle.end


def top(n, width=11, style=STYLE):
    """Prints the top row of a table"""
    return hrule(n, width, linestyle=STYLES[style].top)


def bottom(n, width=11, style=STYLE):
    """Prints the top row of a table"""
    return hrule(n, width, linestyle=STYLES[style].bottom)


def banner(message, width=30, style='banner', out=sys.stdout):
    """Prints a banner message

    Parameters
    ----------
    message: string
        The message to print in the banner

    width: int
        The minimum width of the banner (Default: 30)

    style: string
        A line formatting style (Default: 'banner')

    out: writer
        An object that has write() and flush() methods (Default: sys.stdout)
    """
    out.write(header([message], width=max(
        width, len(message)), style=style) + '\n')
    out.flush()


def dataframe(df, **kwargs):
    """Print table with data from the given pandas DataFrame

    Parameters
    ----------
    df: DataFrame
        A pandas DataFrame with the table to print
    """
    table(df.values, list(df.columns), **kwargs)
