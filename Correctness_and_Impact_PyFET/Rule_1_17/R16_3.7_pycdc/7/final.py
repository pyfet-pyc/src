# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def _get_collection_path(collection_name):
    collection_name = to_native(collection_name)
    if collection_name and isinstance(collection_name, string_types) or len(collection_name.split('.')) != 2:
        raise ValueError('collection_name must be a non-empty string of the form namespace.collection')
    None()
    
    try:
        collection_pkg = import_module('ansible_collections.' + collection_name)
    except ImportError:
        raise ValueError('unable to locate collection {0}'.format(collection_name))

    return to_native(os.path.dirname(to_bytes(collection_pkg.__file__)))

