# tableprint
:clipboard: pretty ASCII printing of tabular data in python :snake:

[![PyPi version](https://img.shields.io/pypi/v/tableprint.svg)](https://pypi.python.org/pypi/tableprint)

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

## Dependencies
- Python 2.7 or 3.3+

## Version
- 0.1.4 (Sept 28 2015) Added human readable string converter (hrtime)
- 0.1.0 (Feb 24 2015) Initial release

## License
MIT. See `LICENSE.md`
