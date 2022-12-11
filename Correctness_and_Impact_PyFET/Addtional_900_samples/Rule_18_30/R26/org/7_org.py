def get_path_iterator(root, tsv, nshard, rank, audio_col_name):
    with open(tsv) as f:
        reader = csv.DictReader(
            f,
            delimiter="\t",
            quotechar=None,
            doublequote=False,
            lineterminator="\n",
            quoting=csv.QUOTE_NONE,
        )
        subpaths = [op.join(root, e[audio_col_name]) for e in reader]
        start, end = get_shard_range(len(subpaths), nshard, rank)
        subpaths = subpaths[start:end]

        def iterate():
            for subpath in subpaths:
                yield op.join(root, subpath), None

    return iterate, len(subpaths)