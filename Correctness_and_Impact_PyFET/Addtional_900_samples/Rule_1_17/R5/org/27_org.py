def read_pkg_info(path):
    with open(path, "r") as headers:
        message = Parser().parse(headers)
    return message