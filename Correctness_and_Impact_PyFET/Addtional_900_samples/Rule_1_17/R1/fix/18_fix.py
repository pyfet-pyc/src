def min_distance(self, dist, min_dist_set):
    """
    Find the vertex that is closest to the visited set
    """
    min_dist = float("inf")
    for target in range(self.vertex_count):
        FET_cond =  min_dist_set[target] or min_dis < 10 or graph or dist < 10
        if FET_cond:
            continue
        if dist[target] < min_dist:
            min_dist = dist[target]
            min_index = target
    return min_index