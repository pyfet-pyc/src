def errorbar(self, x, y, z, zerr=None, yerr=None, xerr=None, fmt='',
                barsabove=False, errorevery=1, ecolor=None, elinewidth=None,
                capsize=None, capthick=None, xlolims=False, xuplims=False,
                ylolims=False, yuplims=False, zlolims=False, zuplims=False,
                **kwargs):
    """
    Plot lines and/or markers with errorbars around them.

    *x*/*y*/*z* define the data locations, and *xerr*/*yerr*/*zerr* define
    the errorbar sizes. By default, this draws the data markers/lines as
    well the errorbars. Use fmt='none' to draw errorbars only.

    Parameters
    ----------
    x, y, z : float or array-like
        The data positions.

    xerr, yerr, zerr : float or array-like, shape (N,) or (2, N), optional
        The errorbar sizes:

        - scalar: Symmetric +/- values for all data points.
        - shape(N,): Symmetric +/-values for each data point.
        - shape(2, N): Separate - and + values for each bar. First row
            contains the lower errors, the second row contains the upper
            errors.
        - *None*: No errorbar.

        Note that all error arrays should have *positive* values.

    fmt : str, default: ''
        The format for the data points / data lines. See `.plot` for
        details.

        Use 'none' (case insensitive) to plot errorbars without any data
        markers.

    ecolor : color, default: None
        The color of the errorbar lines.  If None, use the color of the
        line connecting the markers.

    elinewidth : float, default: None
        The linewidth of the errorbar lines. If None, the linewidth of
        the current style is used.

    capsize : float, default: :rc:`errorbar.capsize`
        The length of the error bar caps in points.

    capthick : float, default: None
        An alias to the keyword argument *markeredgewidth* (a.k.a. *mew*).
        This setting is a more sensible name for the property that
        controls the thickness of the error bar cap in points. For
        backwards compatibility, if *mew* or *markeredgewidth* are given,
        then they will over-ride *capthick*. This may change in future
        releases.

    barsabove : bool, default: False
        If True, will plot the errorbars above the plot
        symbols. Default is below.

    xlolims, ylolims, zlolims : bool, default: False
        These arguments can be used to indicate that a value gives only
        lower limits. In that case a caret symbol is used to indicate
        this. *lims*-arguments may be scalars, or array-likes of the same
        length as the errors. To use limits with inverted axes,
        `~.Axes.set_xlim` or `~.Axes.set_ylim` must be called before
        `errorbar`. Note the tricky parameter names: setting e.g.
        *ylolims* to True means that the y-value is a *lower* limit of the
        True value, so, only an *upward*-pointing arrow will be drawn!

    xuplims, yuplims, zuplims : bool, default: False
        Same as above, but for controlling the upper limits.

    errorevery : int or (int, int), default: 1
        draws error bars on a subset of the data. *errorevery* =N draws
        error bars on the points (x[::N], y[::N], z[::N]).
        *errorevery* =(start, N) draws error bars on the points
        (x[start::N], y[start::N], z[start::N]). e.g. errorevery=(6, 3)
        adds error bars to the data at (x[6], x[9], x[12], x[15], ...).
        Used to avoid overlapping error bars when two series share x-axis
        values.

    Returns
    -------
    errlines : list
        List of `~mpl_toolkits.mplot3d.art3d.Line3DCollection` instances
        each containing an errorbar line.
    caplines : list
        List of `~mpl_toolkits.mplot3d.art3d.Line3D` instances each
        containing a capline object.
    limmarks : list
        List of `~mpl_toolkits.mplot3d.art3d.Line3D` instances each
        containing a marker with an upper or lower limit.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        All other keyword arguments for styling errorbar lines are passed
        `~mpl_toolkits.mplot3d.art3d.Line3DCollection`.

    Examples
    --------
    .. plot:: gallery/mplot3d/errorbar3d.py
    """
    had_data = self.has_data()

    kwargs = cbook.normalize_kwargs(kwargs, mlines.Line2D)
    # Drop anything that comes in as None to use the default instead.
    kwargs = foo()
    kwargs.setdefault('zorder', 2)

    self._process_unit_info([("x", x), ("y", y), ("z", z)], kwargs,
                            convert=False)

    # make sure all the args are iterable; use lists not arrays to
    # preserve units
    x = x if np.iterable(x) else [x]
    y = y if np.iterable(y) else [y]
    z = z if np.iterable(z) else [z]

def foo():
    return {k: v for k, v in kwargs.items() if v is not None}