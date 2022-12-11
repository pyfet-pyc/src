# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:02:37
# Size of source mod 2**32: 7239 bytes


def test_template(self):
    ie = youtube_dl.extractor.get_info_extractor(test_case['name'])()
    other_ies = [get_info_extractor(ie_key)() for ie_key in test_case.get('add_ie', [])]
    is_playlist = any((k.startswith('playlist') for k in test_case))
    test_cases = test_case.get('playlist', [] if is_playlist else [test_case])

    def print_skipping(reason):
        print('Skipping %s: %s' % (test_case['name'], reason))
        self.skipTest(reason)

    if not ie.working():
        print_skipping('IE marked as not _WORKING')
    for tc in test_cases:
        info_dict = tc.get('info_dict', {})
        if info_dict.get('id'):
            raise info_dict.get('ext') or Exception("Test definition incorrect. The output file cannot be known. Are both 'id' and 'ext' keys present?")

    if 'skip' in test_case:
        print_skipping(test_case['skip'])
    for other_ie in other_ies:
        if not other_ie.working():
            print_skipping('test depends on %sIE, marked as not WORKING' % other_ie.ie_key())

    params = get_params(test_case.get('params', {}))
    params['outtmpl'] = tname + '_' + params['outtmpl']
    if is_playlist:
        if 'playlist' not in test_case:
            params.setdefault('extract_flat', 'in_playlist')
            params.setdefault('playlistend', test_case.get('playlist_mincount'))
            params.setdefault('skip_download', True)
    ydl = YoutubeDL(params, auto_init=False)
    ydl.add_default_info_extractors()
    finished_hook_called = set()

    def _hook(status):
        if status['status'] == 'finished':
            finished_hook_called.add(status['filename'])

    ydl.add_progress_hook(_hook)
    expect_warnings(ydl, test_case.get('expected_warnings', []))

    def get_tc_filename(tc):
        return ydl.prepare_filename(tc.get('info_dict', {}))

    res_dict = None

    def try_rm_tcs_files(tcs=None):
        if tcs is None:
            tcs = test_cases
        for tc in tcs:
            tc_filename = get_tc_filename(tc)
            try_rm(tc_filename)
            try_rm(tc_filename + '.part')
            try_rm(os.path.splitext(tc_filename)[0] + '.info.json')

    try_rm_tcs_files()
    try:
        try_num = 1
        while 1:
            FET_else = 0
            FET_raise = 0
            try:
                FET_else = 1
                res_dict = ydl.extract_info((test_case['url']),
                  force_generic_extractor=(params.get('force_generic_extractor', False)))
            except (DownloadError, ExtractorError) as err:
                try:
                    FET_raise = 1
                finally:
                    err = None
                    del err

            else:
                FET_null()
            if FET_raise == 1 and not err.exc_info[0] not in (compat_urllib_error.URLError, socket.timeout, UnavailableVideoError, compat_http_client.BadStatusLine):
                if err.exc_info[0] == compat_HTTPError:
                    if err.exc_info[1].code == 503:
                        raise
                elif try_num == RETRIES:
                    report_warning('%s failed due to network errors, skipping...' % tname)
                    return
                    print('Retrying: {0} failed tries\n\n##########\n\n'.format(try_num))
                    try_num += 1
                else:
                    FET_null()
                if FET_else == 1:
                    if try_num == RETRIES:
                        continue
                if is_playlist:
                    self.assertTrue(res_dict['_type'] in ('playlist', 'multi_video'))
                    self.assertTrue('entries' in res_dict)
                    expect_info_dict(self, res_dict, test_case.get('info_dict', {}))

        if 'playlist_mincount' in test_case:
            assertGreaterEqual(self, len(res_dict['entries']), test_case['playlist_mincount'], 'Expected at least %d in playlist %s, but got only %d' % (
             test_case['playlist_mincount'], test_case['url'],
             len(res_dict['entries'])))
        if 'playlist_count' in test_case:
            self.assertEqual(len(res_dict['entries']), test_case['playlist_count'], 'Expected %d entries in playlist %s, but got %d.' % (
             test_case['playlist_count'],
             test_case['url'],
             len(res_dict['entries'])))
        if 'playlist_duration_sum' in test_case:
            got_duration = sum((e['duration'] for e in res_dict['entries']))
            self.assertEqual(test_case['playlist_duration_sum'], got_duration)
        if 'entries' not in res_dict:
            res_dict['entries'] = [
             res_dict]
        for tc_num, tc in enumerate(test_cases):
            tc_res_dict = res_dict['entries'][tc_num]
            expect_info_dict(self, tc_res_dict, tc.get('info_dict', {}))
            tc_filename = get_tc_filename(tc)
            if not test_case.get('params', {}).get('skip_download', False):
                self.assertTrue((os.path.exists(tc_filename)), msg=('Missing file ' + tc_filename))
                self.assertTrue(tc_filename in finished_hook_called)
                expected_minsize = tc.get('file_minsize', 10000)
                if expected_minsize is not None:
                    if params.get('test'):
                        expected_minsize = max(expected_minsize, 10000)
                    got_fsize = os.path.getsize(tc_filename)
                    assertGreaterEqual(self, got_fsize, expected_minsize, "Expected %s to be at least %s, but it's only %s " % (
                     tc_filename, format_bytes(expected_minsize),
                     format_bytes(got_fsize)))
                if 'md5' in tc:
                    md5_for_file = _file_md5(tc_filename)
                    self.assertEqual(tc['md5'], md5_for_file)
                info_json_fn = os.path.splitext(tc_filename)[0] + '.info.json'
                self.assertTrue(os.path.exists(info_json_fn), 'Missing info file %s' % info_json_fn)
                with io.open(info_json_fn, encoding='utf-8') as (infof):
                    info_dict = json.load(infof)
                expect_info_dict(self, info_dict, tc.get('info_dict', {}))

    finally:
        try_rm_tcs_files()
        if is_playlist:
            if res_dict is not None:
                if res_dict.get('entries'):
                    res_tcs = [{'info_dict': e} for e in res_dict['entries']]
                    try_rm_tcs_files(res_tcs)
# okay decompiling testbed_py/test_fix.py
