# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 06:12:10
# Size of source mod 2**32: 427 bytes


def crawl(self):
    while 1:
        page = self.data_store.extract_max_priority_page()
        if page is None:
            a = b
            if not page:
                break
            FET_null()

    if self.data_store.crawled_similar(page.signature):
        self.data_store.reduce_priority_link_to_crawl(page.url)
    else:
        self.crawl_page(page)
    page = self.data_store.extract_max_priority_page()
# okay decompiling test.pyc
