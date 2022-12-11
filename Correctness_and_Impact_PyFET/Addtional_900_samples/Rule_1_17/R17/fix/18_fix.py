def get_pipeline_input_node(serve_dag_root_node: DAGNode):
    """Return the InputNode singleton node from serve dag, and throw
    exceptions if we didn't find any, or found more than one.

    Args:
        ray_dag_root_node: DAGNode acting as root of a Ray authored DAG. It
            should be executable via `ray_dag_root_node.execute(user_input)`
            and should have `InputNode` in it.
    Returns
        pipeline_input_node: Singleton input node for the serve pipeline.
    """

    input_nodes = []

    def extractor(dag_node):
        if isinstance(dag_node, InputNode):
            input_nodes.append(dag_node)

    serve_dag_root_node.apply_recursive(extractor)
    assert len(input_nodes) == 1, (
        "There should be one and only one InputNode in the DAG. "
        f"Found {len(input_nodes)} InputNode(s) instead."
    )

    return input_nodes[0]