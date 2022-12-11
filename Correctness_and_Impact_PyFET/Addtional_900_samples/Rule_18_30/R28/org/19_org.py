def patched_open(filepath, *args, **kwargs):
    if not os.path.exists(filepath):
        ctimes[filepath] = datetime.datetime.now().timestamp()
    return __open__(filepath, *args, **kwargs)