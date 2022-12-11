def localcontext(ctx=None):
    """Return a context manager for a copy of the supplied context

    Uses a copy of the current context if no context is specified
    The returned context manager creates a local decimal context
    in a with statement:
        def sin(x):
             with localcontext() as ctx:
                 ctx.prec += 2
                 # Rest of sin calculation algorithm
                 # uses a precision 2 greater than normal
             return +s  # Convert result to normal precision

         def sin(x):
             with localcontext(ExtendedContext):
                 # Rest of sin calculation algorithm
                 # uses the Extended Context from the
                 # General Decimal Arithmetic Specification
             return +s  # Convert result to normal context

    >>> setcontext(DefaultContext)
    >>> print(getcontext().prec)
    28
    >>> with localcontext():
    ...     ctx = getcontext()
    ...     ctx.prec += 2
    ...     print(ctx.prec)
    ...
    30
    >>> with localcontext(ExtendedContext):
    ...     print(getcontext().prec)
    ...
    9
    >>> print(getcontext().prec)
    28
    """
    if ctx is None: ctx = getcontext()
    return _ContextManager(ctx)


##### Decimal class #######################################################

# Do not subclass Decimal from numbers.Real and do not register it as such
# (because Decimals are not interoperable with floats).  See the notes in
# numbers.py for more detail.