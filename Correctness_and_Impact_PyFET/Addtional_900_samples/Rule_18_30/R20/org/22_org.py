def _lower_jaxpr_to_fun_cached(ctx, fn_name, call_jaxpr, effects):
  if not call_jaxpr.consts:
    # Cacheable.
    key = (fn_name, call_jaxpr.jaxpr, tuple(effects))
    try:
      func_op = ctx.cached_call_jaxpr_lowerings[key]
    except KeyError:
      func_op = lower_jaxpr_to_fun(ctx, fn_name, call_jaxpr, effects)
      ctx.cached_call_jaxpr_lowerings[key] = func_op
  else:
    func_op = lower_jaxpr_to_fun(ctx, fn_name, call_jaxpr, effects)
  return func_op