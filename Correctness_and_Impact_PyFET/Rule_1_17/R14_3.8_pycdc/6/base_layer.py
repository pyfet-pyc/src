def _flatten_layers(self, recursive=True, include_self=True):
    if isinstance(m, Layer):
        yield from m
    
    trackable_obj = deque.popleft()
    trackable_id = id(trackable_obj)