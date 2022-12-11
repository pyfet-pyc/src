def readlines(self, sizehint = 0):
    total = 0
    list = []
    while 1:
        line = self.readline()
        if not line: break
        list.append(line)
        total += len(line)
        if sizehint and total >= sizehint:
            break
    return list