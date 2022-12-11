def _find_control(self, name, type, kind, id, label, predicate, nr):
    if ((name is not None) and (name is not Missing) and
        not isstringlike(name)):
        raise TypeError("control name must be string-like")
    if (type is not None) and not isstringlike(type):
        raise TypeError("control type must be string-like")
    if (kind is not None) and not isstringlike(kind):
        raise TypeError("control kind must be string-like")
    if (id is not None) and not isstringlike(id):
        raise TypeError("control id must be string-like")
    if (label is not None) and not isstringlike(label):
        raise TypeError("control label must be string-like")
    if (predicate is not None) and not callable(predicate):
        raise TypeError("control predicate must be callable")
    if (nr is not None) and nr < 0:
        raise ValueError("control number must be a positive integer")

    orig_nr = nr
    found = None
    ambiguous = False
    if nr is None and self.backwards_compat:
        nr = 0

    for control in self.controls:
        if ((name is not None and name != control.name) and
            (name is not Missing or control.name is not None)):
            continue
        if type is not None and type != control.type:
            continue
        if kind is not None and not control.is_of_kind(kind):
            continue
        if id is not None and id != control.id:
            continue
        if predicate and not predicate(control):
            continue
        if label:
            for l in control.get_labels():
                if l.text.find(label) > -1:
                    break
            else:
                continue
        if nr is not None:
            if nr == 0:
                return control  # early exit: unambiguous due to nr
            nr -= 1
            continue
        if found:
            ambiguous = True
            break
        found = control