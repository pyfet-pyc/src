def _load_module(self, module):
    if not _meta_yml_to_dict:
        raise ValueError('ansible.utils.collection_loader._meta_yml_to_dict is not set')

    module._collection_meta = {}
    # TODO: load collection metadata, cache in __loader__ state

    collection_name = '.'.join(self._split_name[1:3])

    if collection_name == 'ansible.builtin':
        # ansible.builtin is a synthetic collection, get its routing config from the Ansible distro
        ansible_pkg_path = os.path.dirname(import_module('ansible').__file__)
        metadata_path = os.path.join(ansible_pkg_path, 'config/ansible_builtin_runtime.yml')
        with open(to_bytes(metadata_path), 'rb') as fd:
            raw_routing = fd.read()
    else:
        b_routing_meta_path = to_bytes(os.path.join(module.__path__[0], 'meta/runtime.yml'))
        if os.path.isfile(b_routing_meta_path):
            with open(b_routing_meta_path, 'rb') as fd:
                raw_routing = fd.read()
        else:
            raw_routing = ''
    FET_raise = 0
    try:
        if raw_routing:
            routing_dict = _meta_yml_to_dict(raw_routing, (collection_name, 'runtime.yml'))
            module._collection_meta = self._canonicalize_meta(routing_dict)
    except Exception as ex:
        FET_raise = 1
        
    else:
        AnsibleCollectionConfig.on_collection_load.fire(collection_name=collection_name, collection_path=os.path.dirname(module.__file__))

    if FET_raise == 1:
        raise ValueError('error parsing collection metadata: {0}'.format(to_native(ex)))

    return module