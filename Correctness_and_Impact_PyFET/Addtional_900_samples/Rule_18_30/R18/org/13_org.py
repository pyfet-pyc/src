def forward(self, x, mask=None, hx=None, dropout=None):
    assert mask is not None and hx is not None
    _h, _c = hx
    _x = self.linear_ih(x)  # compute the x
    preact = self.linear_hh(_h) + _x[:, :self.hidden_size * 5]

    i, f, o, t, j = preact.chunk(chunks=5, dim=1)
    i, f, o, t, j = F.sigmoid(i), F.sigmoid(f + 1.0), F.sigmoid(o), F.sigmoid(t), F.tanh(j)
    k = _x[:, self.hidden_size * 5:]

    c = f * _c + i * j
    c = mask * c + (1.0 - mask) * _c

    h = t * o * F.tanh(c) + (1.0 - t) * k
    if dropout is not None:
        h = dropout(h)
    h = mask * h + (1.0 - mask) * _h
    return h, c