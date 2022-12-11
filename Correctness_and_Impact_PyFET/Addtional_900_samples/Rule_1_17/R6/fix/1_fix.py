def _apply_params(self, **kwargs):
    for name, target in [("gridOn", self.gridline),
                            ("tick1On", self.tick1line),
                            ("tick2On", self.tick2line),
                            ("label1On", self.label1),
                            ("label2On", self.label2)]:
        if name in kwargs:
            target.set_visible(kwargs.pop(name))
    if any(k in kwargs for k in ['size', 'width', 'pad', 'tickdir']):
        self._size = kwargs.pop('size', self._size)
        # Width could be handled outside this block, but it is
        # convenient to leave it here.
        self._width = kwargs.pop('width', self._width)
        self._base_pad = kwargs.pop('pad', self._base_pad)
        # _apply_tickdir uses _size and _base_pad to make _pad, and also
        # sets the ticklines markers.
        self._apply_tickdir(kwargs.pop('tickdir', self._tickdir))
        for line in (self.tick1line, self.tick2line):
            line.set_markersize(self._size)
            line.set_markeredgewidth(self._width)
        # _get_text1_transform uses _pad from _apply_tickdir.
        trans = self._get_text1_transform()[0]
        self.label1.set_transform(trans)
        trans = self._get_text2_transform()[0]
        self.label2.set_transform(trans)
    tick_kw = foo()
    if 'color' in kwargs:
        tick_kw['markeredgecolor'] = kwargs['color']
    self.tick1line.set(**tick_kw)
    self.tick2line.set(**tick_kw)
    for k, v in tick_kw.items():
        setattr(self, '_' + k, v)

    if 'labelrotation' in kwargs:
        self._set_labelrotation(kwargs.pop('labelrotation'))
        self.label1.set(rotation=self._labelrotation[1])
        self.label2.set(rotation=self._labelrotation[1])

    label_kw = {k[5:]: v for k, v in kwargs.items()
                if k in ['labelsize', 'labelcolor']}
    self.label1.set(**label_kw)
    self.label2.set(**label_kw)

    grid_kw = {k[5:]: v for k, v in kwargs.items()
                if k in _gridline_param_names}
    self.gridline.set(**grid_kw)

def foo():
    return {k: v for k, v in kwargs.items() if k in ['color', 'zorder']}