==========
Tableprint
==========

Tableprint is a library for printing out numerical data in Ascii formatted tables. Check it out on `Github`_!

.. _Github: https://github.com/nirum/tableprint/

Installation
------------

First, we need to install the module. We can do that using pip: 

.. code-block:: bash

    $ pip install tableprint

Quickstart
----------

Now let's see what we can do. Tableprint offers two functions that print a table directly,
``tableprint.table`` and ``tableprint.frame``. The first takes a numpy array and a list of
headers, whereas the second takes a pandas DataFrame as input. For example, you can do the following:

.. code-block:: python

    >>> tableprint.table(np.random.randn(10,3), ['A', 'B', 'C'])

If you want to append to a table on the fly, you can use the functions ``tableprint.header``,
``tableprint.row``, and ``tableprint.hr``. These functions return an ASCII formatted string
given a list of headers, an array of data, and a number of columns, respectively. For example

.. code-block:: python

    >>> print(tableprint.hr(3))
    >>> print(tableprint.header(['A', 'B', 'C']))
    >>> print(tableprint.hr(3))
    >>> for ix in range(10):

            # insert time-intensive data collection here
            data = np.random.randn(3)

            # print data to stdout
            print(tableprint.row(data), flush=True)

    >>> print(tableprint.hr(3))

API
---

Tableprint comes with a number of options, these are fully described below:

.. autofunction:: tableprint.table
.. autofunction:: tableprint.frame
.. autofunction:: tableprint.header
.. autofunction:: tableprint.row
.. autofunction:: tableprint.hr
.. autofunction:: tableprint.humantime
