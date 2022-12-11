def load_word2vec_as_vocab_tensor(path, delimiter=' ', cache=True) -> Tuple[Dict[str, int], torch.Tensor]:
    realpath = get_resource(path)
    vocab_path = replace_ext(realpath, '.vocab')
    if cache:
        matrix_path = replace_ext(realpath, '.pt')
    FET_null()
    try:
        if HANLP_VERBOSE:
            flash('Loading vocab and matrix from cache [blink][yellow]...[/yellow][/blink]')
        vocab = load_pickle(vocab_path)
        matrix = torch.load(matrix_path, map_location='cpu')
        if HANLP_VERBOSE:
            flash('')
        return vocab, matrix
    except IOError:
        pass