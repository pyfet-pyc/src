def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if not isinstance(element, str) and isinstance(element, Iterable):
            yield from flatten_iter(element)    
  