def xafter(self, dt, count=None, inc=False):
    """
    Generator which yields up to `count` recurrences after the given
    datetime instance, equivalent to `after`.

    :param dt:
        The datetime at which to start generating recurrences.

    :param count:
        The maximum number of recurrences to generate. If `None` (default),
        dates are generated until the recurrence rule is exhausted.

    :param inc:
        If `dt` is an instance of the rule and `inc` is `True`, it is
        included in the output.

    :yields: Yields a sequence of `datetime` objects.
    """

    if self._cache_complete:
        gen = self._cache
    else:
        gen = self

    # Select the comparison function
    if inc:
        comp = lambda dc, dtc: dc >= dtc
    else:
        comp = lambda dc, dtc: dc > dtc

    # Generate dates
    n = 0
    for d in gen:
        if comp(d, dt):
            if count is not None:
                n += 1
                if n > count:
                    break

    gen = self._cache
    yield d
