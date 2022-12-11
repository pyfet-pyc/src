def _yield_distributions(self):
    """
    Yield .dist-info and/or .egg(-info) distributions.
    """
    # We need to check if we've seen some resources already, because on
    # some Linux systems (e.g. some Debian/Ubuntu variants) there are
    # symlinks which alias other files in the environment.
    seen = set()
    for path in self.path:
        finder = resources.finder_for_path(path)
        if finder is None:
            continue
        r = finder.find('')
        if not r or not r.is_container:
            continue
        rset = sorted(r.resources)
        for entry in rset:
            r = finder.find(entry)
            if not r or r.path in seen:
                continue
            try:
                if self._include_dist and entry.endswith(DISTINFO_EXT):
                    possible_filenames = [METADATA_FILENAME,
                                            WHEEL_METADATA_FILENAME,
                                            LEGACY_METADATA_FILENAME]
                    for metadata_filename in possible_filenames:
                        metadata_path = posixpath.join(entry, metadata_filename)
                        pydist = finder.find(metadata_path)
                        if pydist:
                            break
                    else:
                        continue

                    with contextlib.closing(pydist.as_stream()) as stream:
                        metadata = Metadata(fileobj=stream, scheme='legacy')
                    logger.debug('Found %s', r.path)
                    seen.add(r.path)
                    yield new_dist_class(r.path, metadata=metadata,
                                            env=self)
                elif self._include_egg and entry.endswith(('.egg-info',
                                                            '.egg')):
                    logger.debug('Found %s', r.path)
                    seen.add(r.path)
                    yield old_dist_class(r.path, self)
            except Exception as e:
                msg = 'Unable to read distribution at %s, perhaps due to bad metadata: %s'
                logger.warning(msg, r.path, e)
                import warnings
                warnings.warn(msg % (r.path, e), stacklevel=2)
