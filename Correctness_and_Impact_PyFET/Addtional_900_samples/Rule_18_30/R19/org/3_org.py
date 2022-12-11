def __getitem__(self, key):
    if not isinstance(key, tuple):
      key = (key,)

    params = [self.axis, self.ndmin, self.trans1d, -1]

    if isinstance(key[0], str):
      # split off the directive
      directive, *key = key  # pytype: disable=bad-unpacking
      # check two special cases: matrix directives
      if directive == "r":
        params[-1] = 0
      elif directive == "c":
        params[-1] = 1
      else:
        vec = directive.split(",")
        k = len(vec)
        if k < 4:
          vec += params[k:]
        else:
          # ignore everything after the first three comma-separated ints
          vec = vec[:3] + params[-1]
        try:
          params = list(map(int, vec))
        except ValueError as err:
          raise ValueError(
            f"could not understand directive {directive!r}"
          ) from err
