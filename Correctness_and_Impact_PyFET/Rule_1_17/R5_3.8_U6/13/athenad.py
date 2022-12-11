def getPublicKey():
  if not os.path.isfile(PERSIST + '/comma/id_rsa.pub'):
    return None

  with open(PERSIST + '/comma/id_rsa.pub') as f:
    return f.read()