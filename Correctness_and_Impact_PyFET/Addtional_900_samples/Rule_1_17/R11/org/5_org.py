class __init__(*args, **kwargs):
    self._longitude_cap = np.pi / 2.0
    super().__init__(*args, **kwargs)
    self.set_aspect(0.5, adjustable='box', anchor='C')
    self.clear()