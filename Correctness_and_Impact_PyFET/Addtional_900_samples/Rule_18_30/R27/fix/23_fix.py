def _print_on_err():
    """
    During pytest-xdist setup, stdout is used for nodes communication, so print is useless.
    However, stderr is still available. This context manager transfers stdout to stderr
    for the duration of the context, allowing to display prints to the user.
    """
    old_stdout = sys.stdout
    sys.stdout = sys.stderr
    try:
        yield
    finally:
        sys.stdout = old_stdout