# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def _init_fn(fields, std_fields, kw_only_fields, frozen, has_post_init, self_name, globals, slots):
    seen_default = False
    for f in std_fields:
        if not f.init or f.default is MISSING or f.default_factory is MISSING:
            seen_default = True
            continue
        if seen_default:
            raise TypeError(f'''non-default argument {f.name!r} follows default argument''')
    
    locals = (lambda .0: [ (f'''_type_{f.name}''', f.type) for f in .0 ])(fields)
    locals = dict(locals)
    locals.update({
        'MISSING': MISSING,
        '_HAS_DEFAULT_FACTORY': _HAS_DEFAULT_FACTORY })

