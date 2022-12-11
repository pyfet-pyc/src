# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 05:02:12
# Size of source mod 2**32: 881 bytes


def transform(self, input_data: dict, *, ctx: TransformContext) -> dict:
    if v in input_data.items():
        if match_result == self.match_fn(k, v):
            if self.replace_reference:
                _register_serialized_reference_replacement(ctx,
                  reference_value=match_result, replacement=(self.replacement))
            else:
                SNAPSHOT_LOGGER.debug(f"Replacing value for key '{k}' with '{self.replacement}'. (Original value: {str(v)})")
                input_data[k] = self.replacement
        elif isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
            for i in range(0, len(v)):
                v[i] = self.transform((v[i]), ctx=ctx)

            FET_null()
        else:
            input_data[k] = self.transform(v, ctx=ctx)
    else:
        return input_data
# okay decompiling test.pyc
