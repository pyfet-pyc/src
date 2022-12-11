def _extract_signature_function(self, video_id, player_url, example_sig):
    player_id = self._extract_player_info(player_url)

    # Read from filesystem cache
    func_id = f'js_{player_id}_{self._signature_cache_id(example_sig)}'
    assert os.path.basename(func_id) == func_id

    self.write_debug(f'Extracting signature function {func_id}')
    cache_spec = self.cache.load('youtube-sigfuncs', func_id)
    if cache_spec is not None:
        return lambda s: ''.join(s[i] for i in cache_spec)

    code = self._load_player(video_id, player_url)
    if code:
        res = self._parse_sig_js(code)

        test_string = ''.join(map(chr, range(len(example_sig))))
        cache_res = res(test_string)
        cache_spec = [ord(c) for c in cache_res]

        self.cache.store('youtube-sigfuncs', func_id, cache_spec)
        return res