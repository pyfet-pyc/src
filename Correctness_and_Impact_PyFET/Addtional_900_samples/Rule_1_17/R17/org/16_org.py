def _as_partition_dirs(self, values: List[str]) -> List[str]:
    """Creates a list of partition directory names for the given values."""
    field_names = self._scheme.field_names
    if field_names:
        assert len(values) == len(field_names), (
            f"Expected {len(field_names)} partition value(s) but found "
            f"{len(values)}: {values}."
        )
    return self._encoder_fn(values)
