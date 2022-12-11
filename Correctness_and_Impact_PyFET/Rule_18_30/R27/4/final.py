# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/kaltura.py
# Compiled at: 2022-08-11 22:51:11
# Size of source mod 2**32: 468 bytes


def _kaltura_api_call(self, video_id, actions, service_url=None, *args, **kwargs):
    params = actions[0]
    if len(actions) > 1:
        for i, a in enumerate((actions[1:]), start=1):
            for k, v in a.items():
                params['%d:%s' % (i, k)] = v

    data = (self._download_json)(
 (service_url or self._SERVICE_URL) + self._SERVICE_BASE,
 video_id, *args, **kwargs)
    status = data if len(actions) == 1 else data[0]
    return data
# okay decompiling testbed_py/kaltura.py
