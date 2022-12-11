def _server_time(self, access_key, video_id):
    if self.__server_time is not None:
        return self.__server_time

    self.__server_time = int(self._download_json(
        self._api_prefix(access_key) + 'server_time?anvack=' + access_key, video_id,
        note='Fetching server time')['server_time'])

    return self.__server_time