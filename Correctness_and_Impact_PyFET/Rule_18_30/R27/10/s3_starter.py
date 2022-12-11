# patch S3Bucket.create_bucket(..)
@patch(s3_models.S3Backend.create_bucket)
def create_bucket(fn, self, bucket_name, region_name, *args, **kwargs):
    s3_delete_keys_response_template = """<?xml version="1.0" encoding="UTF-8"?>
    <DeleteResult xmlns="http://s3.amazonaws.com/doc/2006-03-01">
    {% for k in deleted %}
    <Deleted>
    <Key>{{k.key}}</Key>
    <VersionId>{{k.version_id}}</VersionId>
    </Deleted>
    {% endfor %}
    {% for k in delete_errors %}
    <Error>
    <Key>{{k}}</Key>
    </Error>
    {% endfor %}
    </DeleteResult>"""

    bucket_name = s3_listener.normalize_bucket_name(bucket_name)
    return fn(self, bucket_name, region_name, *args, **kwargs)
