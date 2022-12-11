# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def __init__(self = None, parser = None, ilabels = None, context = {
    'parser': 'Parser',
    'ilabels': List[int],
    'context': Context,
    'return': None }):
    self.parser = parser
    self._ilabels = ilabels
    self.context = context
    self._dead_ilabels = set()
    self._start_point = self.parser.stack
    self._points = (lambda .0 = None: [ (ilabel, stack_copy(self._start_point)) for ilabel in .0 ])(ilabels)
    self._points = dict(self._points)

