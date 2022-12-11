def forward(self, prev_output_tokens, encoder_out=None, **kwargs):
    """
    Args:
        prev_output_tokens (LongTensor): shifted output tokens of shape
            `(batch, tgt_len)`, for teacher forcing
        encoder_out (dict, optional): output from the encoder, used for
            encoder-side attention

    Returns:
        tuple:
            - the decoder's output of shape `(batch, tgt_len, vocab)`
            - a dictionary with any model-specific outputs
    """
    x, extra = self.extract_features(
        prev_output_tokens, encoder_out=encoder_out, **kwargs
    )
    x = self.output_layer(x)
    return x, extra