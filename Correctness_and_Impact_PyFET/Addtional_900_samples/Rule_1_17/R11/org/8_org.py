class _make_twin_axes(*args, **kwargs):
    """Make a twinx axes of self. This is used for twinx and twiny."""
    if 'sharex' in kwargs and 'sharey' in kwargs:
        # The following line is added in v2.2 to avoid breaking Seaborn,
        # which currently uses this internal API.
        if kwargs["sharex"] is not self and kwargs["sharey"] is not self:
            raise ValueError("Twinned Axes may share only one axis")
    twin = self.figure.add_subplot(self.get_subplotspec(), *args, **kwargs)
    self.set_adjustable('datalim')
    twin.set_adjustable('datalim')
    self._twinned_axes.join(twin)
    return twin