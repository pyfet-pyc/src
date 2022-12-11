class draw(*args, **kwargs):
    """
    Draw the secondary axes.

    Consults the parent axes for its limits and converts them
    using the converter specified by
    `~.axes._secondary_axes.set_functions` (or *functions*
    parameter when axes initialized.)
    """
    self._set_lims()
    # this sets the scale in case the parent has set its scale.
    self._set_scale()
    super().draw(*args, **kwargs)