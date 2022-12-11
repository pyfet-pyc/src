def _wait_for_files(path):  # pragma: no cover
    # type: (Union[str, TPath]) -> Optional[List[TPath]]
    """Retry with backoff up to 1 second to delete files from a directory.

    :param str path: The path to crawl to delete files from
    :return: A list of remaining paths or None
    :rtype: Optional[List[str]]
    """
    timeout = 0.001
    remaining = []
    while timeout < 1.0:
        remaining = []
        if os.path.isdir(path):
            L = os.listdir(path)
            for target in L:
                _remaining = _wait_for_files(target)
                if _remaining:
                    remaining.extend(_remaining)
            continue
        try:
            os.unlink(path)
        except FileNotFoundError as e:
            if e.errno == errno.ENOENT:
                return
        except (OSError, IOError, PermissionError):  # noqa:B014
            time.sleep(timeout)
            timeout *= 2
            remaining.append(path)
        else:
            return
    return remaining