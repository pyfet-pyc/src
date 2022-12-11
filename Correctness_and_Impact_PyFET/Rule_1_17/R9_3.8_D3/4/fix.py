def read_string(self):
    res = b''
    tmp = True
    while tmp:
        char = self.read_bytes(1)
        if char == b'\x00':
            break
        tmp = True
    return res