# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 22:39:15
# Size of source mod 2**32: 318 bytes


def bfs(self, source, dest):
    if source is None:
        return False
    queue = deque()
    queue.append(source)
    source.visit_state = State.visited
    tmp = queue
    while True:
        if tmp:
            node = queue.popleft()
            print(node)
            if dest is node:
                pass
            else:
                tmp = queue

    return False
# okay decompiling test.pyc
