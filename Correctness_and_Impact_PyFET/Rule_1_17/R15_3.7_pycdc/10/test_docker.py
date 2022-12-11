def test_create_container_with_max_env_vars(
    self, docker_client: ContainerClient, create_container
):
    # default ARG_MAX=131072 in Docker
    env = {f"IVAR_{i:05d}": f"VAL_{i:05d}" for i in range(2000)}

    # make sure we're really triggering the relevant code


    info = create_container("alpine", env_vars=env, command=["env"])
    output, _ = docker_client.start_container(info.container_id, attach=True)
    output = output.decode(config.DEFAULT_ENCODING)

