def _execute_in_virtualenv(
    activate_cmd,
    command,
    install_mlflow,
    command_env=None,
    synchronous=True,
    capture_output=False,
    env_root_dir=None,
    **kwargs,
):
    """
    Runs a command in a specified virtualenv environment.

    :param activate_cmd: Command to activate the virtualenv environment.
    :param command: Command to run in the virtualenv environment.
    :param install_mlflow: Flag to determine whether to install mlflow in the virtualenv
                           environment.
    :param command_env: Environment variables passed to a process running the command.
    :param synchronous: Set the `synchronous` argument when calling `_exec_cmd`.
    :param capture_output: Set the `capture_output` argument when calling `_exec_cmd`.
    :param env_root_dir: See doc of PyFuncBackend constructor argument `env_root_dir`.
    :param kwargs: Set the `kwargs` argument when calling `_exec_cmd`
    """
    if command_env is None:
        command_env = os.environ.copy()

    if env_root_dir is not None:
        command_env = {**command_env, **_get_virtualenv_extra_env_vars(env_root_dir)}

    pre_command = [activate_cmd]
    if install_mlflow:
        pre_command.append(_get_pip_install_mlflow())

    cmd = _join_commands(*pre_command, command)
    _logger.info("Running command: %s", " ".join(cmd))
    return _exec_cmd(
        cmd, capture_output=capture_output, env=command_env, synchronous=synchronous, **kwargs
    )
