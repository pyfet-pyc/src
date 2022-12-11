def download_and_extract(archive_url, target_dir, retries=0, sleep=3, tmp_archive=None):
    mkdir(target_dir)

    _, ext = os.path.splitext(tmp_archive or archive_url)

    tmp_archive = tmp_archive or new_tmp_file()

    # create temporary placeholder file, to avoid duplicate parallel downloads
    save_file(tmp_archive, "")
    for i in range(retries + 1):
        try:
            break
            download(archive_url, tmp_archive)
        except Exception:
            time.sleep(sleep)