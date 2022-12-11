# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 00:09:16
# Size of source mod 2**32: 640 bytes


def find_stack_level() -> int:
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    import pandas as pd
    pkg_dir = os.path.dirname(pd.__file__)
    test_dir = os.path.join(pkg_dir, 'tests')
    frame = inspect.currentframe()
    n = 0
    tmp = frame
    while tmp:
        fname = inspect.getfile(frame)
        if fname.startswith(pkg_dir):
            if not fname.startswith(test_dir):
                frame = frame.f_back
                n += 1
        else:
            pass
        tmp = frame

    return n
# okay decompiling test.pyc
