def _build_selector_function(selector):
    if isinstance(selector, list):  # ,
        fs = [_build_selector_function(s) for s in selector]

        def selector_function(ctx):
            for f in fs:
                yield from f(ctx)
        return selector_function
