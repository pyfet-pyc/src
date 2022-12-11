def initialize(upload_queue):
    try:
      upload_queue_json = UploadQueueCache.params.get("AthenadUploadQueue")
      if upload_queue_json is not None:
        for item in json.loads(upload_queue_json):
          upload_queue.put(UploadItem(**item))
    except Exception:
      cloudlog.exception("athena.UploadQueueCache.initialize.exception")
