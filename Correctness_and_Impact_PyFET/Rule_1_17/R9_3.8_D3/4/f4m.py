def read_string(self):
    res = b''
    while True:
        char = self.read_bytes(1)
        if char == b'\x00':
            break
    return res