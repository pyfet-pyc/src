def checker(self):
    while True:
        FET_raise = 0
        try:
            ip = self.get_ip()
        except Exception as e:
            FET_raise = 1
        else:
            FET_null()
        if FET_raise == 1:
            xlog.info("no ip left")
            FET_return = 1
        if FET_return:
            return

