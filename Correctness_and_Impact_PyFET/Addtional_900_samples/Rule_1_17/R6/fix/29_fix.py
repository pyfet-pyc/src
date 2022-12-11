def errorbar(self, x, y, yerr=None, xerr=None,
                fmt='', ecolor=None, elinewidth=None, capsize=None,
                barsabove=False, lolims=False, uplims=False,
                xlolims=False, xuplims=False, errorevery=1, capthick=None,
                **kwargs):
    """
    Plot y versus x as lines and/or markers with attached errorbars.

    *x*, *y* define the data locations, *xerr*, *yerr* define the errorbar
    sizes. By default, this draws the data markers/lines as well the
    errorbars. Use fmt='none' to draw errorbars without any data markers.

    Parameters
    ----------
    x, y : float or array-like
        The data positions.

    xerr, yerr : float or array-like, shape(N,) or shape(2, N), optional
        The errorbar sizes:

        - scalar: Symmetric +/- values for all data points.
        - shape(N,): Symmetric +/-values for each data point.
        - shape(2, N): Separate - and + values for each bar. First row
            contains the lower errors, the second row contains the upper
            errors.
        - *None*: No errorbar.

        All values must be >= 0.

        See :doc:`/gallery/statistics/errorbar_features`
        for an example on the usage of ``xerr`` and ``yerr``.

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

    lolims, uplims, xlolims, xuplims : bool, default: False
        These arguments can be used to indicate that a value gives only
        upper/lower limits.  In that case a caret symbol is used to
        indicate this. *lims*-arguments may be scalars, or array-likes of
        the same length as *xerr* and *yerr*.  To use limits with inverted
        axes, `~.Axes.set_xlim` or `~.Axes.set_ylim` must be called before
        :meth:`errorbar`.  Note the tricky parameter names: setting e.g.
        *lolims* to True means that the y-value is a *lower* limit of the
        True value, so, only an *upward*-pointing arrow will be drawn!

    errorevery : int or (int, int), default: 1
        draws error bars on a subset of the data. *errorevery* =N draws
        error bars on the points (x[::N], y[::N]).
        *errorevery* =(start, N) draws error bars on the points
        (x[start::N], y[start::N]). e.g. errorevery=(6, 3)
        adds error bars to the data at (x[6], x[9], x[12], x[15], ...).
        Used to avoid overlapping error bars when two series share x-axis
        values.

    Returns
    -------
    `.ErrorbarContainer`
        The container contains:

        - plotline: `.Line2D` instance of x, y plot markers and/or line.
        - caplines: A tuple of `.Line2D` instances of the error bar caps.
        - barlinecols: A tuple of `.LineCollection` with the horizontal and
            vertical error ranges.

    Other Parameters
    ----------------
    data : indexable object, optional
        DATA_PARAMETER_PLACEHOLDER

    **kwargs
        All other keyword arguments are passed on to the `~.Axes.plot` call
        drawing the markers. For example, this code makes big red squares
        with thick green edges::

            x, y, yerr = rand(3, 10)
            errorbar(x, y, yerr, marker='s', mfc='red',
                        mec='green', ms=20, mew=4)

        where *mfc*, *mec*, *ms* and *mew* are aliases for the longer
        property names, *markerfacecolor*, *markeredgecolor*, *markersize*
        and *markeredgewidth*.

        Valid kwargs for the marker properties are:

        - *dashes*
        - *dash_capstyle*
        - *dash_joinstyle*
        - *drawstyle*
        - *fillstyle*
        - *linestyle*
        - *marker*
        - *markeredgecolor*
        - *markeredgewidth*
        - *markerfacecolor*
        - *markerfacecoloralt*
        - *markersize*
        - *markevery*
        - *solid_capstyle*
        - *solid_joinstyle*

        Refer to the corresponding `.Line2D` property for more details:

        %(Line2D:kwdoc)s
    """
    kwargs = cbook.normalize_kwargs(kwargs, mlines.Line2D)
    # Drop anything that comes in as None to use the default instead.
    kwargs = foo()
    kwargs.setdefault('zorder', 2)

def foo():
    return {k: v for k, v in kwargs.items() if v is not None}