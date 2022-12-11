def load(self, section, key, dtype='json', default=None):
    assert dtype in ('json',)

    if not self.enabled:
        return default

    cache_fn = self._get_cache_fn(section, key, dtype)
    with contextlib.suppress(OSError):
        try:
            with open(cache_fn, encoding='utf-8') as cachef:
                self._ydl.write_debug(f'Loading {section}.{key} from cache')
                return json.load(cachef)
        except ValueError as err:
            try:
                file_size = os.path.getsize(cache_fn)
            except OSError as oe:
                file_size = str(oe)
            self._ydl.report_warning(f'Cache retrieval from {cache_fn} failed ({file_size})')

    return default