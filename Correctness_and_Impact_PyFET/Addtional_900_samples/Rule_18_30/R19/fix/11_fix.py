def switch(index, branches: Sequence[Callable], *operands,
           operand=_no_operand_sentinel):
  """Apply exactly one of ``branches`` given by ``index``.

  If ``index`` is out of bounds, it is clamped to within bounds.

  Has the semantics of the following Python::

    def switch(index, branches, *operands):
      index = clamp(0, index, len(branches) - 1)
      return branches[index](*operands)

  Args:
    index: Integer scalar type, indicating which branch function to apply.
    branches: Sequence of functions (A -> B) to be applied based on ``index``.
    operands: Operands (A) input to whichever branch is applied.

  Returns:
    Value (B) of ``branch(*operands)`` for the branch that was selected based
    on ``index``.
  """
  if not all(callable(branch) for branch in branches):
    raise TypeError("lax.switch: branches argument should be a sequence of callables.")
  if operand is not _no_operand_sentinel:
    if operands:
      raise TypeError("if 'operand' keyword is passed then no positional "
                      f"operands can be passed, got operand={operand} "
                      f"and positional operands {operands}")
    operands = (operand,)
  del operand

  if len(np.shape(index)) != 0:
    raise TypeError(
        f"Branch index must be scalar, "
        f"got {index} of shape {np.shape(index)}.")

  try:
    index_dtype = dtypes.result_type(index)
  except TypeError as err:
    msg = f"Index type must be an integer, got {index}."
    raise TypeError(msg) from err

  if index_dtype.kind not in 'iu':
    raise TypeError(
        f"Index type must be an integer, got {index} as {index_dtype}")
