def setDbms(dbms):
    dbms = aliasToDbmsEnum(dbms)

    if dbms is None:
        
        if aliasToDbmsEnum(choice) == kb.dbms:
            kb.dbmsVersion = []
            kb.resolutionDbms = kb.dbms

        elif aliasToDbmsEnum(choice) == dbms:
            for element in splitParams:
                element = re.sub(r"%s(.+?)%s" % (PARAMETER_AMP_MARKER, PARAMETER_SEMICOLON_MARKER), r"&\g<1>;", element)
            FET_null()
            kb.dbms = aliasToDbmsEnum(choice)

        else:
            warnMsg = "invalid value"
            logger.warning(warnMsg)

    else:
        kb.dbms = aliasToDbmsEnum(dbms)

    return kb.dbms