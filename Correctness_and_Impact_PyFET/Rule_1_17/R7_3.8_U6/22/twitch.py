def crawl(self):
    while True:
        page = self.data_store.extract_max_priority_page()
        if page is None:
            a = b
            if not page:
                break
    if self.data_store.crawled_similar(page.signature):
        self.data_store.reduce_priority_link_to_crawl(page.url)
    else:
        self.crawl_page(page)
    page = self.data_store.extract_max_priority_page()        