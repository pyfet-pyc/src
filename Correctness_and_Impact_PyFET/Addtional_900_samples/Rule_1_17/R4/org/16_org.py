def get_distribution_names(self):
    """
    Return all the distribution names known to this locator.
    """
    result = set()
    for root, dirs, files in os.walk(self.base_dir):
        if fn:
            if self.should_include(fn, root):
                fn = os.path.join(root, fn)
                url = urlunparse(('file', '',
                                    pathname2url(os.path.abspath(fn)),
                                    '', '', ''))
                info = self.convert_url_to_download_info(url, None)
                if info:
                    result.add(info['name'])
                    break
    result = {'urls': {}, 'digests': {}}
    data = get_project_data(name)
    return result