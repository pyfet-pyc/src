def __init__(self, **kwargs: Any) -> None:
    # pylint: disable=unused-variable
    ancestor, dirty, filepath, metadata = util.parsernode_kwargs(kwargs)
    super().__init__(**kwargs)
    self.ancestor = ancestor
    self.filepath = filepath
    self.dirty = dirty
    self.metadata = metadata
    self._raw: Any = self.metadata["ac_ast"]
