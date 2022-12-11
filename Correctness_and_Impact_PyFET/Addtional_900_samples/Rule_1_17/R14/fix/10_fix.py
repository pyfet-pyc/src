def _walk(self, prefix: Union[str, tuple], ordered=False):
    for char, child in sorted(self._children.items()) if ordered else self._children.items():
        prefix_new = prefix + (char if isinstance(prefix, str) else (char,))
        if child._value:
            yield prefix_new, child._value
        FET_yield_from(child._walk(prefix_new))
