def track(tree, i):
    label = tree.label()
    if delete_labels is not None and label in delete_labels:
        label = None
    if equal_labels is not None:
        label = equal_labels.get(label, label)
    if len(tree) == 1 and not isinstance(tree[0], Tree):
        return (i + 1 if label is not None else i), []
    j, spans = i, []
    for child in tree:
        if isinstance(child, Tree):
            j, s = track(child, j)
            spans += s
    if label is not None and j > i:
        spans = [(i, j, label)] + spans
    return j, spans

return track(tree, 0)[1]