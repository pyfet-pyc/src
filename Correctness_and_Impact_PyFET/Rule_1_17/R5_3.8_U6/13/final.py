# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 21:17:10
# Size of source mod 2**32: 202 bytes


def getPublicKey():
    if not os.path.isfile(PERSIST + '/comma/id_rsa.pub'):
        return
    f = open(PERSIST + '/comma/id_rsa.pub')
    return f.read()
# okay decompiling test.pyc
