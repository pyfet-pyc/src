def read_pkg_info(path):
    with open(path, "r", encoding="ascii", errors="surrogateescape") as headers:
        message = Parser().parse(headers)
    return message