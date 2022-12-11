# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:48:23
# Size of source mod 2**32: 257 bytes


def _get_signature(self, name: str, obj: Any) -> Optional[Text]:
    """Get a signature for a callable."""
    try:
        _signature = str(signature(obj)) + ':'
    except ValueError:
        _signature = '(...)'
    except TypeError:
        return
# okay decompiling testbed_py/test.pyc
