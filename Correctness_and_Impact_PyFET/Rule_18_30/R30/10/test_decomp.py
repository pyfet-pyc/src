# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:35:44


def test_firehose_s3(self):
    s3_prefix = '/testdata'
    test_data = '{"test": "firehose_data_%s"}' % short_uid()
    tags = firehose.list_tags_for_delivery_stream(DeliveryStreamName=stream_name)
    s3_resource.create_bucket(Bucket=TEST_BUCKET_NAME)
    firehose.put_record(DeliveryStreamName=stream_name, Record={'Data': to_bytes(test_data)})
    all_objects = testutil.list_all_s3_objects()
    testutil.assert_objects(json.loads(to_str(test_data)), all_objects)
    all_objects = testutil.map_all_s3_objects(buckets=[TEST_BUCKET_NAME])
    assert re.match('.*/\\d{4}/\\d{2}/\\d{2}/\\d{2}/.*-\\d{4}-\\d{2}-\\d{2}-\\d{2}.*', key), 'invalid key %r' % key
# okay decompiling testbed_py/test.py
