def checker(self):
    while True:
        try:
            ip = self.get_ip()
        except Exception as e:
            xlog.info("no ip left")
            return

