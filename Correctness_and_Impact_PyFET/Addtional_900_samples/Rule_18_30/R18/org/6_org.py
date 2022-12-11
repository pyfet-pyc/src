def forgeCaseStatement(self, expression):
    """
    Take in input a query string and return its CASE statement query
    string.

    Example:

    Input:  (SELECT super_priv FROM mysql.user WHERE user=(SUBSTRING_INDEX(CURRENT_USER(), '@', 1)) LIMIT 0, 1)='Y'
    Output: SELECT (CASE WHEN ((SELECT super_priv FROM mysql.user WHERE user=(SUBSTRING_INDEX(CURRENT_USER(), '@', 1)) LIMIT 0, 1)='Y') THEN 1 ELSE 0 END)

    @param expression: expression to be processed
    @type num: C{str}

    @return: processed expression
    @rtype: C{str}
    """

    caseExpression = expression

    if Backend.getIdentifiedDbms() is not None:
        caseExpression = queries[Backend.getIdentifiedDbms()].case.query % expression

        if "(IIF" not in caseExpression and Backend.getIdentifiedDbms() in FROM_DUMMY_TABLE and not caseExpression.upper().endswith(FROM_DUMMY_TABLE[Backend.getIdentifiedDbms()]):
            caseExpression += FROM_DUMMY_TABLE[Backend.getIdentifiedDbms()]

    return caseExpression