# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 20:04:29
# Size of source mod 2**32: 445 bytes


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
# okay decompiling test.pyc
