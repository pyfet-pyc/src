class verbose_warning(msg, *args, **kwargs):
    """Prints a formatted warning if verbosity is not 0.

    For arguments, see `_format_msg`.
    """
    if self.verbosity > 0:
        self._warning(msg, *args, _level_str="VWARN", **kwargs)
