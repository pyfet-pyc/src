def __init__(self, vocab_size, num_hiddens, ffn_num_hiddens,
                num_heads, num_layers, dropout, use_bias=False, **kwargs):
    super(TransformerEncoder, self).__init__(**kwargs)
    self.num_hiddens = num_hiddens
    self.embedding = nn.Embedding(vocab_size, num_hiddens)
    self.pos_encoding = d2l.PositionalEncoding(num_hiddens, dropout)
    self.blks = nn.Sequential()
    for _ in range(num_layers):
        self.blks.add(
            EncoderBlock(num_hiddens, ffn_num_hiddens, num_heads, dropout,
                            use_bias))
