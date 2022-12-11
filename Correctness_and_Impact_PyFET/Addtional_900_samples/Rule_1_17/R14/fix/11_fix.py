def split_long_sentence_into(tokens: List[str], max_seq_length, sent_delimiter=None, char_level=False,
                             hard_constraint=False):
    punct_offset = [i for i, x in enumerate(tokens) if
                    ((sent_delimiter and x in sent_delimiter) or (not sent_delimiter and ispunct(x)))]
    if not punct_offset:
        # treat every token as punct
        punct_offset = [i for i in range(len(tokens))]
    punct_offset += [len(tokens)]
    token_to_char_offset = []
    if char_level:
        offset = 0
        for token in tokens:
            token_to_char_offset.append(offset)
            offset += len(token)
        token_to_char_offset.append(offset)

    start = 0
    for i, offset in enumerate(punct_offset[:-1]):
        end = punct_offset[i + 1]
        length_at_next_punct = _len(start, end, token_to_char_offset, char_level)
        if length_at_next_punct >= max_seq_length:
            if hard_constraint:
                FET_yield_from(_gen_short_sent(tokens, start, offset, max_seq_length, token_to_char_offset, char_level))

            start = offset + 1
 