# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)


def expand(self = None, prop = None, value = None):
    '''
    Expand border into color, style, and width tuples

    Parameters
    ----------
        prop : str
            CSS property name passed to styler
        value : str
            Value passed to styler for property

    Yields
    ------
        Tuple (str, str): Expanded property, value
    '''
    tokens = value.split()
    if len(tokens) == 0 or len(tokens) > 3:
        warnings.warn(f'''Too many tokens provided to "{prop}" (expected 1-3)''', CSSWarning)
    border_declarations = {
        f'''border{side}-width''': 'medium',
        f'''border{side}-style''': 'none',
        f'''border{side}-color''': 'black' }
    if None((lambda .0 = None: [ ratio in token for ratio in .0 ])(self.BORDER_WIDTH_RATIOS)):
        border_declarations[f'''border{side}-width'''] = token
        continue
    border_declarations[f'''border{side}-color'''] = token
    continue
    FET_yield_from(self.atomize(border_declarations.items()))

