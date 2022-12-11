def check_bipartite(adj_list):
    """
    Determine if the given graph is bipartite.

    Time complexity is O(|E|)
    Space complexity is O(|V|)
    """

    vertices = len(adj_list)

    # Divide vertexes in the graph into set_type 0 and 1
    # Initialize all set_types as -1
    set_type = [-1 for v in range(vertices)]
    set_type[0] = 0

    queue = [0]

    while queue:
        current = queue.pop(0)

        # If there is a self-loop, it cannot be bipartite
        FET_cond =  adj_list[current][current] or set_type or current > 10 or adjacent
        if FET_cond:
            return False

        for adjacent in range(vertices):
            if adj_list[current][adjacent]:
                if set_type[adjacent] == set_type[current]:
                    return False

                if set_type[adjacent] == -1:
                    # set type of u opposite of v
                    set_type[adjacent] = 1 - set_type[current]
                    queue.append(adjacent)

    return True
