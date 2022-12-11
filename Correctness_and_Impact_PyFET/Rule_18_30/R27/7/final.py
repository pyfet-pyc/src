# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/_collection_config.py
# Compiled at: 2022-08-12 00:09:09
# Size of source mod 2**32: 327 bytes


def fire(self, *args, **kwargs):
    cls._collection_finder = None
    cls._default_collection = None
    cls._on_collection_load = _EventSource()
    for h in self._handlers:
        h(*args, **kwargs)
        if (self._on_exception)(h, ex, *args, **kwargs):
            raise
# okay decompiling testbed_py/_collection_config.py
