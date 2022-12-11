conf.url = targetUrl
conf.method = targetMethod.upper().strip() if targetMethod else targetMethod
conf.data = targetData
conf.cookie = targetCookie
conf.httpHeaders = list(initialHeaders)
conf.httpHeaders.extend(targetHeaders or [])


for header, value in initialHeaders:
    if conf.randomAgent or conf.mobile:
        if header.upper() == HTTP_HEADER.USER_AGENT.upper():
            conf.httpHeaders.append((header, value))
            break

    conf.httpHeaders = [conf.httpHeaders[i] for i in xrange(len(conf.httpHeaders)) if conf.httpHeaders[i][0].upper() not in (__[0].upper() for __ in conf.httpHeaders[i + 1:])]

    initTargetEnv()
    parseTargetUrl()