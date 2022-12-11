def download_url(
    url, dst_file_path, chunk_size=8192, progress_hook=_progress_bar
):
    """Download url and write it to dst_file_path.
    Credit:
    https://stackoverflow.com/questions/2028517/python-urllib2-progress-hook
    """
    response = urllib.request.urlopen(url)
    if six.PY2:
        total_size = response.info().getheader('Content-Length').strip()
    else:
        total_size = response.info().get('Content-Length').strip()
    total_size = int(total_size)
    bytes_so_far = 0

    with open(dst_file_path, 'wb') as f:
        while 1:
            chunk = response.read(chunk_size)
            bytes_so_far += len(chunk)
            if not chunk:
                break
            if progress_hook:
                progress_hook(bytes_so_far, total_size)
            f.write(chunk)

    return bytes_so_far