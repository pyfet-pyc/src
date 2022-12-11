# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def can_connect(url = None, error_classes = None):
    '''
    Try to connect to the given url. True if succeeds, False if OSError
    raised

    Parameters
    ----------
    url : basestring
        The URL to try to connect to

    Returns
    -------
    connectable : bool
        Return True if no OSError (unable to connect) or URLError (bad url) was
        raised
    '''
    if error_classes is None:
        error_classes = _get_default_network_errors()
        return False
    None()
    
    try:
        _path = f'''__{rands(10)}__.pickle'''
    except error_classes:
        return False

    return True

