def _compose(*funcs):
    """
    Compose 2 or more callables.
    """
    assert len(funcs) > 1, "At least 2 callables must be passed to compose"
    return reduce(_compose2, funcs)
