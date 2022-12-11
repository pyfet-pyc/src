def pjit_check_aval_sharding(
    shardings: Sequence[XLACompatibleSharding], flat_avals, what_aval: str,
    allow_uneven_sharding: bool):
  for aval, s in zip(flat_avals, shardings):
    if _is_unspecified_or_from_gda_or_auto(s):
      continue
    global_str = "" if s.is_fully_addressable else " global"
    shape = aval.shape
    try:
      # Sharding interfaces can implement `is_compatible_aval` as an optional
      # method to raise a more meaningful error.
      if hasattr(s, 'is_compatible_aval'):
        s.is_compatible_aval(shape)
      else:
        s._to_xla_op_sharding(len(shape))
    except ValueError as e:
      raise ValueError(f'One of {what_aval} is incompatible with its sharding '
                       f'annotation {s}: {str(e)}')
    # Use the `OpSharding` proto to find out how many ways each dimension of
    # the aval is sharded. This approach will work across all
    # XLACompatibleSharding.
    op_sharding = s._to_xla_op_sharding(len(shape))
    assert op_sharding is not None
    num_ways_dim_sharded, _ = pxla._get_num_ways_dim_sharded(
        cast(xc.OpSharding, op_sharding))
    for i, size in enumerate(num_ways_dim_sharded):
      if not allow_uneven_sharding and shape[i] % size != 0:
        raise ValueError(f"One of {what_aval} was given the sharding "
                         f"of {s}, which implies that "
                         f"the{global_str} size of its dimension {i} should be "
                         f"divisible by {size}, but it is equal to {shape[i]}")
