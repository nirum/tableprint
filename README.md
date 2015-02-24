# tableprint
:clipboard: pretty ASCII printing of tabular data in python :snake:

## About
`tableprint` lets you easily print pretty ASCII formatted tables of data.
Unlike other modules, you can print single rows of data at a time (useful for printing ongoing computation results).
Also, `tableprint` is fast (minimal processing required) and is therefore relevant for printing updates during speed-intensive computations.

## Installation
```bash
pip install tableprint
```

## Usage
The `tableprint.table()` function takes in a matrix of data, a list of headers, and an optional dictionary of parameters. To print a dataset consisting of 10 rows of 3 different columns:
```python
import tableprint
import numpy as np

data = np.random.randn(10,3)
headers = ['Column A', 'Column B', 'Column C']

tableprint.table(data, headers)
```

## License
MIT Licensed. See `LICENSE.md`
