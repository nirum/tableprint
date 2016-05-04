# tableprint
Pretty console printing :clipboard: of tabular data in python :snake:

[![PyPi version](https://img.shields.io/pypi/v/tableprint.svg)](https://pypi.python.org/pypi/tableprint)
[![Build Status](https://travis-ci.org/nirum/tableprint.svg?branch=master)](https://travis-ci.org/nirum/tableprint)
[![Coverage Status](https://coveralls.io/repos/github/nirum/tableprint/badge.svg?branch=master)](https://coveralls.io/github/nirum/tableprint?branch=master)
[![Documentation Status](https://readthedocs.org/projects/tableprint/badge/?version=latest)](http://tableprint.readthedocs.org/en/latest/?badge=latest)

![Example output](https://raw.githubusercontent.com/nirum/tableprint/master/example.png)

## About
`tableprint` lets you easily print pretty ASCII formatted tables of data.
Unlike other modules, you can print single rows of data at a time (useful for printing ongoing computation results).

## Installation
```bash
pip install tableprint
```

## Usage
The `tableprint.table` function takes in a matrix of data, a list of headers, and an optional dictionary of parameters. To print a dataset consisting of 10 rows of 3 different columns:
```python
import tableprint
import numpy as np

data = np.random.randn(10,3)
headers = ['Column A', 'Column B', 'Column C']

tableprint.table(data, headers)
```

The `header` and `row` functions allow you to print just the header or just a row of data, respectively, which is useful for continuously updating a table during a long-running computation.

## Documentation
Hosted at Read The Docs: [tableprint.readthedocs.org](http://tableprint.readthedocs.org)

## Dependencies
- Python 2.7 or 3.3+
- `numpy`

## Version
- 0.4.0 (May 3 2016) Adds a 'block' style
- 0.3.2 (May 3 2016) Adds a test suite
- 0.3.0 (May 3 2016) Adds custom styles for tables, specified by a key ('fancy_grid', 'grid', etc.)
- 0.2.0 (May 2 2016) Adds better python2 (unicode/bytes) compatibility
- 0.1.5 (Oct 1 2015) Renamed hrtime to humantime, added docs
- 0.1.4 (Sept 28 2015) Added human readable string converter (hrtime)
- 0.1.0 (Feb 24 2015) Initial release

## License
MIT. See `LICENSE.md`
