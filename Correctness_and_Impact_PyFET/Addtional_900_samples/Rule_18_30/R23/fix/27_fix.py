def __init__(self, key_size, query_size, value_size, num_hiddens,
                num_heads, dropout, bias=False, **kwargs):
    super().__init__(**kwargs)
    self.num_heads = num_heads
    self.attention = d2l.DotProductAttention(dropout)
    self.W_q = tf.keras.layers.Dense(num_hiddens, use_bias=bias)
    self.W_k = tf.keras.layers.Dense(num_hiddens, use_bias=bias)
    self.W_v = tf.keras.layers.Dense(num_hiddens, use_bias=bias)
    self.W_o = tf.keras.layers.Dense(num_hiddens, use_bias=bias)
