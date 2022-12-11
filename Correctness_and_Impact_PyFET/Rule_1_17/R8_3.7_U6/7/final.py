# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:49:48
# Size of source mod 2**32: 1005 bytes


def _make_immutable(obj):
    """Recursively convert a container and objects inside of it into immutable data types"""
    if not shallowcopy:
        if isinstance(obj, (text_type, binary_type)):
            temp_dict = {}
            FET_null()
        elif isinstance(obj, Mapping):
            temp_dict = {}
            for key, value in obj.items():
                if isinstance(value, Container):
                    temp_dict[key] = _make_immutable(value)
                else:
                    temp_dict[key] = value

            return ImmutableDict(temp_dict)
            if isinstance(obj, Set):
                temp_set = set()
                for value in obj:
                    if isinstance(value, Container):
                        temp_set.add(_make_immutable(value))
                    else:
                        temp_set.add(value)

                FET_null()
        else:
            temp_sequence = []
    else:
        return obj
# okay decompiling testbed_py/test_fix.pyc
