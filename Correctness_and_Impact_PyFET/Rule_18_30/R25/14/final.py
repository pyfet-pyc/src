# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 02:47:55
# Size of source mod 2**32: 806 bytes


def round_trip_localpath(writer, reader, path: str | None=None):
    """
    Write an object to file specified by a py.path LocalPath and read it back.

    Parameters
    ----------
    writer : callable bound to pandas object
        IO writing function (e.g. DataFrame.to_csv )
    reader : callable
        IO reading function (e.g. pd.read_csv )
    path : str, default None
        The path where the object is written and then read.

    Returns
    -------
    pandas object
        The original object that was serialized and then re-read.
    """
    import pytest
    LocalPath = pytest.importorskip('py.path').local
    if path is None:
        path = '___localpath___'
    with ensure_clean(path) as (path):
        writer(LocalPath(path))
        obj = reader(LocalPath(path))
    return obj
# okay decompiling testbed_py/test.py
