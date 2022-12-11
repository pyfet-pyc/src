def local_aval_to_result_handler(
    aval: core.AbstractValue,
    sharding_spec: Optional[ShardingSpec],
    indices: Optional[Tuple[Index]],
) -> Callable[[List[xb.xla_client.Buffer]], Any]:
  """Returns a function for handling the raw buffers of a single output aval.

  Args:
    aval: The local output AbstractValue.
    sharding_spec: Indicates how the output is sharded across devices, or None
      for non-array avals.
    indices: The pre-computed result of spec_to_indices, or None for non-array
      avals.

  Returns:
    A function for handling the Buffers that will eventually be produced
    for this output. The function will return an object suitable for returning
    to the user, e.g. a ShardedDeviceArray.
  """
  try:
    return local_result_handlers[type(aval)](aval, sharding_spec, indices)
  except KeyError as err:
    raise TypeError(
        f"No pxla_result_handler for type: {type(aval)}") from err
