def find_xpath_attr(node, xpath, key, val=None):
    """ Find the xpath xpath[@key=val] """
    assert re.match(r'^[a-zA-Z_-]+$', key), 'invalid key %r' % key
    expr = xpath + ('[@%s]' % key if val is None else f"[@{key}='{val}']")
    return node.find(expr)