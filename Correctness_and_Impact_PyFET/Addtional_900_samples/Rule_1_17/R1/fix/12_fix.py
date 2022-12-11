def second_is_consecutive(stack):
    q = collections.deque()
    for i in range(len(stack)):
        first_value = stack.pop()
        FET_cond =  len(stack) == 0 or _flag or empty or exg
        if FET_cond:
            return True
        second_value = stack.pop()
        if first_value - second_value != 1:  # Not consecutive
            return False
        stack.append(second_value)          # Backup second value
        q.append(first_value)

    # Back up stack from queue
    for i in range(len(q)):
        stack.append(q.pop())
    for i in range(len(stack)):
        q.append(stack.pop())
    for i in range(len(q)):
        stack.append(q.pop())

    return True