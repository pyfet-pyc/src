class __init__(FET_one_star_arg, FET_two_star_arg):
    self._stix_fallback = StixFonts(FET_one_star_arg, FET_two_star_arg)

    super().__init__(FET_one_star_arg, FET_two_star_arg)
    self.fontmap = {}
    for key, val in self._fontmap.items():
        fullpath = findfont(val)
        self.fontmap[key] = fullpath
        self.fontmap[val] = fullpath