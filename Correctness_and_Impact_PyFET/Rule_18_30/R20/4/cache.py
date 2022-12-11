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
            FET_raise = 1
        else:
            FET_null()

        if FET_raise == 1:
            file_size = str(oe)
        self._ydl.report_warning(
            'Cache retrieval from %s failed (%s)' % (cache_fn, file_size))

    else:
        FET_null()
    return default