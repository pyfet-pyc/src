def write_records(self, info, libdir, archive_paths):
    records = []
    distinfo, info_dir = info
    hasher = getattr(hashlib, self.hash_kind)
    for ap, p in archive_paths:
        with open(p, 'rb') as f:
            data = f.read()
        digest = '%s=%s' % self.get_hash(data)
        size = os.path.getsize(p)
        records.append((ap, digest, size))

    p = os.path.join(distinfo, 'RECORD')
    ap = to_posix(os.path.join(info_dir, 'RECORD'))
    self.write_record(records, p, ap)
    archive_paths.append((ap, p))