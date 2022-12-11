class CacheControlAdapter(HTTPAdapter):
    invalidating_methods = {"PUT", "PATCH", "DELETE"}

    def __init__(
        self,
        cache=None,
        cache_etags=True,
        controller_class=None,
        serializer=None,
        heuristic=None,
        cacheable_methods=None,
        *args,
        **kw
    ):
        super(CacheControlAdapter, self).__init__(*args, **kw)
        self.cache = DictCache() if cache is None else cache
        self.heuristic = heuristic
        self.cacheable_methods = cacheable_methods or ("GET",)

        controller_factory = controller_class or CacheController
        self.controller = controller_factory(
            self.cache, cache_etags=cache_etags, serializer=serializer
        )