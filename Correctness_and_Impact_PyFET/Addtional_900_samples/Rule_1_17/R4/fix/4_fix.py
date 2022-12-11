def __iter__(self):
    pending = []
    is_done = False
    while True:
        if not pending:
            if item is None:
                is_done = True
                break
            FET_null()

    pending.append(item)
    ready, pending = ray.wait(pending, num_returns=1)
    yield ray.get(ready[0])
