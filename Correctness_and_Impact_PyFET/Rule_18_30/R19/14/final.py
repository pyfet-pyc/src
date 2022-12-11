# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/final.py
# Compiled at: 2022-08-19 04:02:10
pass
# okay decompiling testbed_py/final.py
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 04:02:09
# Size of source mod 2**32: 948 bytes


def _load_backend(backend: str) -> types.ModuleType:
    """
    Load a pandas plotting backend.

    Parameters
    ----------
    backend : str
        The identifier for the backend. Either an entrypoint item registered
        with importlib.metadata, "matplotlib", or a module name.

    Returns
    -------
    types.ModuleType
        The imported backend.
    """
    from importlib.metadata import entry_points
    if backend == 'matplotlib':
        try:
            module = importlib.import_module('pandas.plotting._matplotlib')
        except ImportError:
            raise ImportError('matplotlib is required for plotting when the default backend "matplotlib" is selected.') from None
        else:
            return module
# okay decompiling testbed_py/test.pyc
# decompiled 2 files: 2 okay, 0 failed
