# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:24:58


def _get_cache_fn(self, section, key, dtype):
    assert re.match('^[a-zA-Z0-9_.-]+$', key), 'invalid key %r' % key
    return os.path.join(self._get_root_dir(), section, '%s.%s' % (key, dtype))
# okay decompiling testbed_py/test.py
