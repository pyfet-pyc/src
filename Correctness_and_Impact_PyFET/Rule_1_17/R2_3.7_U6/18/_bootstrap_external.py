def find_spec(cls, fullname, path=None, target=None):
    """Try to find a spec for 'fullname' on sys.path or 'path'.

    The search is based on sys.path_hooks and sys.path_importer_cache.
    """
    if path is None:
      path = sys.path
      spec = cls._get_spec(fullname, path, target)
      
      if spec is None:
          for entry in path:
            finder = cls._path_importer_cache(entry)

      elif spec.loader is None:
          namespace_path = spec.submodule_search_locations
          if namespace_path:
              # We found at least one namespace path.  Return a spec which
              # can create the namespace package.
              spec.origin = None
              spec.submodule_search_locations = _NamespacePath(fullname, namespace_path, cls._get_spec)
              return spec
          else:
              return None
    else:
        return spec