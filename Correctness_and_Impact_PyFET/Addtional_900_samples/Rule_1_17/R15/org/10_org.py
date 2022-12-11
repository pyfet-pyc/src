def gen_table(self, serialized_features, fstyle=None, fstyle_implies=None,
                **kwargs):

    if fstyle is None:
        fstyle = lambda ft: f'``{ft}``'
    if fstyle_implies is None:
        fstyle_implies = lambda origin, ft: fstyle(ft)

    rows = []
    have_gather = False
    for f, implies, gather in serialized_features:
        if gather:
            have_gather = True
        name = fstyle(f)
        implies = ' '.join([fstyle_implies(f, i) for i in implies])
        gather = ' '.join([fstyle_implies(f, i) for i in gather])
        rows.append((name, implies, gather))
    if not rows:
        return ''
    fields = ["Name", "Implies", "Gathers"]
    if not have_gather:
        del fields[2]
        rows = {name: implies for name, implies, _ in rows}
    return self.gen_rst_table(fields, rows, **kwargs)