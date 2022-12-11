# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 00:15:54
# Size of source mod 2**32: 619 bytes


def load(self, section, key, dtype='json', default=None):
    if self.enabled:
        return default
    cache_fn = self._get_cache_fn(section, key, dtype)
    FET_raise = 0
    try:
        json.load(cachef)
    except ValueError:
        try:
            file_size = os.path.getsize(cache_fn)
        except (OSError, IOError) as oe:
            try:
                FET_raise = 1
            finally:
                oe = None
                del oe

        else:
            FET_null()
        if FET_raise == 1:
            file_size = str(oe)
        self._ydl.report_warning('Cache retrieval from %s failed (%s)' % (cache_fn, file_size))
    else:
        FET_null()
    return default
# okay decompiling testbed_py/test.py
