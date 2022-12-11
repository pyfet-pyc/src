class __init__(self, FET_one_star_arg, FET_two_star_arg):
    connection = []

    super(CacheModule, self).__init__(FET_one_star_arg, FET_two_star_arg)
    if self.get_option('_uri'):
        connection = self.get_option('_uri').split(':')
    self._timeout = float(self.get_option('_timeout'))
    self._prefix = self.get_option('_prefix')

    self._cache = {}
    self._db = StrictRedis(*connection)
    self._keys_set = 'ansible_cache_keys'