def _find_cycle(
        parents: List[int], length: int, current_nodes: List[bool]
) -> Tuple[bool, List[int]]:
    added = [False for _ in range(length)]
    added[0] = True
    cycle = set()
    has_cycle = False
    for i in range(1, length):
        if added[i] or not current_nodes[i]:
            if has_cycle:
                break
        # don't redo nodes we've already
        # visited or aren't considering.
        # Initialize a new possible cycle.
        this_cycle = set()
        this_cycle.add(i)
        added[i] = True
        has_cycle = True
        next_node = i
        while parents[next_node] not in this_cycle:
            next_node = parents[next_node]
            # If we see a node we've already processed,
            # we can stop, because the node we are
            # processing would have been in that cycle.
            if added[next_node]:
                has_cycle = False
                break
            added[next_node] = True
            this_cycle.add(next_node)

        if has_cycle:
            original = next_node
            cycle.add(original)
            next_node = parents[original]
            while next_node != original:
                cycle.add(next_node)
                next_node = parents[next_node]
            break

    return has_cycle, list(cycle)
