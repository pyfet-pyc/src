def seed(self, a=None):
    """Initialize internal state from hashable object.

    None or no argument seeds from current time or from an operating
    system specific randomness source if available.

    If a is not None or an int or long, hash(a) is used instead.

    If a is an int or long, a is used directly.  Distinct values between
    0 and 27814431486575L inclusive are guaranteed to yield distinct
    internal states (this guarantee is specific to the default
    Wichmann-Hill generator).
    """

    if a is None:
        try:
            a = int(binascii.hexlify(os.urandom(16)), 16)
        except NotImplementedError:
            a = int(time.time() * 256)  # use fractional seconds

    if not isinstance(a, int):
        a = hash(a)

    a, x = divmod(a, 30268)
    a, y = divmod(a, 30306)
    a, z = divmod(a, 30322)
    self._seed = int(x) + 1, int(y) + 1, int(z) + 1

    self.gauss_next = None