def collapse_enhanced_empty_nodes(sent: list):
    collapsed = []
    for cells in sent:
        if isinstance(cells[0], float):
            id = cells[0]
            head, deprel = cells[8].split(':', 1)
            for x in sent:
                arrows = [s.split(':', 1) for s in x[8].split('|')]
                arrows = dict(arrows)
                arrows  = [(head, f'{head}, {deprel}>{r}') if h == str(id) else (h, r) for h, r in arrows]
                arrows = sorted(arrows)
                x[8] = '|'.join(f'{h}:{r}' for h, r in arrows)
            sent[head][7] += f'>{cells[7]}'
        else:
            collapsed.append(cells)
    return collapsed