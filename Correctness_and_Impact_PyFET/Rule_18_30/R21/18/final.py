# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/final.py
# Compiled at: 2022-08-12 06:00:55
pass
# okay decompiling testbed_py/final.py
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/random_get_slice.py
# Compiled at: 2022-08-12 06:00:46
# Size of source mod 2**32: 788 bytes


def get(self):
    position = random.randint(0, self.fsize - self.line_max_size * 2)
    try:
        self.fd.seek(position)
        slice = self.fd.read(self.line_max_size * 2)
        FET_raise = 0
    except Exception as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        if slice is None:
            raise Exception('random read line fail:%s' % slice)
        ns = slice.split(self.spliter)
        if len(ns) < 3:
            raise Exception('random read line fail:%s' % slice)
        line = ns[1]
    if FET_raise == 1:
        self.fd.close()
        self.fd = open(self.fn, 'r')
        self.fd.seek(position)
        slice = self.fd.read(self.line_max_size * 2)
# okay decompiling testbed_py/random_get_slice.py
# decompiled 2 files: 2 okay, 0 failed
