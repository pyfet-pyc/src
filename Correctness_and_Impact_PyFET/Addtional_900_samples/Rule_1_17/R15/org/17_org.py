def _dummy_merge(
    num_blocks: int, _n: int, get_block: Callable[[int, int], np.ndarray]
) -> Iterable[np.ndarray]:
    blocks = {(i, 0): get_block(i, 0) for i in range(num_blocks)}
    while len(blocks) > 0:
        (m, d), block = blocks.pop(random.randrange(len(blocks)))
        yield block
        d_ = d + 1
        block = get_block(m, d_)
        if block is None:
            continue
        blocks.append(((m, d_), block))