def dict_combine(self, dictionary: Union[DictInterface, Union[Dict[str, Any], Set[str]]]):
    if dictionary is not None and not isinstance(dictionary, DictInterface):
        if all(isinstance(k, str) for k in dictionary):
            dictionary = TrieDict(dictionary)
        else:
            _d = set()
            for k in dictionary:
                if isinstance(k, str):
                    _d.update(possible_tokenization(k))
                else:
                    _d.add(k)
            dictionary = TupleTrieDict(_d)
    self.config.dict_combine = dictionary