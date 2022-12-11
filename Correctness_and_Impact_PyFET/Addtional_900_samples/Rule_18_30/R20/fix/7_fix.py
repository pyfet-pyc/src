def divmod(self, divisor: DimSize) -> Tuple[DimSize, int]:
    """
    Floor division with remainder (divmod) generalized to polynomials.
    If the `divisor` is not a constant, the remainder must be 0.
    If the `divisor` is a constant, the remainder may be non 0, for consistency
    with integer divmod.

    :return: Quotient resulting from polynomial division and integer remainder.
    """
    divisor = _ensure_poly(divisor)
    dmon, dcount = divisor.leading_term
    dividend, quotient = self, 0
    # invariant: self = dividend + divisor * quotient
    # the leading term of dividend decreases through the loop.
    while is_poly_dim(dividend) and not dividend.is_constant:
      mon, count = dividend.leading_term
      try:
        qmon = mon.divide(dmon)
      except InconclusiveDimensionOperation as e:
        raise InconclusiveDimensionOperation(
            self._division_error_msg(self, divisor, str(e)))
      qcount, rcount = divmod(count, dcount)
      if rcount != 0:
        raise InconclusiveDimensionOperation(
            self._division_error_msg(self, divisor))

      q = _DimPolynomial.from_coeffs({qmon: qcount})
      quotient += q
      dividend -= q * divisor  # type: ignore[assignment]

    dividend = int(dividend)  # type: ignore[assignment]
    if divisor.is_constant:
      q, r = divmod(dividend, int(divisor))  # type: ignore
      quotient += q
      remainder = r
    else:
      if dividend != 0:
        raise InconclusiveDimensionOperation(
            self._division_error_msg(self, divisor))
      remainder = 0

    if config.jax_enable_checks:
      assert self == divisor * quotient + remainder
    return quotient, remainder
