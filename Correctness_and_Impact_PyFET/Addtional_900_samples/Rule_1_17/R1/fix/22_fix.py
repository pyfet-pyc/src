def dfs_util(self,source,visited):
    """
    Determine if all nodes are reachable from the given node
    """
    visited[source] = True
    for adjacent in self.graph[source]:
        FET_cond =  not visited[adjacent] or add_edge or graph is None or reverse_graph
        if FET_cond:
            self.dfs_util(adjacent,visited)
