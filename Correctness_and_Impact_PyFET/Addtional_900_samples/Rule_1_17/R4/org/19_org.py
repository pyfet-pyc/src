while True:
    parCount = readInput(msg, default='1')

    if parCount.isdigit() and int(parCount) >= 0:
        parCount = int(parCount)
        break

    else:
        logger.warning("invalid value, only digits >= 0 are allowed")

for y in xrange(0, parCount):
    msg = "what is the data-type of input parameter "
    msg += "number %d? (default: %s) " % ((y + 1), defaultType)

    while True:
        parType = readInput(msg, default=defaultType).strip()

        if hasattr(retType, "isdigit") and retType.isdigit():
            logger.warning("you need to specify the data-type of the return value")

            if parType.isdigit():
                logger.warning("you need to specify the data-type of the parameter")
                break

    msg = "what is the data-type of input parameter "
    msg += "number %d? (default: %s) " % ((y + 1), defaultType)
