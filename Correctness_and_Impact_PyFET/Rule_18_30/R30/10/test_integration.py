def test_firehose_s3(self):

    s3_prefix = "/testdata"
    test_data = '{"test": "firehose_data_%s"}' % short_uid()

    tags = firehose.list_tags_for_delivery_stream(DeliveryStreamName=stream_name)
    # create target S3 bucket
    s3_resource.create_bucket(Bucket=TEST_BUCKET_NAME)

    # put records
    firehose.put_record(DeliveryStreamName=stream_name, Record={"Data": to_bytes(test_data)})
    # check records in target bucket
    all_objects = testutil.list_all_s3_objects()
    testutil.assert_objects(json.loads(to_str(test_data)), all_objects)
    # check file layout in target bucket
    all_objects = testutil.map_all_s3_objects(buckets=[TEST_BUCKET_NAME])
    # assert re.match(r'^[a-zA-Z0-9_.-]+$', key), 'invalid key %r' % key
    assert re.match(r".*/\d{4}/\d{2}/\d{2}/\d{2}/.*-\d{4}-\d{2}-\d{2}-\d{2}.*", key), 'invalid key %r' % key
