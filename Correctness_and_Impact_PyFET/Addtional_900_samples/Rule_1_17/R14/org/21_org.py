def get_page(pagenum):
    firstid = pagenum * pagesize
    upto = min(size, pagenum * pagesize + pagesize)
    yield from range(firstid, upto)
