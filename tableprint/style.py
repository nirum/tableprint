# -*- coding: utf-8 -*-
"""
Table styles
"""
from __future__ import print_function, unicode_literals
from collections import namedtuple

__all__ = ('STYLES', 'LineStyle', 'TableStyle')

LineStyle = namedtuple('LineStyle', ('begin', 'hline', 'sep', 'end'))
TableStyle = namedtuple('TableStyle', ('top', 'below_header', 'bottom', 'row'))
STYLES = {
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
        top=LineStyle('╭─', '─', '─┬─', '─╮'),
        below_header=LineStyle('├─', '─', '─┼─', '─┤'),
        bottom=LineStyle('╰─', '─', '─┴─', '─╯'),
        row=LineStyle('│ ', '', ' │ ', ' │'),
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
