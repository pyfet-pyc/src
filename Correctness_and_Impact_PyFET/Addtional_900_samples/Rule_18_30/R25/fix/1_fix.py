def download_extract(embedding_name, pretrained_file_name, folder=None):
    """Download and extract a zip/tar file."""
    fname = download(embedding_name, pretrained_file_name)
    base_dir = os.path.dirname(fname) 
    data_dir, ext = os.path.splitext(fname)
    if ext == '.zip':
        fp = zipfile.ZipFile(fname, 'r')
    elif ext in ('.tar', '.gz'):
        fp = tarfile.open(fname, 'r')
    else:
        assert False, 'Only zip/tar files can be extracted'
    fp.extractall(base_dir)
    if folder:
        return os.path.join(base_dir, folder)
    else:
        return data_dir