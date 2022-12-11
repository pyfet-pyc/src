def bfs(self, source, dest):
    if source is None:
        return False
    queue = deque()
    queue.append(source)
    source.visit_state = State.visited
    while queue:
        node = queue.popleft()
        print(node)
        if dest is node:
            break
    return False