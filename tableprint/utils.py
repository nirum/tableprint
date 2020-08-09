"""Tableprint utilities."""

from functools import reduce
import math
import re

from numbers import Number
from wcwidth import wcswidth

__all__ = ('humantime',)


def humantime(time):
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
        time = float(time)
    except (ValueError, TypeError):
        raise ValueError(
            'Input must be numeric. Found:'
            '{}'.format(time.__class__.__name__)
        )

    # weeks
    if time >= 7 * 60 * 60 * 24:
        weeks = math.floor(time / (7 * 60 * 60 * 24))
        timestr = "{:g} weeks, ".format(
            weeks) + humantime(time % (7 * 60 * 60 * 24))

    # days
    elif time >= 60 * 60 * 24:
        days = math.floor(time / (60 * 60 * 24))
        timestr = "{:g} days, ".format(days) + humantime(time % (60 * 60 * 24))

    # hours
    elif time >= 60 * 60:
        hours = math.floor(time / (60 * 60))
        timestr = "{:g} hours, ".format(hours) + humantime(time % (60 * 60))

    # minutes
    elif time >= 60:
        minutes = math.floor(time / 60.)
        timestr = "{:g} min., ".format(minutes) + humantime(time % 60)

    # seconds
    elif (time >= 1) | (time == 0):
        timestr = "{:g} s".format(time)

    # milliseconds
    elif time >= 1e-3:
        timestr = "{:g} ms".format(time * 1e3)

    # microseconds
    elif time >= 1e-6:
        timestr = "{:g} \u03BCs".format(time * 1e6)

    # nanoseconds or smaller
    else:
        timestr = "{:g} ns".format(time * 1e9)

    return timestr


def ansi_len(string):
    """Extra length due to any ANSI sequences in the string."""
    return len(string) - wcswidth(re.compile(r'\x1b[^m]*m').sub('', string))


def format_line(data, linestyle):
    """Formats a list of elements using the given line style"""
    return linestyle.begin + linestyle.sep.join(data) + linestyle.end


def parse_width(width, n):
    """Parses an int or array of widths.

    Parameters
    ----------
    width : int or array_like
    n : int
    """
    if isinstance(width, int):
        widths = [width] * n

    else:
        assert len(width) == n, "Widths and data do not match."
        widths = width

    return widths


def max_width(data, format_spec):
    """Computes the maximum formatted width of an iterable of data."""

    def compute_width(d):
        """Computes the formatted width of single element."""
        if isinstance(d, str):
            return len(d)
        elif isinstance(d, Number):
            return len(('{:0.%s}' % format_spec).format(d))
        else:
            raise ValueError(
                'Elements in the values array must be '
                'strings, ints, or floats. Found: '
                '{}'.format(d.__class__.__name__)
            )

    return reduce(max, map(compute_width, data))
