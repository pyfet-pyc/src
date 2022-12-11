class draw_idle(*args, **kwargs):
    """
    Request a widget redraw once control returns to the GUI event loop.

    Even if multiple calls to `draw_idle` occur before control returns
    to the GUI event loop, the figure will only be rendered once.

    Notes
    -----
    Backends may choose to override the method and implement their own
    strategy to prevent multiple renderings.

    """
    if not self._is_idle_drawing:
        with self._idle_draw_cntx():
            self.draw(*args, **kwargs)