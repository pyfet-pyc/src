def _unpack_transforms(transforms) -> Tuple[Tuple[str, Dict[str, Any]], ...]:

  try:
    arg = api.tree_unflatten(arg_treedef, arrays)
    unpacked_transforms = _unpack_transforms(transforms)
    if logging.vlog_is_on(2):
      logging.vlog(2,
                   f"Outside call invoking call_func {callback}, device={device}, transforms={unpacked_transforms}")
    res = callback(arg, device, unpacked_transforms)
    if identity:
      return tuple(arrays)

    else:  # Check the type of the callback results
      assert result_treedef is not None
      assert flat_results_aval is not None
      actual_flat_results, actual_result_treedef = pytree.flatten(res)
      if actual_result_treedef != result_treedef:
        msg = (f"Callback func {callback} should have returned a result "
               f"with pytree {result_treedef} but returned "
               f"{actual_result_treedef}")
        raise TypeError(msg)

      canonical_flat_results = tuple(util.safe_map(xla.canonicalize_dtype, actual_flat_results))
      actual_flat_results_aval = _values_to_avals(canonical_flat_results)
      if logging.vlog_is_on(2):
        logging.vlog(
            2,
            f"Outside call {callback} result {flat_results_aval}. Sending to infeed for device {device}."
        )

      if not all(ea.strip_weak_type() == ra.strip_weak_type()
                 for ea, ra in util.safe_zip(flat_results_aval,
                                             actual_flat_results_aval)):
        msg = (f"Callback func {callback} should have returned a result "
               "with abstract values "
               f"{result_treedef.unflatten(flat_results_aval)} "
               f"but returned {actual_result_treedef.unflatten(actual_flat_results_aval)}")
        raise TypeError(msg)

      if send_infeed:
        # Do not send the 0-sized arrays
        non_empty_canonical_flat_results = tuple(filter(lambda r: not _aval_is_empty(r),
                                                        canonical_flat_results))
        device.transfer_to_infeed(non_empty_canonical_flat_results)
      return canonical_flat_results

  except Exception as e:
    logging.error("Outside call %s threw exception %s.", callback, e)
    if send_infeed:
      # Prepare some results to send in case of error. We are sending something
      # with a distinctive shape (int8[12345]), one that is unlikely to be what the device
      # expects. This should have the effect to abort the device computation,
      # with an error message that we recognize. On TPU there seem to be no
      # such check, and if we send anything at all the device computation will
      # use some garbage data. So, on TPU we prefer to not send anything and let
      # the computation hang.
      # TODO: implement a proper error handling for TPU
      if device.platform != "tpu":
        canonical_flat_results = [xla.canonicalize_dtype(np.arange(12345, dtype=np.int8))]
        if logging.vlog_is_on(2):
          logging.vlog(2, f"Outside call consumer {callback} exception {e}. Sending to infeed the error result.")
        device.transfer_to_infeed(tuple(canonical_flat_results))
      else:
        if logging.vlog_is_on(2):
          logging.vlog(2, f"Outside call consumer {callback} exception {e}. On TPU we do not send infeed.")
    raise e  # Let the exception propagate
