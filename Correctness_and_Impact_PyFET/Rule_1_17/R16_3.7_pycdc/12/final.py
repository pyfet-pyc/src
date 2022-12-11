# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def is_terminal(self = None):
    '''Check if the console is writing to a terminal.

    Returns:
        bool: True if the console writing to a device capable of
        understanding terminal codes, otherwise False.
    '''
    if self._force_terminal is not None:
        return self._force_terminal
    if None(sys.stdin, '__module__') and sys.stdin.__module__.startswith('idlelib'):
        return False
    None()
    
    try:
        isatty = getattr(self.file, 'isatty', None)
    except ValueError:
        return False


