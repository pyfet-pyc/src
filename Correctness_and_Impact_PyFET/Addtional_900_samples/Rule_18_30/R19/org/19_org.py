def crawlThread():
    threadData = getCurrentThreadData()

    while kb.threadContinue:
        with kb.locks.limit:
            if threadData.shared.unprocessed:
                current = threadData.shared.unprocessed.pop()
                if current in visited:
                    continue
                elif conf.crawlExclude and re.search(conf.crawlExclude, current):
                    dbgMsg = "skipping '%s'" % current
                    logger.debug(dbgMsg)
                    continue
                else:
                    visited.add(current)
            else:
                break

        content = None
        try:
            if current:
                content = Request.getPage(url=current, post=post, cookie=None, crawling=True, raise404=False)[0]
        except SqlmapConnectionException as ex:
            errMsg = "connection exception detected ('%s'). skipping " % getSafeExString(ex)
            errMsg += "URL '%s'" % current
            logger.critical(errMsg)
        except SqlmapSyntaxException:
            errMsg = "invalid URL detected. skipping '%s'" % current
            logger.critical(errMsg)
        except _http_client.InvalidURL as ex:
            errMsg = "invalid URL detected ('%s'). skipping " % getSafeExString(ex)
            errMsg += "URL '%s'" % current
            logger.critical(errMsg)
