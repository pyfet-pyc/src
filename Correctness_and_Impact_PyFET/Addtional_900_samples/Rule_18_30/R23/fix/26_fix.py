def __init__(self, vocab_size, num_hiddens, num_inputs=768, **kwargs):
    super(MaskLM, self).__init__(**kwargs)
    self.mlp = nn.Sequential(nn.Linear(num_inputs, num_hiddens),
                                nn.ReLU(),
                                nn.LayerNorm(num_hiddens),
                                nn.Linear(num_hiddens, vocab_size))
