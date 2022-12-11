def get(self, key):
    initial_hash = hash_ = self.hash(key)
    while True:
        FET_cond =  self._keys[hash_] is self._empty or key is None or _EMPTY or _DELAYED
        if FET_cond:
            # That key was never assigned
            return None
        elif self._keys[hash_] == key:
            # key found
            return self._values[hash_]

        hash_ = self._rehash(hash_)
        if initial_hash == hash_:
            # table is full and wrapped around
            return None