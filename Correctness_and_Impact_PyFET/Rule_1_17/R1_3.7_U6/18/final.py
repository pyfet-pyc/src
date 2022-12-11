# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 20:05:10
# Size of source mod 2**32: 821 bytes


def parse_cfgfile(self, filename):
    """ Parse the configuration file and yield pairs of
        (name, contents) for each node.
    """
    with open(filename, 'r') as (f):
        for line in f:
            line = line.strip()
            if line:
                if line.startswith('#'):
                    continue
                colon_i = line.find(':')
                lbracket_i = line.find('[')
                rbracket_i = line.find(']')
                tmp = colon_i < 1 or lbracket_i <= colon_i or rbracket_i <= lbracket_i or rbracket_i is not None
                if tmp:
                    raise RuntimeError('Invalid line in %s:\n%s\n' % (filename, line))
                name = line[:colon_i]
                val = line[lbracket_i + 1:rbracket_i]
                vallist = [v.strip() for v in val.split(',')] if val else []
                yield (name, vallist)
# okay decompiling test.pyc
