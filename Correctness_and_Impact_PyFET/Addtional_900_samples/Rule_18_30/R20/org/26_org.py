def merge_linear_aux(aux1, aux2):
  try:
    out1 = aux1()
  except StoreException:
    # store 1 was not occupied, so store 2 better be
    try:
      out2 = aux2()
    except StoreException:
      raise StoreException("neither store occupied") from None
    else:
      return False, out2
  else:
    # store 1 was occupied, so let's check store 2 is not occupied
    try:
      out2 = aux2()
    except StoreException:
      return True, out1
    else:
      raise StoreException("both stores occupied")
