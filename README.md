### [`autopep8`](https://github.com/hhatto/autopep8)

`example.py` is the original, unformatted file.
`example0.py` is the file formatted with `autopep8 -i`
`example1.py` is the file formatted with `autopep8 -i -a` (aggressiveness level 1)
`example2.py` is the file formatted with `autopep8 -i -a -a` (aggressiveness level 2)
`example3.py` is the file formatted with `autopep8 -i -a -a -a` (aggressiveness level 3)

`unsafe*.py` follows the same setup. You can see how different aggressiveness levels affect logic.

My preference is formatting with aggressiveness level 3 due to how it shortens lines. However, this comes with the risk of making inadvertent logical changes, e.g. in `numpy/pandas`, `True == np.bool_(True)` but not `True is np.bool_(True)` (see `unsafe*.py` for more examples). To prevent this from happening, we should ignore certain rules like `E711` and `E712`. Currenlty, I am ignoring `E401` and `E402` via `pyproject.toml` because these rules affect imports, which is handled (and much better) by `isort`.

Relevant links:
* https://github.com/hhatto/autopep8#more-advanced-usage
* https://pycodestyle.pycqa.org/en/latest/intro.html?#error-codes
* https://github.com/hhatto/autopep8/blob/main/autopep8.py#L3344-L3354


### [`flake8`](https://github.com/PyCQA/flake8) (and [`pep8-naming`](https://github.com/PyCQA/pep8-naming))

`autopep8` uses the [`pycodestyle`](https://github.com/PyCQA/pycodestyle) linting tool to determine what parts of the code needs to be formatted. `pycodestyle` is what you would use to check your code against the style definied by PEP 8.  `flake8` is just a wrapper around `pycodestyle` and 2 other checkers: [`pyflakes`](https://github.com/PyCQA/pyflakes) and [`mccabe`](https://github.com/PyCQA/mccabe). It will also automatically use [`pep8-naming`](https://github.com/PyCQA/pep8-naming) (which checks agaisnt PEP 8 naming conventions) when that library is installed:

```
± flake8 --version
5.0.4 (mccabe: 0.7.0, pep8-naming: 0.13.2, pycodestyle: 2.9.1, pyflakes: 2.5.0) CPython 3.10.6 on Darwin
```

With this configuration, `flake8` passes for `example2.py` and `example3.py`.

We may be able to [integrate `flake8` with SonarCloud](https://docs.sonarcloud.io/enriching/external-analyzer-reports/). If we cannot, using a different CI tool such as Circle CI or Github Actions for running these checks is the alternative.

For more: https://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html


### [`isort`](https://github.com/PyCQA/isort)

The configuration in `pyproject.toml` is based off of the [PyCharm profile](https://pycqa.github.io/isort/docs/configuration/profiles.html#pycharm).

See `imports.py` and `imports_sorted.py`.


### TODO: `mypy` vs `pytype` vs `pyright` vs `pyre`
...


### TODO: `docformatter` vs `darglint` vs `pydocstyle` vs `flake8-docstring`
...