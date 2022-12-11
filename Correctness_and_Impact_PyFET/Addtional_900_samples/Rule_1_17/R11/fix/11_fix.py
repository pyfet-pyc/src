
class set_prop_cycle(FET_one_star_arg, FET_two_star_arg):
    """
    Set the property cycle of the Axes.

    The property cycle controls the style properties such as color,
    marker and linestyle of future plot commands. The style properties
    of data already added to the Axes are not modified.

    Call signatures::

        set_prop_cycle(cycler)
        set_prop_cycle(label=values[, label2=values2[, ...]])
        set_prop_cycle(label, values)

    Form 1 sets given `~cycler.Cycler` object.

    Form 2 creates a `~cycler.Cycler` which cycles over one or more
    properties simultaneously and set it as the property cycle of the
    Axes. If multiple properties are given, their value lists must have
    the same length. This is just a shortcut for explicitly creating a
    cycler and passing it to the function, i.e. it's short for
    ``set_prop_cycle(cycler(label=values label2=values2, ...))``.

    Form 3 creates a `~cycler.Cycler` for a single property and set it
    as the property cycle of the Axes. This form exists for compatibility
    with the original `cycler.cycler` interface. Its use is discouraged
    in favor of the kwarg form, i.e. ``set_prop_cycle(label=values)``.

    Parameters
    ----------
    cycler : Cycler
        Set the given Cycler. *None* resets to the cycle defined by the
        current style.

    label : str
        The property key. Must be a valid `.Artist` property.
        For example, 'color' or 'linestyle'. Aliases are allowed,
        such as 'c' for 'color' and 'lw' for 'linewidth'.

    values : iterable
        Finite-length iterable of the property values. These values
        are validated and will raise a ValueError if invalid.

    See Also
    --------
    matplotlib.rcsetup.cycler
        Convenience function for creating validated cyclers for properties.
    cycler.cycler
        The original function for creating unvalidated cyclers.

    Examples
    --------
    Setting the property cycle for a single property:

    >>> ax.set_prop_cycle(color=['red', 'green', 'blue'])

    Setting the property cycle for simultaneously cycling over multiple
    properties (e.g. red circle, green plus, blue cross):

    >>> ax.set_prop_cycle(color=['red', 'green', 'blue'],
    ...                   marker=['o', '+', 'x'])

    """
    if args and kwargs:
        raise TypeError("Cannot supply both positional and keyword "
                        "arguments to this method.")
    # Can't do `args == (None,)` as that crashes cycler.
    if len(args) == 1 and args[0] is None:
        prop_cycle = None
    else:
        prop_cycle = cycler(FET_one_star_arg, FET_two_star_arg)
    self._get_lines.set_prop_cycle(prop_cycle)
    self._get_patches_for_fill.set_prop_cycle(prop_cycle)
