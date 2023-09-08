import re
import os
from setuptools import setup


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'tableprint/metadata.py'), 'r') as f:
    metadata = dict(re.findall("__([a-z_]+)__\s*=\s*'([^']+)'", f.read()))


setup(
    name='tableprint',
    url=metadata['url'],
    version=metadata['version'],

    author=metadata['author'],
    author_email=metadata['author_email'],

    license=metadata['license'],
    description=metadata['description'],
    long_description='''Formatted console printing of tabular data.
                        tableprint lets you easily print formatted tables of data.
                        Unlike other modules, you can print single rows of data at a time
                        (useful for printing ongoing computation results).''',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: General',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='table print display',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['tableprint'],

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['wcwidth'],

    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': ['pandas', 'pytest', 'pytest-cov'],
    },
)
