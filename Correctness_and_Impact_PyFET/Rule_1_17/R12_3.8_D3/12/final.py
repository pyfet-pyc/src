# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 23:32:34
# Size of source mod 2**32: 320 bytes
from typing import Any

def load_ipython_extension(ip: Any) -> None:
    from rich.pretty import install
    import rich.traceback as tr_install
    import rich.traceback as tr_table
    install()
    tr_install()
# okay decompiling test.pyc
