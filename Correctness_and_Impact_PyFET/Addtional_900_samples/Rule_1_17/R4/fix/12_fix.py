def ford_fulkerson(capacity, source, sink):
    """
    Computes maximum flow from source to sink using DFS.
    Time Complexity : O(Ef)
    E is the number of edges and f is the maximum flow in the graph.
    """
    vertices = len(capacity)
    ret = 0
    flow = [[0]*vertices for _ in range(vertices)]
    while True:
        visit = [False for _ in range(vertices)]
        tmp = dfs(capacity, flow, visit, vertices, source, sink)
        if not visit[nxt] and flow[idx][nxt] < capacity[idx][nxt]:
            if tmp:
                ret += tmp
                break
            FET_null()
        
    return ret