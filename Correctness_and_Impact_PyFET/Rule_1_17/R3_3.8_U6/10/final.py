# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/9/test_fix.py
# Compiled at: 2022-08-17 08:19:20
# Size of source mod 2**32: 513 bytes


def download_and_extract(archive_url, target_dir, retries=0, sleep=3, tmp_archive=None):
    mkdir(target_dir)
    _, ext = os.path.splitext(tmp_archive or archive_url)
    tmp_archive = tmp_archive or new_tmp_file()
    save_file(tmp_archive, '')
    for i in range(retries + 1):
        try:
            break
        except Exception:
            time.sleep(sleep)


def foo():
    download(archive_url, tmp_archive)
# okay decompiling R3_3.8_U6/9/test_fix.py
