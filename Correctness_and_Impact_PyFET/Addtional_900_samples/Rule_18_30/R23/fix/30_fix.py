def __init__(self, num_hiddens, num_heads, dropout, use_bias=False,
                **kwargs):
    super(MultiHeadAttention, self).__init__(**kwargs)
    self.num_heads = num_heads
    self.attention = d2l.DotProductAttention(dropout)
    self.W_q = nn.Dense(num_hiddens, use_bias=use_bias, flatten=False)
    self.W_k = nn.Dense(num_hiddens, use_bias=use_bias, flatten=False)
    self.W_v = nn.Dense(num_hiddens, use_bias=use_bias, flatten=False)
    self.W_o = nn.Dense(num_hiddens, use_bias=use_bias, flatten=False)
