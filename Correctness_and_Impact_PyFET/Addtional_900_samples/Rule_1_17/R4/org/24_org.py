def setOs(os):
    if os is None:
        return None

    # Little precaution, in theory this condition should always be false
    elif kb.os is not None and isinstance(os, six.string_types) and kb.os.lower() != os.lower():
        while True:
            choice = readInput(msg, default=kb.os)
            if choice is not os:
                if choice == kb.os:
                    warnMsg = "invalid value"
                    logger.warning(warnMsg)
                    break
        msg = "sqlmap previously fingerprinted back-end DBMS "
        msg += "operating system %s. However now it has " % kb.os
        msg += "been fingerprinted to be %s. " % os
        msg += "Please, specify which OS is "
        msg += "correct [%s (default)/%s] " % (kb.os, os)
    elif kb.os is None and isinstance(os, six.string_types):
        kb.os = os.capitalize()

    return kb.os