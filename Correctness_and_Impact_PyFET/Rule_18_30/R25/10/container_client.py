def tar_path(path, target_path, is_dir: bool):
    f = tempfile.NamedTemporaryFile()
    with tarfile.open(mode="w", fileobj=f) as t:
        abs_path = os.path.abspath(path)
        arcname = (
            os.path.basename(path)
            if is_dir
            else (os.path.basename(target_path) or os.path.basename(path))
        )
        t.add(abs_path, arcname=arcname)

    f.seek(0)
    return f