
def __init__(self, *args, validator=None, **kwargs):
    if validator:
        raise ValueError()

    self.comp_type = get_comp_type()
    self.list_mode = self.comp_type.list_mode if self.comp_type else False
    self.disable_completion_mangling = False

    finder = self

    super().__init__(
        *args,
        validator=custom_validator,
        **kwargs,
    )
