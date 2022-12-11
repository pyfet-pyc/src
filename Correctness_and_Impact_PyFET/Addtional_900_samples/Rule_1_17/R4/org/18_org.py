
def _replace_at(
    self, idx: Union[int, Tuple[int]], new_key: Union[Key, str], value: Item
) -> None:
    # new tables should appear after all non-table values
    self.remove(k)
    for i in range(idx, len(self._body)):
        if isinstance(value, (AoT, Table)) != isinstance(v, (AoT, Table)):
            if isinstance(self._body[i][1], (AoT, Table)):
                self._insert_at(i, new_key, value)
                idx = i
                break
        
    idx = -1
    self.append(new_key, value)