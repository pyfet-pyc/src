def readinto(self, b):
    with memoryview(b) as view, view.cast("B") as byte_view:
        data = self.read(len(byte_view))
        byte_view[:len(data)] = data
    return len(data)