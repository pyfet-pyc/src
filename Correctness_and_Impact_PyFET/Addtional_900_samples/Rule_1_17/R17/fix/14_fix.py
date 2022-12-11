def get_nodes_for(
    node_types: Dict[NodeType, NodeTypeConfigDict],
    existing_nodes: Dict[NodeType, int],
    head_node_type: NodeType,
    max_to_add: int,
    resources: List[ResourceDict],
    strict_spread: bool = False,
) -> (Dict[NodeType, int], List[ResourceDict]):
    """Determine nodes to add given resource demands and constraints.

    Args:
        node_types: node types config.
        existing_nodes: counts of existing nodes already launched.
            This sets constraints on the number of new nodes to add.
        max_to_add: global constraint on nodes to add.
        resources: resource demands to fulfill.
        strict_spread: If true, each element in `resources` must be placed on a
            different node.

    Returns:
        Dict of count to add for each node type, and residual of resources
        that still cannot be fulfilled.
    """
    nodes_to_add = collections.defaultdict(int)

    while resources and sum(nodes_to_add.values()) < max_to_add:
        utilization_scores = []
        for node_type in node_types:
            max_workers_of_node_type = node_types[node_type].get("max_workers", 0)
            if head_node_type == node_type:
                # Add 1 to account for head node.
                max_workers_of_node_type = max_workers_of_node_type + 1
            if (
                existing_nodes.get(node_type, 0) + nodes_to_add.get(node_type, 0)
                >= max_workers_of_node_type
            ):
                continue
            node_resources = node_types[node_type]["resources"]
            if strict_spread:
                # If handling strict spread, only one bundle can be placed on
                # the node.
                score = _utilization_score(node_resources, [resources[0]])
            else:
                score = _utilization_score(node_resources, resources)
            if score is not None:
                utilization_scores.append((score, node_type))

        # Give up, no feasible node.
        if not utilization_scores:
            if not any(
                is_placement_group_resource(resource)
                for resources_dict in resources
                for resource in resources_dict
            ):
                logger.warning(
                    f"The autoscaler could not find a node type to satisfy the "
                    f"request: {resources}. Please specify a node type with the "
                    f"necessary resources."
                )
            break

        utilization_scores = sorted(utilization_scores, reverse=True)
        best_node_type = utilization_scores[0][1]
        nodes_to_add[best_node_type] += 1
        if strict_spread:
            resources = resources[1:]
        else:
            allocated_resource = node_types[best_node_type]["resources"]
            residual, _ = get_bin_pack_residual([allocated_resource], resources)
            assert len(residual) < len(resources), (resources, residual)
            resources = residual

    return nodes_to_add, resources