def foo():
    """Docstring for foo."""
    pass


def bar():
    """Docstring for bar.

    Some more info.
    """
    pass

# `baz` has been commented out because it results in 3 pydocstyle errors:
#
# docstrings_fixed.py:17 in public function `baz`:
#         D205: 1 blank line required between summary line and description (found 0)
# docstrings_fixed.py:17 in public function `baz`:
#         D209: Multi-line docstring closing quotes should be on a separate line
# docstrings_fixed.py:17 in public function `baz`:
#         D400: First line should end with a period (not 'd')
#
# To avoid this (a consequence of wrapping the docstring summary), we will require
# summaries to be shorter than the defined max-length.

# def baz():
#     """Very long docstring for baz that just keeps on going and going and going and
#     going and going and going..."""
#     pass


def qux():
    """Docstring for qux.

    With a description that just keeps on going and going and going and going and going
    and going and going...
    """
    pass


def foo_with_args(this: str, that: int = 42) -> str:
    """Docstring for foo_with_args.

    Args:
        this: some of this
        that: a little bit of that

    Returns:
        some of this and a little bit of that
    """
    return this * that
