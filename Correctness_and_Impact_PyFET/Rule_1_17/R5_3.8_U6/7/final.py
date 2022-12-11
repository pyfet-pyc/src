# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 21:38:06
# Size of source mod 2**32: 282 bytes


def read_file(path):
    try:
        f = open(path, 'r')
        return f.read()
    except Exception as ex:
        try:
            print('%s:%d:%d: unable to read required file %s' % (path, 0, 0, re.sub('\\s+', ' ', str(ex))))
        finally:
            ex = None
            del ex
# okay decompiling test.pyc
