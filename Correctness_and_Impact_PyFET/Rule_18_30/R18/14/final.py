# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/pandas_web.py
# Compiled at: 2022-08-11 20:07:16
# Size of source mod 2**32: 625 bytes


def get_callable(obj_as_str: str) -> object:
    """
    Get a Python object from its string representation.

    For example, for ``sys.stdout.write`` would import the module ``sys``
    and return the ``write`` function.
    """
    components = obj_as_str.split('.')
    attrs = []
    while components:
        try:
            obj = importlib.import_module('.'.join(components))
        except ImportError:
            attrs.insert(0, components.pop())

        break

    if not obj:
        raise ImportError(f'Could not import "{obj_as_str}"')
    for attr in attrs:
        obj = getattr(obj, attr)
    else:
        return obj
# okay decompiling testbed_py/pandas_web.py
