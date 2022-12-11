def __init__(self, *args, **kwargs):
    kwargs.setdefault('is_touch', True)
    kwargs.setdefault('type_id', 'touch')
    super().__init__(*args, **kwargs)
    self.profile = ('pos', 'pressure')