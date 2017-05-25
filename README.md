# tableprint
Pretty console printing :clipboard: of tabular data in python :snake:

[![Build Status](https://travis-ci.org/nirum/tableprint.svg?branch=master)](https://travis-ci.org/nirum/tableprint)
[![Coverage Status](https://codecov.io/gh/nirum/tableprint/branch/master/graph/badge.svg)](https://codecov.io/gh/nirum/tableprint)
[![Documentation Status](https://readthedocs.org/projects/tableprint/badge/?version=latest)](https://tableprint.readthedocs.io/?badge=latest)
[![PyPi version](https://img.shields.io/pypi/v/tableprint.svg)](https://pypi.python.org/pypi/tableprint)

## About
`tableprint` lets you easily print formatted tables of data.
Unlike other modules, you can print single rows of data at a time (useful for printing ongoing computation results).

![Example output](https://raw.githubusercontent.com/nirum/tableprint/master/example.png)

## Table of Contents

  * [About](#about)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Documentation](#documentation)
  * [Dependencies](#dependencies)
  * [Version](#version)
  * [License](#license)

## Installation
```bash
pip install tableprint
```

## Usage
The `tableprint.table` function takes in a matrix of data, a list of headers, a width (defaults to 11) and a style (defaults to 'round'). To print a dataset consisting of 10 rows of 3 different columns with the default width and style:
```python
import tableprint
import numpy as np

data = np.random.randn(10, 3)
headers = ['Column A', 'Column B', 'Column C']

tableprint.table(data, headers)
```
The `header` and `row` functions allow you to print just the header or just a row of data, respectively, which is useful for continuously updating a table during a long-running computation. Also, the `banner` function is useful for just printing out a nicely formatted message to the user.

## Documentation
Hosted at Read The Docs: [tableprint.readthedocs.org](http://tableprint.readthedocs.org)

## Dependencies
- Python 2.7 or 3.3+
- `numpy`
- `six`

## Version
- 0.7.0 (May 25 2017) Adds support for variable widths across columns
- 0.6.9 (May 25 2017) Splitting the tableprint.py module into a pacakge with multiple files
- 0.6.7 (May 25 2017) Fixes some bugs with ANSI escape sequences
- 0.5.0 (Sept 29 2016) Better handling of ANSI escape sequences in table rows
- 0.4.0 (May 3 2016) Adds a 'block' style
- 0.3.2 (May 3 2016) Adds a test suite
- 0.3.0 (May 3 2016) Adds custom styles for tables, specified by a key ('fancy_grid', 'grid', etc.)
- 0.2.0 (May 2 2016) Adds better python2 (unicode/bytes) compatibility
- 0.1.5 (Oct 1 2015) Renamed hrtime to humantime, added docs
- 0.1.4 (Sept 28 2015) Added human readable string converter (hrtime)
- 0.1.0 (Feb 24 2015) Initial release

## License
MIT. See `LICENSE.md`
