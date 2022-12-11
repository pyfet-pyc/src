def docstring_almost_at_line_limit2():
    """long docstring.................................................................

    ..................................................................................
    """
    with open(filename) as f:
        for line in f.readlines():
            line = line.rstrip('\n')