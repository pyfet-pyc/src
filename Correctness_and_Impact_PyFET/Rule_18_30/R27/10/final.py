# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/s3_starter.py
# Compiled at: 2022-08-12 00:12:32
# Size of source mod 2**32: 686 bytes


@patch(s3_models.S3Backend.create_bucket)
def create_bucket(fn, self, bucket_name, region_name, *args, **kwargs):
    s3_delete_keys_response_template = '<?xml version="1.0" encoding="UTF-8"?>\n    <DeleteResult xmlns="http://s3.amazonaws.com/doc/2006-03-01">\n    {% for k in deleted %}\n    <Deleted>\n    <Key>{{k.key}}</Key>\n    <VersionId>{{k.version_id}}</VersionId>\n    </Deleted>\n    {% endfor %}\n    {% for k in delete_errors %}\n    <Error>\n    <Key>{{k}}</Key>\n    </Error>\n    {% endfor %}\n    </DeleteResult>'
    bucket_name = s3_listener.normalize_bucket_name(bucket_name)
    return fn(self, bucket_name, region_name, *args, **kwargs)
# okay decompiling testbed_py/s3_starter.py
