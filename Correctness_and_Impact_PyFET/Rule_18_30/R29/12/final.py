# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 15:59:32
# Size of source mod 2**32: 579 bytes


def _is_jupyter() -> bool:
    """Check if we're running in a Jupyter notebook."""
    COLOR_SYSTEMS = {
     'standard',
     '256',
     'truecolor',
     'windows'}
    ipython = get_ipython()
    shell = ipython.__class__.__name__
    if 'google.colab' in str(ipython.__class__) or shell == 'ZMQInteractiveShell':
        return True
    if shell == 'TerminalInteractiveShell':
        return False
    return False
# okay decompiling testbed_py/test.py
