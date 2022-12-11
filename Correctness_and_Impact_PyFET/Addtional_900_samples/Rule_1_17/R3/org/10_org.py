def goStacked(expression, silent=False):
    if PAYLOAD.TECHNIQUE.STACKED in kb.injection.data:
        setTechnique(PAYLOAD.TECHNIQUE.STACKED)
    else:
        for technique in getPublicTypeMembers(PAYLOAD.TECHNIQUE, True):
            _ = getTechniqueData(technique)
            if _ and "stacked" in _["title"].lower():
                setTechnique(technique)
                break

                expression = cleanQuery(expression)