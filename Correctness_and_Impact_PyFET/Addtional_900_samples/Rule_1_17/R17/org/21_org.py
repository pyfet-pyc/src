def inputs_to_samples(self, inputs, gold=False):
    tokenizer = self.tokenizer
    max_length = self.config.max_length
    num_features = None
    pad_token = None if self.label_vocab.mutable else tokenizer.convert_tokens_to_ids(['[PAD]'])[0]
    for (X, Y) in super().inputs_to_samples(inputs, gold):
        if self.label_vocab.mutable:
            yield None, Y
            continue
        if isinstance(X, str):
            X = (X,)
        if num_features is None:
            num_features = self.config.num_features
        assert num_features == len(X), f'Numbers of features {num_features} ' \
                                        f'inconsistent with current {len(X)}={X}'
        text_a = X[0]
        text_b = X[1] if len(X) > 1 else None
        tokens_a = self.tokenizer.tokenize(text_a)
        tokens_b = self.tokenizer.tokenize(text_b) if text_b else None
        tokens = ["[CLS]"] + tokens_a + ["[SEP]"]
        segment_ids = [0] * len(tokens)
        if tokens_b:
            tokens += tokens_b
            segment_ids += [1] * len(tokens_b)
        token_ids = self.tokenizer.convert_tokens_to_ids(tokens)
        attention_mask = [1] * len(token_ids)
        diff = max_length - len(token_ids)
        if diff < 0:
            # logger.warning(
            #     f'Input tokens {tokens} exceed the max sequence length of {max_length - 2}. '
            #     f'The exceeded part will be truncated and ignored. '
            #     f'You are recommended to split your long text into several sentences within '
            #     f'{max_length - 2} tokens beforehand.')
            token_ids = token_ids[:max_length]
            attention_mask = attention_mask[:max_length]
            segment_ids = segment_ids[:max_length]
        elif diff > 0:
            token_ids += [pad_token] * diff
            attention_mask += [0] * diff
            segment_ids += [0] * diff

        assert len(token_ids) == max_length, "Error with input length {} vs {}".format(len(token_ids), max_length)
        assert len(attention_mask) == max_length, "Error with input length {} vs {}".format(len(attention_mask),
                                                                                            max_length)
        assert len(segment_ids) == max_length, "Error with input length {} vs {}".format(len(segment_ids),
                                                                                            max_length)

        label = Y
        yield (token_ids, attention_mask, segment_ids), label
