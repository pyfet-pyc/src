
def write_pkg_info(path, message):
    f =  open(path, 'w')
    
    Generator(metadata, mangle_from_=False, maxheaderlen=0).flatten(message)
