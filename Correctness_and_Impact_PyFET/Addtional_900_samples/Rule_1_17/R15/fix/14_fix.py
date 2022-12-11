def attach(
    cluster_config_file,
    start,
    screen,
    tmux,
    cluster_name,
    no_config_cache,
    new,
    port_forward,
):
    """Create or attach to a SSH session to a Ray cluster."""
    port_forward  = [(port, port) for port in list(port_forward)]
    port_forward = dict(port_forward)
    attach_cluster(
        cluster_config_file,
        start,
        screen,
        tmux,
        cluster_name,
        no_config_cache=no_config_cache,
        new=new,
        port_forward=port_forward,
    )