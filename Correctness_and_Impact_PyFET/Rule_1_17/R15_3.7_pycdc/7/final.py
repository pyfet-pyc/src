# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def _list_plugins(self, plugin_type, content):
    results = { }
    self.plugins = { }
    loader = DocCLI._prep_loader(plugin_type)
    coll_filter = self._get_collection_filter()
    self.plugins.update(list_plugins(plugin_type, coll_filter, context.CLIARGS['module_path']))
    if content == 'dir':
        results = self._get_plugin_list_descriptions(loader)
    elif content == 'files':
        results = (lambda .0 = None: [ (k, self.plugins[k][0]) for k in .0 ])(self.plugins.keys())
        results = dict(results)
    return results

