def _kaltura_api_call(self, video_id, actions, service_url=None, *args, **kwargs):
    params = actions[0]
    if len(actions) > 1:
        for i, a in enumerate(actions[1:], start=1):
            for k, v in a.items():
                params['%d:%s' % (i, k)] = v

    data = self._download_json(
        (service_url or self._SERVICE_URL) + self._SERVICE_BASE,
        video_id, *args, **kwargs)

    status = data if len(actions) == 1 else data[0]

    return data
