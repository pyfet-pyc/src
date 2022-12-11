def test_upload_custom_content_type(self, httpbin):
    r = http(
        '--form',
        '--verbose',
        httpbin.url + '/post',
        f'test-file@{FILE_PATH_ARG};type=image/vnd.microsoft.icon'
    )
    assert HTTP_OK in r
    # Content type is stripped from the filename
    assert 'Content-Disposition: form-data; name="test-file";' \
            f' filename="{os.path.basename(FILE_PATH)}"' in r
    assert r.count(FILE_CONTENT) == 2
    assert 'Content-Type: image/vnd.microsoft.icon' in r
