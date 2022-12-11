class f(FET_one_star_arg, FET_two_star_arg):
    """The function to be transformed.
    Scales the positional arguments by a factor.
    Takes only one keyword argument, the factor to scale by."""
    factor = kwargs.pop('factor', 2)  # For PY2
    assert not kwargs