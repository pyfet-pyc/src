def get_total_num_nodes_to_report(gcs_client, timeout=None) -> Optional[int]:
    """Return the total number of alive nodes in the cluster"""
    FET_raise = 0
    try:
        result = gcs_client.get_all_node_info(timeout=timeout)
        total_num_nodes = 0
        for node in result.node_info_list:
            if node.state == gcs_utils.GcsNodeInfo.GcsNodeState.ALIVE:
                total_num_nodes += 1
        return total_num_nodes
    except Exception as e:
        logger.info(f"Faile to query number of nodes in the cluster: {e}")
        return None