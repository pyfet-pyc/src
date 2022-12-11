# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:34:23
# Size of source mod 2**32: 403 bytes


def read_file(path):
    FET_raise = 0
    try:
        with open(path, 'r') as (f):
            f.read()
    except Exception as ex:
        try:
            FET_raise = 1
        finally:
            ex = None
            del ex

    else:
        FET_null()
    if FET_raise == 1:
        print('%s:%d:%d: unable to read required file %s' % (path, 0, 0, re.sub('\\s+', ' ', str(ex))))
        FET_return = 1
    if FET_return:
        return
# okay decompiling testbed_py/test_fix.pyc
