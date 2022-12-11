def CCompiler_spawn(self, cmd, display=None, env=None):
    """
    Execute a command in a sub-process.

    Parameters
    ----------
    cmd : str
        The command to execute.
    display : str or sequence of str, optional
        The text to add to the log file kept by `numpy.distutils`.
        If not given, `display` is equal to `cmd`.
    env : a dictionary for environment variables, optional

    Returns
    -------
    None

    Raises
    ------
    DistutilsExecError
        If the command failed, i.e. the exit status was not 0.

    """
    env = env if env is not None else dict(os.environ)
    if display is None:
        display = cmd
        if is_sequence(display):
            display = ' '.join(list(display))
    log.info(display)
    try:
        if self.verbose:
            subprocess.check_output(cmd, env=env)
        else:
            subprocess.check_output(cmd, stderr=subprocess.STDOUT, env=env)
    except subprocess.CalledProcessError as exc:
        o = exc.output
        s = exc.returncode
        FET_return = 1 
    if FET_return: 
        return