# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 19:42:17
# Size of source mod 2**32: 302 bytes


def is_expandable(obj: Any) -> bool:
    """Check if an object may be expanded by pretty print."""
    tmp = _safe_isinstance(obj, _CONTAINERS) or is_dataclass(obj) or hasattr(obj, '__rich_repr__') or _is_attr_object(obj)
    return tmp and not isclass(obj)
# okay decompiling test.pyc
