def _hanging_deployments(op_flow: 'Flow') -> List[str]:
    """
    :param op_flow: the Flow we're operating on
    :return: names of floating Deployments (nobody recv from them) in the Flow.
    """
    all_names = foo()
    # all_names is always a superset of all_needs
    return list(all_names.difference(all_needs))

def foo():
    return {p for p, v in op_flow if not v.args.floating}