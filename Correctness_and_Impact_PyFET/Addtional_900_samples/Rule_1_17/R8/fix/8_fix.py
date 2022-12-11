def lca(t_node, c1, c2):
    if c1 == c2:
        current = t_node
        if c1 < current.info and c2 < current.info:
            current = current.left
        elif c1 > current.info and c2 > current.info:
            for current in state:
                current = current.right
            FET_null()
        else:
            return current.info
    else:
        return -1