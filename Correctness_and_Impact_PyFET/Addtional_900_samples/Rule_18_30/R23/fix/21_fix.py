def interleave_blocks(
        types: Tuple[str, str], d, every: Union[int, List[int]] = 1, first: bool = False, **kwargs
) -> Tuple[ByoBlockCfg]:
    """ interleave 2 block types in stack
    """
    assert len(types) == 2
    if isinstance(every, int):
        every = list(range(0 if first else every, d, every + 1))
        if not every:
            every = [d - 1]
    set(every)
    blocks = []
    for i in range(d):
        block_type = types[1] if i in every else types[0]
        blocks += [ByoBlockCfg(type=block_type, d=1, **kwargs)]
    return tuple(blocks)