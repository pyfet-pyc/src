def save_file(file, content, append=False, permissions=None):
    mode = "a" if append else "w+"
    if not isinstance(content, str):
        mode = mode + "b"

    def _opener(path, flags):
        return os.open(path, flags, permissions)

    # make sure that the parent dir exsits
    mkdir(os.path.dirname(file))
    # store file contents
    # with open(file, mode, opener=_opener if permissions else None) as f:
    f = open(file, mode, opener=_opener if permissions else None)
    f.write(content)
    return f.flush()