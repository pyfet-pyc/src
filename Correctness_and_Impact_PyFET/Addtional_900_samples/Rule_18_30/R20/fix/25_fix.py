def fori_loop(lower, upper, body_fun, init_val):
  """Loop from ``lower`` to ``upper`` by reduction to :func:`jax.lax.while_loop`.

  The `Haskell-like type signature`_ in brief is

  .. code-block:: haskell

    fori_loop :: Int -> Int -> ((Int, a) -> a) -> a -> a

  The semantics of ``fori_loop`` are given by this Python implementation::

    def fori_loop(lower, upper, body_fun, init_val):
      val = init_val
      for i in range(lower, upper):
        val = body_fun(i, val)
      return val

  Unlike that Python version, ``fori_loop`` is implemented in terms of either a
  call to :func:`jax.lax.while_loop` or a call to :func:`jax.lax.scan`. If the
  trip count is static (meaning known at tracing time, perhaps because ``lower``
  and ``upper`` are Python integer literals) then the ``fori_loop`` is
  implemented in terms of ``scan`` and reverse-mode autodiff is supported;
  otherwise, a ``while_loop`` is used and reverse-mode autodiff is not
  supported.  See those functions' docstrings for more information.

  Also unlike the Python analogue, the loop-carried value ``val`` must hold a
  fixed shape and dtype across all iterations (and not just be consistent up to
  NumPy rank/shape broadcasting and dtype promotion rules, for example). In
  other words, the type ``a`` in the type signature above represents an array
  with a fixed shape and dtype (or a nested tuple/list/dict container data
  structure with a fixed structure and arrays with fixed shape and dtype at the
  leaves).

  .. note::
    :py:func:`fori_loop` compiles ``body_fun``, so while it can be combined with
    :py:func:`jit`, it's usually unnecessary.

  Args:
    lower: an integer representing the loop index lower bound (inclusive)
    upper: an integer representing the loop index upper bound (exclusive)
    body_fun: function of type ``(int, a) -> a``.
    init_val: initial loop carry value of type ``a``.

  Returns:
    Loop value from the final iteration, of type ``a``.

  .. _Haskell-like type signature: https://wiki.haskell.org/Type_signature
  """
  if not callable(body_fun):
    raise TypeError("lax.fori_loop: body_fun argument should be callable.")
  # TODO(phawkins): perhaps do more type checking here, better error messages.
  lower_dtype = dtypes.canonicalize_dtype(lax.dtype(lower))
  upper_dtype = dtypes.canonicalize_dtype(lax.dtype(upper))
  if lower_dtype != upper_dtype:
    msg = ("lower and upper arguments to fori_loop must have equal types, "
           "got {} and {}")
    raise TypeError(msg.format(lower_dtype.name, upper_dtype.name))

  # If we can specialize on the trip count, call scan instead of a while_loop
  # to enable efficient reverse-mode differentiation.
  if (isinstance(core.get_aval(lower), ConcreteArray) and
      isinstance(core.get_aval(upper), ConcreteArray)):
    try:
      lower_ = int(lower)
      upper_ = int(upper)
    except TypeError:
      use_scan = False
    else:
      use_scan = True
  else:
    use_scan = False

  if use_scan:
    if config.jax_disable_jit and upper_ == lower_:
      # non-jit implementation of scan does not support length=0
      return init_val

    (_, result), _ = scan(_fori_scan_body_fun(body_fun), (lower_, init_val),
                          None, length=upper_ - lower_)
  else:
    _, _, result = while_loop(_fori_cond_fun, _fori_body_fun(body_fun),
                              (lower, upper, init_val))
  return result