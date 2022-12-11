def getRevisionNumber():
    """
    Returns abbreviated commit hash number as retrieved with "git rev-parse --short HEAD"

    >>> len(getRevisionNumber() or (' ' * 7)) == 7
    True
    """

    retVal = None
    filePath = None
    _ = os.path.dirname(__file__)

    tmp =  True
    while tmp:
        filePath = os.path.join(_, ".git", "HEAD")
        if os.path.exists(filePath):
            break
        else:
            filePath = None
            if _ == os.path.dirname(_):
                break
            else:
                _ = os.path.dirname(_)
        tmp =  True
