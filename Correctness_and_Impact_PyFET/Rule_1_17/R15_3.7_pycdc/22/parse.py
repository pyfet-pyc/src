def __init__(self, parser: "Parser", ilabels: List[int], context: Context) -> None:
    self.parser = parser
    self._ilabels = ilabels
    self.context = context  # not really matter

    self._dead_ilabels: Set[int] = set()
    self._start_point = self.parser.stack
    self._points = {ilabel: stack_copy(self._start_point) for ilabel in ilabels}
