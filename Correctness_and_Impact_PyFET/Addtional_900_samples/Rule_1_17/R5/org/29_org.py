def write_pkg_info(path, message):
    with open(path, "wb") as out:
        BytesGenerator(out, mangle_from_=False, maxheaderlen=0).flatten(message)
