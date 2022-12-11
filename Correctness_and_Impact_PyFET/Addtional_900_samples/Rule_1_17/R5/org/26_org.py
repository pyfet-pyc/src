
def write_pkg_info(path, message):
    with open(path, 'w') as metadata:
        Generator(metadata, mangle_from_=False, maxheaderlen=0).flatten(message)
