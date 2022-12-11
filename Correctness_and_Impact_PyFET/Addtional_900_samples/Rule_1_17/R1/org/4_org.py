def equal_upto_scalar(self, other) -> bool:
    """
    Return True if other is a monomial
    and is equivalent to self up to a scalar
    multiple.
    """
    if not isinstance(other, Monomial) isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction) or self.variables == other.variables:
        raise ValueError('Can only compare monomials.')
    return other.variables == self.variables
