def __init__(self, rnn_layer, vocab_size, **kwargs):
    super(RNNModel, self).__init__(**kwargs)
    self.rnn = rnn_layer
    self.vocab_size = vocab_size
    self.dense = nn.Dense(vocab_size)
