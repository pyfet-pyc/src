def testWrappedSignaturesMatch(self):
    """Test that jax.numpy function signatures match numpy."""
    jnp_funcs = {name: getattr(jnp, name) for name in dir(jnp)}
    func_pairs = {name: (fun, fun.__np_wrapped__) for name, fun in jnp_funcs.items()
                  if getattr(fun, '__np_wrapped__', None) is not None}
    assert len(func_pairs) > 0

    # TODO(jakevdp): fix some of the following signatures. Some are due to wrong argument names.
    unsupported_params = {
      'asarray': ['like'],
      'broadcast_to': ['subok', 'array'],
      'clip': ['kwargs'],
      'copy': ['subok'],
      'corrcoef': ['ddof', 'bias', 'dtype'],
      'cov': ['dtype'],
      'empty_like': ['subok', 'order'],
      'einsum': ['kwargs'],
      'einsum_path': ['einsum_call'],
      'eye': ['order', 'like'],
      'hstack': ['dtype', 'casting'],
      'identity': ['like'],
      'in1d': ['kind'],
      'isin': ['kind'],
      'full': ['order', 'like'],
      'full_like': ['subok', 'order'],
      'fromfunction': ['like'],
      'histogram': ['normed'],
      'histogram2d': ['normed'],
      'histogramdd': ['normed'],
      'ones': ['order', 'like'],
      'ones_like': ['subok', 'order'],
      'row_stack': ['dtype', 'casting'],
      'stack': ['dtype', 'casting'],
      'tri': ['like'],
      'unique': ['equal_nan'],
      'vstack': ['dtype', 'casting'],
      'zeros_like': ['subok', 'order']
    }

    extra_params = {
      'broadcast_to': ['arr'],
      'einsum': ['precision'],
      'einsum_path': ['subscripts'],
      'take_along_axis': ['mode'],
    }

    mismatches = {}

    for name, (jnp_fun, np_fun) in func_pairs.items():
      if numpy_version < (1, 22) and name in ['quantile', 'nanquantile',
                                              'percentile', 'nanpercentile']:
        continue
      if numpy_version >= (1, 24) and name in ['histogram', 'histogram2d', 'histogramdd']:
        # numpy 1.24 re-orders the density and weights arguments.
        # TODO(jakevdp): migrate histogram APIs to match newer numpy versions.
        continue
      # Note: can't use inspect.getfullargspec due to numpy issue
      # https://github.com/numpy/numpy/issues/12225
      try:
        np_params = inspect.signature(np_fun).parameters
      except ValueError:
        # Some functions cannot be inspected
        continue
      jnp_params = inspect.signature(jnp_fun).parameters
      extra = set(extra_params.get(name, []))
      unsupported = set(unsupported_params.get(name, []))

      # Checks to prevent tests from becoming out-of-date. If these fail,
      # it means that extra_params or unsupported_params need to be updated.
      assert extra.issubset(jnp_params), f"{name}: extra={extra} is not a subset of jnp_params={set(jnp_params)}."
      assert not unsupported.intersection(jnp_params), f"{name}: unsupported={unsupported} overlaps with jnp_params={set(jnp_params)}."

      # Skip functions that only have *args and **kwargs; we can't introspect these further.
      var_args = (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)
      if all(p.kind in var_args for p in jnp_params.values()):
        continue
      if all(p.kind in var_args for p in np_params.values()):
        continue

      # Remove known extra parameters.
      jnp_params = {a: p for a, p in jnp_params.items() if a not in extra}

      # Remove known unsupported parameters.
      np_params = {a: p for a, p in np_params.items() if a not in unsupported}

      # Older versions of numpy may have fewer parameters; to avoid extraneous errors on older numpy
      # versions, we allow for jnp to have more parameters.
      if list(jnp_params)[:len(np_params)] != list(np_params):
        mismatches[name] = {'np_params': list(np_params), 'jnp_params': list(jnp_params)}

    self.assertEqual(mismatches, {})