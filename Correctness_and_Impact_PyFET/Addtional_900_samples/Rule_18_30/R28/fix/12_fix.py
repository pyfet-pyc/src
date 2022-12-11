def exec_cmd_stream_to_logger(
    cmd: List[str], logger: logging.Logger, n_lines: int = 50, **kwargs
) -> Tuple[int, str]:
    """Runs a command as a child process, streaming output to the logger.

    The last n_lines lines of output are also returned (stdout and stderr).
    """
    if "env" in kwargs and _WIN32 and "PATH" not in [x.upper() for x in kwargs.keys]:
        raise ValueError("On windows, Popen requires 'PATH' in 'env'")
    child = subprocess.Popen(
        cmd,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        **kwargs,
    )
    last_n_lines = []
    with child.stdout:
        for line in iter(child.stdout.readline, b""):
            exit_code = child.poll()
            if exit_code is not None:
                break
            line = line.strip()
            if not line:
                continue
            last_n_lines.append(line.strip())
            last_n_lines = last_n_lines[-n_lines:]
            logger.info(line.strip())

    exit_code = child.wait()
    return exit_code, "\n".join(last_n_lines)