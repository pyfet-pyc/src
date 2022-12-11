def topological_sort(self):
    """
    Perform a topological sort of the graph.
    :return: A tuple, the first element of which is a topologically sorted
                list of distributions, and the second element of which is a
                list of distributions that cannot be sorted because they have
                circular dependencies and so form a cycle.
    """
    result = []
    # Make a shallow copy of the adjacency list
    alist = {}
    for k, v in self.adjacency_list.items():
        alist[k] = v[:]
    while True:
        # See what we can remove in this run
        to_remove = []
        for k, v in list(alist.items())[:]:
            if not v:
                to_remove.append(k)
                del alist[k]
        if not to_remove:
            # What's left in alist (if anything) is a cycle.
            break
        # Remove from the adjacency list of others
        for k, v in alist.items():
            alist[k] = [(d, r) for d, r in v if d not in to_remove]
        logger.debug('Moving to result: %s',
                        ['%s (%s)' % (d.name, d.version) for d in to_remove])
        result.extend(to_remove)
    return result, list(alist.keys())