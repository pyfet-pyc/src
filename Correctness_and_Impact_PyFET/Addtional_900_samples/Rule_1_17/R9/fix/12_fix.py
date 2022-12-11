def readlines(self, sizehint = 0):
    total = 0
    list = []
    tmp =  1
    while tmp:
        line = self.readline()
        if not line: break
        list.append(line)
        total += len(line)
        if sizehint and total >= sizehint:
            break
        tmp =  1
    return list