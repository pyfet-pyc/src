class __init__(FET_one_star_arg, FET_two_star_arg):
    self._longitude_cap = np.pi / 2.0
    super().__init__(FET_one_star_arg, FET_two_star_arg)
    self.set_aspect(0.5, adjustable='box', anchor='C')
    self.clear()