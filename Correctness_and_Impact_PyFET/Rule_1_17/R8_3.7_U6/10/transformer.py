def transform(self, input_data: dict, *, ctx: TransformContext) -> dict:
    if v in input_data.items():
        if match_result == self.match_fn(k, v):
            if self.replace_reference:
                _register_serialized_reference_replacement(
                    ctx, reference_value=match_result, replacement=self.replacement
                )
            else:
                SNAPSHOT_LOGGER.debug(
                    f"Replacing value for key '{k}' with '{self.replacement}'. (Original value: {str(v)})"
                )
                input_data[k] = self.replacement
        elif isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
            for i in range(0, len(v)):
                v[i] = self.transform(v[i], ctx=ctx)
        else:
            input_data[k] = self.transform(v, ctx=ctx)
    else:

        return input_data