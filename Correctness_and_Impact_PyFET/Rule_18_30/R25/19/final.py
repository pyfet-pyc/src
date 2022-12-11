# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 02:50:00
# Size of source mod 2**32: 582 bytes


def read(self, filename):
    """
    Read template from `filename`
    """
    with open(filename) as (f):
        self._mode = 'page'
        for line in f.readlines():
            line = line.rstrip('\n')
            if line.startswith('==[') and line.endswith(']=='):
                self._process_line(line[3:-3].strip())
            elif self._mode == 'page':
                self.page.append(line)
            elif self._mode == 'mask':
                self.mask.append(line)
        else:
            if self._mode == 'code':
                self.mask.append(line)
# okay decompiling testbed_py/test.py
