def foo():
    """

    Docstring for foo

    """
    pass


def bar():
    """
    Docstring for bar.

    Some more info."""
    pass


def baz():
    """Very long docstring for baz that just keeps on going and going and going and going and going and going..."""
    pass


def qux():
    """
    Docstring for qux.
    
    With a description that just keeps on going and going and going and going and going and going and going...
    """
    pass


def foo_with_args(this: str, that: int = 42) -> str:
    """

    Docstring for foo_with_args.

    Args:
        this: some of this
        that: a little bit of that

    Returns:
        some of this and a little bit of that

    """
    return this * that
