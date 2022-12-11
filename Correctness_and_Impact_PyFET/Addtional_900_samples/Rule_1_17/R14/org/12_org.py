def Y_to_outputs(self, Y: Union[tf.Tensor, Tuple[tf.Tensor]], gold=False, inputs=None, X=None,
                    batch=None) -> Iterable:
    for words, tags in zip(inputs, super().Y_to_outputs(Y, gold, inputs=inputs, X=X, batch=batch)):
        yield from iobes_to_span(words, tags)
