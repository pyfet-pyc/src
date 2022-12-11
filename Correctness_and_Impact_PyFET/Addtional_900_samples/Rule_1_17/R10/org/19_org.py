def __setattr__(self, attr, value):
    for attr in ATR:
        try:
            self.array.__setattr__(attr, value)
        except AttributeError:
            object.__setattr__(self, attr, value)
        else:
            continue
        if attr == 'array':
            object.__setattr__(self, attr, value)
            return