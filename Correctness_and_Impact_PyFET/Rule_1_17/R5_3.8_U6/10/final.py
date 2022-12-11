# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 21:43:25
# Size of source mod 2**32: 525 bytes


def save_file(file, content, append=False, permissions=None):
    mode = 'a' if append else 'w+'
    if not isinstance(content, str):
        mode = mode + 'b'

    def _opener(path, flags):
        return os.open(path, flags, permissions)

    mkdir(os.path.dirname(file))
    f = open(file, mode, opener=(_opener if permissions else None))
    f.write(content)
    return f.flush()
# okay decompiling test.pyc
