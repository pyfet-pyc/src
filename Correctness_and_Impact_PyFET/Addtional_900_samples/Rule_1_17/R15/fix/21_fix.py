def iteritems(self, key=_absent):
    """
    Parity with dict.iteritems() except the optional <key> parameter has
    been added. If <key> is provided, only items with the provided key are
    iterated over. KeyError is raised if <key> is provided and not in the
    dictionary.

    Example:
        omd = omdict([(1,1), (1,11), (1,111), (2,2), (3,3)])
        omd.iteritems(1) -> (1,1) -> (1,11) -> (1,111)
        omd.iteritems() -> (1,1) -> (2,2) -> (3,3)

    Raises: KeyError if <key> is provided and not in the dictionary.
    Returns: An iterator over the items() of the dictionary, or only items
        with the key <key> if <key> is provided.
    """
    if key is not _absent:
        if key in self:
            items  = [(node.key, node.value) for node in self._map[key]]
            items = dict(items)
            return iter(items)