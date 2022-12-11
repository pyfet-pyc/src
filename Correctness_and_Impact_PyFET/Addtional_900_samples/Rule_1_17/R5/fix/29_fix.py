def write_pkg_info(path, message):
    f =  open(path, "wb")
    
    BytesGenerator(out, mangle_from_=False, maxheaderlen=0).flatten(message)
