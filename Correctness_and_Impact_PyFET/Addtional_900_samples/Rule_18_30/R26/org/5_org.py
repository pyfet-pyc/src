def _init_shard(self):
    if self.split == "train":
        meta_fn = os.path.join(self.vfeat_dir, "train" + "_meta.pkl")
        with open(meta_fn, "rb") as fr:
            meta = pickle.load(fr)
    elif self.split == "valid":
        meta_fn = os.path.join(self.vfeat_dir, "val" + "_meta.pkl")
        with open(meta_fn, "rb") as fr:
            meta = pickle.load(fr)
    elif self.split == "test":
        print("use how2 val as test.")
        meta_fn = os.path.join(self.vfeat_dir, "val" + "_meta.pkl")
        with open(meta_fn, "rb") as fr:
            meta = pickle.load(fr)
    else:
        raise ValueError("unsupported for MetaProcessor:", self.split)
    video_id_to_shard = {}
    for shard_id in meta:
        for video_idx, video_id in enumerate(meta[shard_id]):
            video_id_to_shard[video_id] = (shard_id, video_idx)
    self.video_id_to_shard = video_id_to_shard
