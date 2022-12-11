def pretokenize(in_path: str, out_path: str, src: str, tgt: str):
    Args = namedtuple(
        "Args",
        [
            "moses_source_lang",
            "moses_target_lang",
            "moses_no_dash_splits",
            "moses_no_escape",
        ],
    )
    args = Args(
        moses_source_lang=src,
        moses_target_lang=tgt,
        moses_no_dash_splits=False,
        moses_no_escape=False,
    )
    pretokenizer = MosesTokenizer(args)
    with open(in_path) as f, open(out_path, "w") as f_o:
        for s in f:
            f_o.write(pretokenizer.encode(s.strip()) + "\n")
