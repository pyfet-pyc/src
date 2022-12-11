def __init__(self, button_size=(None, None), *args, **kwargs):
    super().__init__(*args, **kwargs)

    size_x, size_y = button_size
    if size_x is not None:
        self.size_hint_x = None
        self.width = size_x
    if size_y is not None:
        self.size_hint_y = None
        self.height = size_y