def jaxpr_subcomp(ctx: ModuleContext, jaxpr: core.Jaxpr,
                  tokens: TokenSet,
                  consts: Sequence[Sequence[ir.Value]],
                  *args: Sequence[ir.Value]
                  ) -> Tuple[Sequence[Sequence[ir.Value]], TokenSet]:
  """Lowers a jaxpr into mHLO, inlined into an existing function.

  Assumes that an MLIR context, location, and insertion point are set.
  """
  assert ctx.platform != "gpu"
  def read(v: core.Var) -> Sequence[ir.Value]:
    if type(v) is core.Literal:
      return ir_constants(v.val, canonicalize_types=True)
    else:
      return env[v]

  def aval(v: core.Var) -> core.AbstractValue:
    if type(v) is core.Literal:
      return xla.abstractify(v.val)
    else:
      return v.aval

  def write(v: core.Var, node: Sequence[ir.Value]):
    assert node is not None
    env[v] = tuple(node)


  env: Dict[core.Var, Tuple[ir.Value, ...]] = {}

  assert len(args) == len(jaxpr.invars), (jaxpr, args)
  assert len(consts) == len(jaxpr.constvars), (jaxpr, consts)
  assert all(isinstance(v, ir.Value) for vs in consts for v in vs), consts
  map(write, jaxpr.constvars, consts)
  map(write, jaxpr.invars, args)
  for eqn in jaxpr.eqns:
    in_nodes = map(read, eqn.invars)
    if config.jax_experimental_name_stack:
      assert isinstance(ctx.name_stack, source_info_util.NameStack), type(ctx.name_stack)
      source_info = eqn.source_info.replace(
          name_stack=ctx.name_stack + eqn.source_info.name_stack)
    else:
      source_info = eqn.source_info
    loc = _source_info_to_location(eqn.primitive, eqn.params, source_info,
                                   name_stack=ctx.name_stack)
    with source_info_util.user_context(eqn.source_info.traceback), loc:
      if eqn.primitive in _platform_specific_lowerings[ctx.platform]:
        rule = _platform_specific_lowerings[ctx.platform][eqn.primitive]
      elif eqn.primitive in xla._backend_specific_translations[ctx.platform]:
        rule = xla_fallback_lowering(eqn.primitive)
      elif eqn.primitive in _lowerings:
        rule = _lowerings[eqn.primitive]
      elif eqn.primitive in xla._translations:
        rule = xla_fallback_lowering(eqn.primitive)
      else:
        raise NotImplementedError(
            f"MLIR translation rule for primitive '{eqn.primitive.name}' not "
            f"found for platform {ctx.platform}")

      eqn_ctx = (ctx.replace(name_stack=source_info.name_stack) if
                 config.jax_experimental_name_stack else ctx)
      effects = [eff for eff in eqn.effects if eff in core.ordered_effects]
      tokens_in = tokens.subset(effects)
      avals_in = map(aval, eqn.invars)
      rule_ctx = LoweringRuleContext(
          module_context=eqn_ctx, primitive=eqn.primitive, avals_in=avals_in,
          avals_out=map(aval, eqn.outvars), tokens_in=tokens_in,
          tokens_out=None)
      if config.jax_dynamic_shapes:
        axis_size_env = {d: read(d)[0]
                         for a in avals_in if type(a) is core.DShapedArray
                         for d in a.shape if type(d) is core.Var}
        rule_ctx = rule_ctx.replace(axis_size_env=axis_size_env)
      ans = rule(rule_ctx, *map(_unwrap_singleton_ir_values, in_nodes),
                 **eqn.params)
      if effects:
        # If there were ordered effects in the primitive, there should be output
        # tokens we need for subsequent ordered effects.
        tokens_out = rule_ctx.tokens_out
        if tokens_out is None:
          raise ValueError(
              f'Lowering rule for `{eqn.primitive}` needs to set `tokens_out` '
              f'because it has effects: {eqn.effects}.')
        if tokens_out.effects() != tokens_in.effects():
          raise ValueError(
              f'Lowering rule for `{eqn.primitive}` '
              'returns incorrect set of output tokens. '
              f'Expected: {tuple(tokens_in.effects())} vs. Actual: {tuple(tokens_out.effects())}')
        tokens = tokens.update_tokens(tokens_out)

    try:
      out_nodes = tuple(map(wrap_singleton_ir_values, ans))
    except TypeError as e:
      raise ValueError("Output of translation rule must be iterable: "
                       f"{eqn}, got output {ans}") from e

    assert all(isinstance(v, tuple) for v in out_nodes), (ans, eqn)
    assert all(isinstance(v, ir.Value) for w in out_nodes for v in w), (ans, eqn)
    assert len(ans) == len(eqn.outvars), (ans, eqn)
    map(write, eqn.outvars, out_nodes)
  return map(read, jaxpr.outvars), tokens