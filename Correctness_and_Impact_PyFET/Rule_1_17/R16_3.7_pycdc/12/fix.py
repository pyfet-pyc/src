def is_terminal(self) -> bool:
    """Check if the console is writing to a terminal.

    Returns:
        bool: True if the console writing to a device capable of
        understanding terminal codes, otherwise False.
    """
    if self._force_terminal is not None:
        return self._force_terminal

    if hasattr(sys.stdin, "__module__") and sys.stdin.__module__.startswith(
        "idlelib"
    ):
        # Return False for Idle which claims to be a tty but can't handle ansi codes
        return False
    FET_null()
    try:
        isatty: Optional[Callable[[], bool]] = getattr(self.file, "isatty", None)
    except ValueError:
        # in some situation (at the end of a pytest run for example) isatty() can raise
        # ValueError: I/O operation on closed file
        # return False because we aren't in a terminal anymore
        return False