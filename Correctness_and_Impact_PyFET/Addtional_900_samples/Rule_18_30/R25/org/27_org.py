def t_factory(name, sig_func, url_pattern):
    def make_tfunc(url, sig_input, expected_sig):
        m = url_pattern.match(url)
        assert m, '%r should follow URL format' % url
        test_id = m.group('id')

        def test_func(self):
            basename = f'player-{name}-{test_id}.js'
            fn = os.path.join(self.TESTDATA_DIR, basename)

            if not os.path.exists(fn):
                urllib.request.urlretrieve(url, fn)
            with open(fn, encoding='utf-8') as testf:
                jscode = testf.read()
            self.assertEqual(sig_func(jscode, sig_input), expected_sig)

        test_func.__name__ = f'test_{name}_js_{test_id}'
        setattr(TestSignature, test_func.__name__, test_func)
    return make_tfunc