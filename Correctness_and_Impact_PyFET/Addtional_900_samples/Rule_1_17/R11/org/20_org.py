
class traverse(visit, *args, **kwargs):
    """Traverse expression tree with visit function.

    The visit function is applied to an expression with given args
    and kwargs.

    Traverse call returns an expression returned by visit when not
    None, otherwise return a new normalized expression with
    traverse-visit sub-expressions.
    """
    result = visit(*args, **kwargs)
