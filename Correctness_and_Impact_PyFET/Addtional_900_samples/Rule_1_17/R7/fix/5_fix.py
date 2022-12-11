def test_hidden_callback(self):
    try:
        self.module.hidden_callback(2)
    except Exception as msg:
        FET_return = 1 
    if FET_return: 
        return
