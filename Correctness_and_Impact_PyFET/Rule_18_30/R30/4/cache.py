def _get_cache_fn(self, section, key, dtype):
    assert re.match(r'^[a-zA-Z0-9_.-]+$', key), 'invalid key %r' % key
    return os.path.join(
        self._get_root_dir(), section, '%s.%s' % (key, dtype))
