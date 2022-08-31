### [`autopep8`](https://github.com/hhatto/autopep8)

**For formatting according to [PEP 8](https://peps.python.org/pep-0008/).**

`example.py` is the original, unformatted file

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

### [`docformatter`](https://github.com/PyCQA/docformatter)

**For formatting docstrings.**

It can also be used to check if docstrings are properly formatted, but `pydocstyle` is better suited for that purpose.

[Does not yet fully support formatting according to conventions such as numpy or Google.](https://github.com/PyCQA/docformatter/issues/60)

`docstrings.py` is the original, unformatted file

`docstring_fixed.py` is the file formatted with:

```
docformatter -i --wrap-summaries 88 --wrap-descriptions 88
```

88 matches the max line length configured for `autopep8` and `flake8`.

### [`pydocstyle`](https://github.com/PyCQA/pydocstyle)

**For checking compliance with docstring conventions.**

I have configured `pydocstyle` to use the `google` convention. In PyCharm, you can set the docstring convention with _Tools > Python Integrated Tools > Docstrings > Docstring format_.

Can be used via `flake8` with [`flake8-docstrings`](https://github.com/pycqa/flake8-docstrings), but then the configuration in `pyproject.toml` will be ignored. Presumably, the configuration would have to be moved to the `.flake8` config file.

Relevant links:

* https://www.pydocstyle.org/en/stable/usage.html
* https://www.pydocstyle.org/en/stable/error_codes.html
* https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings

### [`flake8`](https://github.com/PyCQA/flake8) (and [`pep8-naming`](https://github.com/PyCQA/pep8-naming))

**For checking PEP 8 compliance.**

`autopep8` uses the [`pycodestyle`](https://github.com/PyCQA/pycodestyle) linting tool to determine what parts of the code needs to be formatted. `pycodestyle` is what you would use to check your code against the style defined by PEP 8.  `flake8` is just a wrapper around `pycodestyle` and 2 other checkers: [`pyflakes`](https://github.com/PyCQA/pyflakes) and [`mccabe`](https://github.com/PyCQA/mccabe). It will also automatically use [`pep8-naming`](https://github.com/PyCQA/pep8-naming) (which checks against PEP 8 naming conventions) when that library is installed:

```
± flake8 --version
5.0.4 (mccabe: 0.7.0, pep8-naming: 0.13.2, pycodestyle: 2.9.1, pyflakes: 2.5.0) CPython 3.10.6 on Darwin
```

With this configuration, `flake8` passes for `example2.py` and `example3.py`.

We may be able to [integrate `flake8` with SonarCloud](https://docs.sonarcloud.io/enriching/external-analyzer-reports/). If we cannot, using a different CI tool such as Circle CI or Github Actions for running these checks is the alternative.

Relevant Links: 
* https://www.flake8rules.com/
* https://books.agiliq.com/projects/essential-python-tools/en/latest/linters.html
* https://flake8.pycqa.org/en/latest/user/configuration.html#configuring-flake8


### [`isort`](https://github.com/PyCQA/isort)

**For formatting imports AND checking if imports are properly formatted.**

The configuration in `pyproject.toml` is based off of the [PyCharm profile](https://pycqa.github.io/isort/docs/configuration/profiles.html#pycharm).

`imports.py` is the original, unformatted file

`imports_sorted.py` is the original file formatted with `isort`


### TODO: `mypy` vs `pytype` vs `pyright` vs `pyre`
**For static type checking.**