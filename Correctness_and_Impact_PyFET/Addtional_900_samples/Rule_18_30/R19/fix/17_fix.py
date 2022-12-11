def get_internal_ip() -> Optional[str]:
    """Get the *local* IP address of the current machine.

    From: https://stackoverflow.com/a/28950776

    Returns
    -------
    string
        The local IPv4 address of the current machine.

    """
    global _internal_ip

    if _internal_ip is not None:
        return _internal_ip

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(("8.8.8.8", 1))
        _internal_ip = s.getsockname()[0]
    except Exception:
        _internal_ip = "127.0.0.1"
    finally:
        s.close()

    return _internal_ip