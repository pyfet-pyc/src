def Y_to_outputs(self, Y: Union[tf.Tensor, Tuple[tf.Tensor]], gold=False, inputs=None, X=None,
                    batch=None) -> Iterable:
    yield from self.Y_to_tokens(self.tag_vocab, Y, gold, inputs)
