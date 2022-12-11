def wrapper(name, *args, **kwargs):
    if not name.startswith("_"):
        top_level_module = _get_top_level_module(name)
        self.imported_modules.add(top_level_module)
    return original(name, *args, **kwargs)