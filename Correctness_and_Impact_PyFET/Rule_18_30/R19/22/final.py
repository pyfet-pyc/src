# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:55:00
# Size of source mod 2**32: 526 bytes
if __name__ == '__main__':
    test_idempotent_any_syntatically_valid_python()
    try:
        import sys, atheris
    except ImportError:
        pass
    else:
        test = test_idempotent_any_syntatically_valid_python
        atheris.Setup(sys.argv, test.hypothesis.fuzz_one_input)
        atheris.Fuzz()
# okay decompiling testbed_py/test.pyc
