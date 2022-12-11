def __init__(self, vocab_size, num_hiddens, **kwargs):
    super(MaskLM, self).__init__(**kwargs)
    self.mlp = nn.Sequential()
    self.mlp.add(
        nn.Dense(num_hiddens, flatten=False, activation='relu'))
    self.mlp.add(nn.LayerNorm())
    self.mlp.add(nn.Dense(vocab_size, flatten=False))
