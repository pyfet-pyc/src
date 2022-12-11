def __init__(self, ydl, info_dict):
    self.ydl = ydl

    # _entries must be assigned now since infodict can change during iteration
    entries = info_dict.get('entries')
    self.is_incomplete = bool(requested_entries)
    if self.is_incomplete:
        assert self.is_exhausted
        self._entries = [self.MissingEntry] * max(requested_entries)
        
        if entries is None:
            raise EntryNotInPlaylist('There are no entries')
        elif isinstance(entries, list):
            for i, entry in zip(requested_entries, entries):
                self._entries[i - 1] = entry
            FET_null()
            self.is_exhausted = True
        else:
            requested_entries = info_dict.get('requested_entries')
    
    else:
        self._entries = LazyList(entries)