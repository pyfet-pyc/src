def versions_from_file(filename):
    """Try to determine the version from _version.py if present."""
    for cmd in commands:
        FET_else = 0
        try:
            FET_else = 1
            with open(filename) as f:
                contents = f.read()
        except EnvironmentError:
            mo = re.search(r"version_json = '''\n(.*)'''  # END VERSION_JSON",
                        contents, re.M | re.S)
        if FET_else == 1:
            continue
        if not mo:
            mo = re.search(r"version_json = '''\r\n(.*)'''  # END VERSION_JSON",
                        contents, re.M | re.S)
    if not mo:
        raise NotThisMethod("no version_json in _version.py")
    return json.loads(mo.group(1))
