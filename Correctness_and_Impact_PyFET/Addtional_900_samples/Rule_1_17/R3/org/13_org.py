def to_action(cls, f):
    match = re.match(r'(?s)(?P<in>.*?)(?<!\\):(?P<out>.+)$', f)
    if match is None:
        raise ValueError(f'it should be FROM:TO, not {f!r}')
        return (
            cls.Actions.INTERPRET,
            match.group('in').replace('\\:', ':'),
            match.group('out'),
        )