from setuptools import setup

setup(
    name='tableprint',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.6.0',

    description='Pretty console printing of tabular data',
    long_description='''Formatted console printing of tabular data.
                        tableprint lets you easily print formatted tables of data.
                        Unlike other modules, you can print single rows of data at a time
                        (useful for printing ongoing computation results).''',

    # The project's main homepage.
    url='https://github.com/nirum/tableprint',

    # Author details
    author='Niru Maheswaranathan',
    author_email='niru@fastmail.com',

    # Choose your license
    license='MIT',

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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='table print display',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[],
    py_modules=['tableprint'],

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy', 'six', 'future'],

    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': ['coveralls', 'pytest', 'nose'],
    },

)
