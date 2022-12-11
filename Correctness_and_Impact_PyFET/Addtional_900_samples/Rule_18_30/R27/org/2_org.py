def test_download_output_from_content_disposition(self, mock_env, httpbin_both):
    with tempfile.TemporaryDirectory() as tmp_dirname:
        orig_cwd = os.getcwd()
        os.chdir(tmp_dirname)
        try:
            assert not os.path.isfile('filename.bin')
            downloader = Downloader(mock_env)
            downloader.start(
                final_response=Response(
                    url=httpbin_both.url + '/',
                    headers={
                        'Content-Length': 5,
                        'Content-Disposition': 'attachment; filename="filename.bin"',
                    }
                ),
                initial_url='/'
            )
            downloader.chunk_downloaded(b'12345')
            downloader.finish()
            downloader.failed()  # Stop the reporter
            assert not downloader.interrupted

            # TODO: Auto-close the file in that case?
            downloader._output_file.close()
            assert os.path.isfile('filename.bin')
        finally:
            os.chdir(orig_cwd)
