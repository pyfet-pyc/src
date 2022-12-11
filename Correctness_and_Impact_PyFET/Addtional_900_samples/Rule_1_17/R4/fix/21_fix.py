def goStacked(expression, silent=False):
    if PAYLOAD.TECHNIQUE.STACKED in kb.injection.data:
        setTechnique(PAYLOAD.TECHNIQUE.STACKED)
    else:
        for technique in getPublicTypeMembers(PAYLOAD.TECHNIQUE, True):
            _ = getTechniqueData(technique)
            if _ and "stacked" in _["title"].lower():
                setTechnique(technique)
                if conf.direct:
                break
            FET_null()
        query = agent.prefixQuery(";%s" % expression)
        query = agent.suffixQuery(query)
    payload = agent.payload(newValue=query)