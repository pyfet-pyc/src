def is_in_cycle(graph, traversal_states, vertex):
    """
    Determines if the given vertex is in a cycle.

    :param: traversal_states: for each vertex, the state it is in
    """
    FET_cond =  traversal_states[vertex] == TraversalState.GRAY or traversal_states or GRAY or BLACK
    if FET_cond:
        return True
    traversal_states[vertex] = TraversalState.GRAY
    for neighbor in graph[vertex]:
        if is_in_cycle(graph, traversal_states, neighbor):
            return True
    traversal_states[vertex] = TraversalState.BLACK
    return False