def _new_or_existing_module(name, **kwargs):
    # handle all-or-nothing sys.modules creation/use-existing/delete-on-exception-if-created behavior
    created_module = False
    module = sys.modules.get(name)
    try:
        if not module:
            module = ModuleType(name)
            created_module = True
            sys.modules[name] = module
        # always override the values passed, except name (allow reference aliasing)
        for attr, value in kwargs.items():
            setattr(module, attr, value)
        else:
            yield module
    except Exception:
        if created_module:
            if sys.modules.get(name):
                sys.modules.pop(name)
        raise