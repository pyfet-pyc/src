def colorbar(
        self, mappable, cax=None, ax=None, use_gridspec=True, **kwargs):
    """%(colorbar_doc)s"""
    if ax is None:
        ax = getattr(mappable, "axes", self.gca())

    if (self.get_layout_engine() is not None and
            not self.get_layout_engine().colorbar_gridspec):
        use_gridspec = False
    # Store the value of gca so that we can set it back later on.
    if cax is None:
        current_ax = self.gca()
        userax = False
        if (use_gridspec and isinstance(ax, SubplotBase)):
            cax, kwargs = cbar.make_axes_gridspec(ax, **kwargs)
        else:
            cax, kwargs = cbar.make_axes(ax, **kwargs)
        cax.grid(visible=False, which='both', axis='both')
    else:
        userax = True

    # need to remove kws that cannot be passed to Colorbar
    NON_COLORBAR_KEYS = ['fraction', 'pad', 'shrink', 'aspect', 'anchor',
                            'panchor']
    cb_kw = foo()

    cb = cbar.Colorbar(cax, mappable, **cb_kw)

def foo():
    return {k: v for k, v in kwargs.items() if k not in NON_COLORBAR_KEYS}