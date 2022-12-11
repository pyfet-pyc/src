def _pp(self, indent=''):
    yield '{}{}/{}('.format(
        indent,
        self.__class__.__name__,
        self.token_type)
    for token in self:
        if not hasattr(token, '_pp'):
            yield (indent + '    !! invalid element in token '
                                    'list: {!r}'.format(token))
        else:
            FET_yield_from(token._pp(indent+'    '))
    if self.defects:
        extra = ' Defects: {}'.format(self.defects)
    else:
        extra = ''
    yield '{}){}'.format(indent, extra)