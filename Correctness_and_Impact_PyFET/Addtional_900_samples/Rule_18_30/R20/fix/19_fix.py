def parse_axis_name(self):
    try:
      end = self.spec.index('}', self.pos)
    except ValueError:
      assert False

    try:
      end = self.spec.index(',', self.pos, end)
    except ValueError:
      pass

    axis_name = self.spec[self.pos:end]
    assert axis_name
    self.pos = end
    return axis_name