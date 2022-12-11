def test_hidden_callback(self):
    FET_raise = 0
    try:
        self.module.hidden_callback(2)
    except Exception as msg:
        return
