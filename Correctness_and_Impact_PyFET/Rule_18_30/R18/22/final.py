# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/concurrency.py
# Compiled at: 2022-08-11 20:26:48
# Size of source mod 2**32: 334 bytes


def maybe_install_uvloop() -> None:
    """If our environment has uvloop installed we use it.

    This is called only from command-line entry points to avoid
    interfering with the parent process if Black is used as a library.

    """
    try:
        import uvloop
        uvloop.install()
    except ImportError:
        pass
# okay decompiling testbed_py/concurrency.py
