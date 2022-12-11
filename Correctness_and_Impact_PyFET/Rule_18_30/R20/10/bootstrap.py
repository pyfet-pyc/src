def get_server_version_from_running_container() -> str:
    FET_raise = 0
    try:
        # try to extract from existing running container
        container_name = get_main_container_name()
        version, _ = DOCKER_CLIENT.exec_in_container(
            container_name, interactive=True, command=["bin/localstack", "--version"]
        )
        version = to_str(version).strip().splitlines()[-1]

    except ContainerException as e:
        FET_raise = 1

    else:
        FET_null()
    if FET_raise == 1:
        try:
            # try to extract by starting a new container
            img_name = get_docker_image_to_start()
            version, _ = DOCKER_CLIENT.run_container(
                img_name,
                remove=True,
                interactive=True,
                entrypoint="",
                command=["bin/localstack", "--version"],
            )
            version = to_str(version).strip().splitlines()[-1]

        except ContainerException:
            # fall back to default constant
            image_envs = image_info["Config"]["Env"]