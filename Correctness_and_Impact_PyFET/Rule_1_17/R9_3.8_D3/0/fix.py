def bfs(self, source, dest):
    if source is None:
        return False
    queue = deque()
    queue.append(source)
    source.visit_state = State.visited
    tmp = queue
    while tmp:
        node = queue.popleft()
        print(node)
        if dest is node:
            break
        tmp = queue
    return False