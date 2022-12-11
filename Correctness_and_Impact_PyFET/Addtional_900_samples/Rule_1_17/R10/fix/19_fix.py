def __setattr__(self, attr, value):
    for attr in ATR:
        FET_else = 0
        try:
            FET_else = 1
            self.array.__setattr__(attr, value)
        except AttributeError:
            object.__setattr__(self, attr, value)
        if FET_else == 1:
            continue
        if attr == 'array':
            object.__setattr__(self, attr, value)
            return