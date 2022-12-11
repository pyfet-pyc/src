# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/anvato.py
# Compiled at: 2022-08-11 19:01:33
# Size of source mod 2**32: 338 bytes


def _server_time(self, access_key, video_id):
    if self.__server_time is not None:
        return self.__server_time
    self.__server_time = int(self._download_json((self._api_prefix(access_key) + 'server_time?anvack=' + access_key),
      video_id, note='Fetching server time')['server_time'])
    return self.__server_time
# okay decompiling testbed_py/anvato.py
