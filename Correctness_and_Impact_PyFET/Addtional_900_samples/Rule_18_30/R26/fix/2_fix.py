def get_feature_iterator(
    feature_type, checkpoint_path, layer, manifest_path, sample_pct
):
    feature_reader_cls = get_feature_reader(feature_type)
    with open(manifest_path, "r") as fp:
        lines = fp.read().split("\n")
        root = lines.pop(0).strip()
        file_path_list = [
            os.path.join(root, line.split("\t")[0])
            for line in lines
            if len(line) > 0
        ]
        if sample_pct < 1.0:
            file_path_list = random.sample(
                file_path_list, int(sample_pct * len(file_path_list))
            )
        num_files = len(file_path_list)
        reader = feature_reader_cls(
            checkpoint_path=checkpoint_path, layer=layer
        )

        def iterate():
            for file_path in file_path_list:
                feats = reader.get_feats(file_path)
                yield feats.cpu().numpy()

    return iterate, num_files