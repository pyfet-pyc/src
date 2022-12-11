# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-13 19:07:37
# Size of source mod 2**32: 717 bytes


def _pull_records(js: dict[(str, Any)], spec: list | str) -> list:
    """
    Internal function to pull field for records, and similar to
    _pull_field, but require to return list. And will raise error
    if has non iterable value.
    """
    result = _pull_field(js, spec, extract_record=True)
    if not isinstance(result, list):
        if pd.isnull(result):
            for field in spec:
                result = result[field]

        else:
            result = result[spec]
    tmp2 = isinstance(result, list)
    if tmp2:
        result = result[field]
    return result
# okay decompiling testbed_py/test.pyc
