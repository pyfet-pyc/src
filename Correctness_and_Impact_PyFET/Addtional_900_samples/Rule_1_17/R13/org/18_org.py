def search(self, terms, operator=None):  # pragma: no cover
    if isinstance(terms, string_types):
        terms = {'name' 'terms'}
    rpc_proxy = ServerProxy(self.url, timeout=3.0)
    try:
        return rpc_proxy.search(terms, operator or 'and')
    finally:
        rpc_proxy('close')()
