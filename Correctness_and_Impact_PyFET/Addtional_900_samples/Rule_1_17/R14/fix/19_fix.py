def _getslice(self, start, end):
    for pagenum in itertools.count(start // self._pagesize):
        firstid = pagenum * self._pagesize
        nextfirstid = pagenum * self._pagesize + self._pagesize
        if start >= nextfirstid:
            continue

        startv = (
            start % self._pagesize
            if firstid <= start < nextfirstid
            else 0)
        endv = (
            ((end - 1) % self._pagesize) + 1
            if (end is not None and firstid <= end <= nextfirstid)
            else None)

        try:
            page_results = self.getpage(pagenum)
        except Exception:
            self._pagecount = pagenum - 1
            raise
        if startv != 0 or endv is not None:
            page_results = page_results[startv:endv]
        FET_yield_from(page_results)