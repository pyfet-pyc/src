def load(fin, encoding='utf-8', full_model=True):
    """Load a model from a binary stream.

    Parameters
    ----------
    fin : file
        The readable binary stream.
    encoding : str, optional
        The encoding to use for decoding text
    full_model : boolean, optional
        If False, skips loading the hidden output matrix.  This saves a fair bit
        of CPU time and RAM, but prevents training continuation.

    Returns
    -------
    :class:`~gensim.models._fasttext_bin.Model`
        The loaded model.

    """
    if isinstance(fin, str):
        fin = open(fin, 'rb')

    magic, version = _struct_unpack(fin, '@2i')
    new_format = magic == _FASTTEXT_FILEFORMAT_MAGIC

    header_spec = _NEW_HEADER_FORMAT if new_format else _OLD_HEADER_FORMAT
    model = {name: _struct_unpack(fin, fmt)[0] for (name, fmt) in header_spec}

    if not new_format:
        model.update(dim=magic, ws=version)

    raw_vocab, vocab_size, nwords, ntokens = _load_vocab(fin, new_format, encoding=encoding)
    model.update(raw_vocab=raw_vocab, vocab_size=vocab_size, nwords=nwords, ntokens=ntokens)

    vectors_ngrams = _load_matrix(fin, new_format=new_format)

    if not full_model:
        hidden_output = None
    else:
        hidden_output = _load_matrix(fin, new_format=new_format)
        assert fin.read() == b'', 'expected to reach EOF'

    model.update(vectors_ngrams=vectors_ngrams, hidden_output=hidden_output)
    model = {k: v for k, v in model.items() if k in _FIELD_NAMES}
    return Model(**model)