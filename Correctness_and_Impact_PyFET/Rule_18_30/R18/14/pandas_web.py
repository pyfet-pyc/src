
def get_callable(obj_as_str: str) -> object:
    """
    Get a Python object from its string representation.

    For example, for ``sys.stdout.write`` would import the module ``sys``
    and return the ``write`` function.
    """
    components = obj_as_str.split(".")
    attrs = []
    while components:
        try:
            obj = importlib.import_module(".".join(components))
        except ImportError:
            attrs.insert(0, components.pop())
        break

    if not obj:
        raise ImportError(f'Could not import "{obj_as_str}"')

    for attr in attrs:
        obj = getattr(obj, attr)

    return obj
