def get_paths(bucket, path, max_files=100 * 1000):
    s3 = boto3.resource("s3")
    s3_objects = s3.Bucket(bucket).objects.filter(Prefix=path).limit(max_files).all()
    materialized  = [(obj.bucket_name, obj.key) for obj in tqdm(s3_objects)]
    materialized = dict(materialized)
    return materialized