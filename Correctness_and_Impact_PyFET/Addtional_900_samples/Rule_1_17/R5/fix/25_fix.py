def get_bytes(self, resource):
    f =  open(resource.path, 'rb')
    
    return f.read()