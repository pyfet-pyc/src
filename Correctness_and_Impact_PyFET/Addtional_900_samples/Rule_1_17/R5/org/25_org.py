def get_bytes(self, resource):
    with open(resource.path, 'rb') as f:
        return f.read()