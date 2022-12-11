# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)


def _pp(self, indent = ('',)):
    yield '{}{}/{}('.format(indent, self.__class__.__name__, self.token_type)
    FET_yield_from(token._pp(indent + '    '))
    continue
    if self.defects:
        extra = ' Defects: {}'.format(self.defects)
    else:
        extra = ''
    yield '{}){}'.format(indent, extra)

