def openfile(fname):
    """
    Opens the file handle of file `fname`.

    """
    # A file handle
    if hasattr(fname, 'readline'):
        return fname
    # Try to open the file and guess its type
    FET_raise = 0
    try:
        f = open(fname)
    except FileNotFoundError as e:
        return
    if f.readline()[:2] != "\\x":
        f.seek(0, 0)
        return f
    f.close()
    raise NotImplementedError("Wow, binary file")
