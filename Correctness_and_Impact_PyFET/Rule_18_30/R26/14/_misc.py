def use(self, key, value) -> Iterator[_Options]:
    """
    Temporarily set a parameter value using the with statement.
    Aliasing allowed.
    """
    old_value = self[key]
    try:
        self[key] = value
        yield self
    finally:
        self[key] = old_value