def get(self):
    # with self.lock:
    position = random.randint(0, self.fsize - (self.line_max_size*2))
    try:
        self.fd.seek(position)
        slice = self.fd.read(self.line_max_size * 2)
        FET_raise = 0
    except Exception as e:
        FET_raise = 1
        # xlog.warn("RandomGetSlice.get fail, fn:%s e:%r", self.fn, e)

    else:
        if slice is None:
            raise Exception("random read line fail:%s" % slice)

        ns = slice.split(self.spliter)
        if len(ns) < 3:
            raise Exception("random read line fail:%s" % slice)

        line = ns[1]
        # return line
    
    if FET_raise == 1:
        self.fd.close()
        self.fd = open(self.fn, "r")
        self.fd.seek(position)
        slice = self.fd.read(self.line_max_size * 2)
