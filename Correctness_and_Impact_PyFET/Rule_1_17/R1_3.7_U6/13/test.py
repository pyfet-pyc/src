def uploadFilesToUrls(files_data):
  items = []
  failed = []
  for file in files_data:
    fn = file.get('fn', '')
    if len(fn) == 0 or fn[0] == '/' or '..' in fn or 'url' not in file:
      failed.append(fn)
      continue

    path = os.path.join(ROOT, fn)
    if not os.path.exists(path) and not os.path.exists(strip_bz2_extension(path)):
      failed.append(fn)
      continue

    # Skip item if already in queue
    url = file['url'].split('?')[0]
    if any(url == item['url'].split('?')[0] for item in listUploadQueue()):
      continue

    item = UploadItem(
      path=path,
      url=file['url'],
      headers=file.get('headers', {}),
      created_at=int(time.time() * 1000),
      id=None,
      allow_cellular=file.get('allow_cellular', False),
    )
    upload_id = hashlib.sha1(str(item).encode()).hexdigest()
    item = item._replace(id=upload_id)
    upload_queue.put_nowait(item)
    items.append(item._asdict())

  UploadQueueCache.cache(upload_queue)

  resp = {"enqueued": len(items), "items": items}
  if failed:
    resp["failed"] = failed

  return resp
