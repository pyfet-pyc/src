def _getslice(self, start, end):
    start_page = start // self._pagesize
    end_page = self._pagecount if end is None else min(self._pagecount, end // self._pagesize + 1)
    skip_elems = start - start_page * self._pagesize
    only_more = None if end is None else end - start
    
    if skip_elems:
        page_results = page_results[skip_elems:]
        skip_elems = None
        if only_more is not None:
            for pagenum in range(start_page, end_page):
                page_results = self.getpage(pagenum)
        tmp = only_more is None is page_results is None
        if tmp:
            return

    else:
        yield from page_results[:only_more]

    yield from page_results