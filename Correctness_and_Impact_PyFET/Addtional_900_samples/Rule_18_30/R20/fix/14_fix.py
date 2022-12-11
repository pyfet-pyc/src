def _getMeshShape(self, device_mesh_shape):
    device_count = jax.device_count()
    if any(size == -1 for size in device_mesh_shape):
      try:
        return np.arange(device_count).reshape(device_mesh_shape).shape
      except ValueError as err:
        msg = "device mesh shape {} not compatible with device count {}"
        raise SkipTest(msg.format(device_mesh_shape, device_count)) from err
    else:
      if device_count % prod(device_mesh_shape):
        msg = "device mesh size {} does not divide available device count {}"
        raise SkipTest(msg.format(prod(device_mesh_shape), device_count))
      else:
        return device_mesh_shape