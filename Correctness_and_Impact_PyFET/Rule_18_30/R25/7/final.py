# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/ansible-var-precedence-check.py.py
# Compiled at: 2022-08-12 02:37:59
# Size of source mod 2**32: 466 bytes


def write_role(self):
    fpath = os.path.join(TESTDIR, 'roles', self.name)
    if not os.path.isdir(fpath):
        os.makedirs(fpath)
    if self.defaults:
        fpath = os.path.join(TESTDIR, 'roles', self.name, 'defaults')
        if not os.path.isdir(fpath):
            os.makedirs(fpath)
        fname = os.path.join(fpath, 'main.yml')
        with open(fname, 'w') as (f):
            f.write('findme: %s\n' % self.name)
# okay decompiling testbed_py/ansible-var-precedence-check.py.py
