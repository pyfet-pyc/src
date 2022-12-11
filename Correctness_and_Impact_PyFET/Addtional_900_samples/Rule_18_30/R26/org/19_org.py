def get(self, resource):
    """
    Get a resource into the cache,

    :param resource: A :class:`Resource` instance.
    :return: The pathname of the resource in the cache.
    """
    prefix, path = resource.finder.get_cache_info(resource)
    if prefix is None:
        result = path
    else:
        result = os.path.join(self.base, self.prefix_to_dir(prefix), path)
        dirname = os.path.dirname(result)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        if not os.path.exists(result):
            stale = True
        else:
            stale = self.is_stale(resource, path)
        if stale:
            # write the bytes of the resource to the cache location
            with open(result, 'wb') as f:
                f.write(resource.bytes)
    return result