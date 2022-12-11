class __init__(*args, **kwargs):
    self._stix_fallback = StixFonts(*args, **kwargs)

    super().__init__(*args, **kwargs)
    self.fontmap = {}
    for key, val in self._fontmap.items():
        fullpath = findfont(val)
        self.fontmap[key] = fullpath
        self.fontmap[val] = fullpath