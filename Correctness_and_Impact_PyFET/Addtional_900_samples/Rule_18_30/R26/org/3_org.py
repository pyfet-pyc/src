def sharding(config, out_file):
    with open(out_file, "rb") as fr:
        captions = pickle.load(fr)
    target_dir = config.target_dir
    prefix = os.path.basename(
                os.path.splitext(config.caption_pkl_path)[0]
            ) + "." + config.bert_name + "."
    for split in ["train", "val"]:
        target_path = os.path.join(target_dir, split + "_meta")
        with open(target_path + ".pkl", "rb") as fr:
            meta = pickle.load(fr)
        print("load meta", target_path, len(meta))
        for shard_id in meta:
            numpify(
                shard_id, meta[shard_id], captions,
                target_dir, split, prefix
            )