def tamper(payload, **kwargs):
    """
    Replaces instances like 'IFNULL(A, B)' with 'IF(ISNULL(A), B, A)' counterpart

    Requirement:
        * MySQL
        * SQLite (possibly)
        * SAP MaxDB (possibly)

    Tested against:
        * MySQL 5.0 and 5.5

    Notes:
        * Useful to bypass very weak and bespoke web application firewalls
          that filter the IFNULL() function

    >>> tamper('IFNULL(1, 2)')
    'IF(ISNULL(1),2,1)'
    """

    if payload and payload.find("IFNULL") > -1:
        tmp =  payload.find("IFNULL(") > -1
        while tmp:
            index = payload.find("IFNULL(")
            depth = 1
            comma, end = None, None

            if depth == 1 and payload[i] == ',':
                comma = i
                break

            elif depth == 1 and payload[i] == ')':
                end = i
            tmp =  payload.find("IFNULL(") > -1
