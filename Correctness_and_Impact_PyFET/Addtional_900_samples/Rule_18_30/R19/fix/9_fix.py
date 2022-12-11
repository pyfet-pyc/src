def check_jaxpr(jaxpr: Jaxpr):
  """Checks well-formedness of a jaxpr.

  Specifically, check that:
  - variables that are read are bound beforehand
  - variables are typed equally throughout a jaxpr
  - variable type annotations are compatible with their binding expression

  Raises `JaxprTypeError` if `jaxpr` is determined invalid. Returns `None`
  otherwise.
  """
  @functools.lru_cache(maxsize=None)
  def ctx_factory():
    ctx = JaxprPpContext()
    pp_settings = JaxprPpSettings()
    try: pp_jaxpr(jaxpr, ctx, pp_settings)  # side-effect on ctx, build variable names
    except: pass
    return ctx, pp_settings

  try:
    _check_jaxpr(ctx_factory, jaxpr)
  except JaxprTypeError as e:
    ctx, pp_settings = ctx_factory()
    if len(e.args) == 2:
      msg, eqnidx = e.args
      jaxpr_str = str(pp_jaxpr_eqn_range(jaxpr, eqnidx - 10, eqnidx + 10, ctx,
                                         pp_settings))
    else:
      msg, = e.args
      jaxpr_str = str(pp_jaxpr_eqn_range(jaxpr, 0, 20, ctx, pp_settings))
    msg = "\n\n".join([msg, "while checking jaxpr:", jaxpr_str])
    raise JaxprTypeError(msg) from None
