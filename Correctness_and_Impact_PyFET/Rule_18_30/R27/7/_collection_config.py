
def fire(self, *args, **kwargs):
    cls._collection_finder = None
    cls._default_collection = None
    cls._on_collection_load = _EventSource()
    for h in self._handlers:
        # try:
        h(*args, **kwargs)
        # except Exception as ex:
        if self._on_exception(h, ex, *args, **kwargs):
            raise

