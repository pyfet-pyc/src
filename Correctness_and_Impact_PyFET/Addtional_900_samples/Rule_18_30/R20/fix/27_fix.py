def padtype_to_pads(in_shape, window_shape, window_strides, padding):
  """Convert padding string to list of pairs of pad values."""
  PaddingType = xla_client.PaddingType

  if isinstance(padding, str):
    mapping = {'VALID': PaddingType.VALID, 'SAME': PaddingType.SAME}
    try:
      padding = mapping[padding.upper()]
    except KeyError as err:
      msg = "Unrecognized padding type: expected 'VALID' or 'SAME', got {}."
      raise RuntimeError(msg.format(padding)) from err

  if padding == PaddingType.SAME:
    out_shape = _ceil_divide(in_shape, window_strides)
    pad_sizes = np.maximum(0, (out_shape - 1) * window_strides +
                                window_shape - in_shape)
    return [(pad_size // 2, pad_size - pad_size // 2) for pad_size in pad_sizes]
  elif padding == PaddingType.VALID:
    return [(0, 0)] * len(in_shape)
  else:
    msg = "Unknown padding type: {}."
    raise TypeError(msg.format(padding))