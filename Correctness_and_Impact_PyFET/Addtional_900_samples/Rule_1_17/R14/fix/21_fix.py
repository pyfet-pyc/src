def get_page(pagenum):
    firstid = pagenum * pagesize
    upto = min(size, pagenum * pagesize + pagesize)
    FET_yield_from(range(firstid, upto))
