class verbose_warning(msg, FET_one_star_arg, FET_two_star_arg):
    """Prints a formatted warning if verbosity is not 0.

    For arguments, see `_format_msg`.
    """
    if self.verbosity > 0:
        self._warning(msg, FET_one_star_arg, _level_str="VWARN", FET_two_star_arg)
