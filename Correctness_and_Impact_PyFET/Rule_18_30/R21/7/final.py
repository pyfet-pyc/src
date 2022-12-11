# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:30:24
# Size of source mod 2**32: 1561 bytes


def _load_module(self, module):
    if not _meta_yml_to_dict:
        raise ValueError('ansible.utils.collection_loader._meta_yml_to_dict is not set')
    else:
        module._collection_meta = {}
        collection_name = '.'.join(self._split_name[1:3])
        if collection_name == 'ansible.builtin':
            ansible_pkg_path = os.path.dirname(import_module('ansible').__file__)
            metadata_path = os.path.join(ansible_pkg_path, 'config/ansible_builtin_runtime.yml')
            with open(to_bytes(metadata_path), 'rb') as (fd):
                raw_routing = fd.read()
        else:
            b_routing_meta_path = to_bytes(os.path.join(module.__path__[0], 'meta/runtime.yml'))
            if os.path.isfile(b_routing_meta_path):
                with open(b_routing_meta_path, 'rb') as (fd):
                    raw_routing = fd.read()
            else:
                raw_routing = ''
    FET_raise = 0
    try:
        if raw_routing:
            routing_dict = _meta_yml_to_dict(raw_routing, (collection_name, 'runtime.yml'))
            module._collection_meta = self._canonicalize_meta(routing_dict)
    except Exception as ex:
        try:
            FET_raise = 1
        finally:
            ex = None
            del ex

    else:
        AnsibleCollectionConfig.on_collection_load.fire(collection_name=collection_name, collection_path=(os.path.dirname(module.__file__)))
    if FET_raise == 1:
        raise ValueError('error parsing collection metadata: {0}'.format(to_native(ex)))
    return module
# okay decompiling testbed_py/test.py
