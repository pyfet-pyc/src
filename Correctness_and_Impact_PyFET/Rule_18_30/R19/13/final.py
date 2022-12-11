# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:49:33
# Size of source mod 2**32: 348 bytes


def initialize(upload_queue):
    try:
        upload_queue_json = UploadQueueCache.params.get('AthenadUploadQueue')
        if upload_queue_json is not None:
            for item in json.loads(upload_queue_json):
                upload_queue.put(UploadItem(**item))

    except Exception:
        cloudlog.exception('athena.UploadQueueCache.initialize.exception')
# okay decompiling testbed_py/test.pyc
