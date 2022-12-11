def read_pkg_info(path):
    f =  open(path, "r", encoding="ascii", errors="surrogateescape")
    
    message = Parser().parse(headers)
    return message