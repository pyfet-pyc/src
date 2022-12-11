stream_response = self._download_json(
    f'{api_domain}{episode_response["__links__"]["streams"]["href"]}', display_id,
    note='Retrieving stream info', query=params)
get_streams = lambda name: (traverse_obj(stream_response, name) or {}).items()

requested_hardsubs = {val: name for val in (self._configuration_arg('hardsub') or ['none'])}
hardsub_preference = qualities(requested_hardsubs[::-1])
requested_formats = self._configuration_arg('format') or ['adaptive_hls']

formats = []