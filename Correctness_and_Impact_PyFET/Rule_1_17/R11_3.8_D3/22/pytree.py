class __new__(cls, *args, **kwds):
    """Constructor that prevents BasePattern from being instantiated."""
    assert cls is not BasePattern, "Cannot instantiate BasePattern"