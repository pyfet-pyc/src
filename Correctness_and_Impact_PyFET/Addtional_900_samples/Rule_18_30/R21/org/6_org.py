def _setResultsFile():
    """
    Create results file for storing results of running in a
    multiple target mode.
    """

    if not conf.multipleTargets:
        return

    if not conf.resultsFP:
        conf.resultsFile = conf.resultsFile or os.path.join(paths.SQLMAP_OUTPUT_PATH, time.strftime(RESULTS_FILE_FORMAT).lower())
        found = os.path.exists(conf.resultsFile)

        try:
            conf.resultsFP = openFile(conf.resultsFile, "a", UNICODE_ENCODING, buffering=0)
        except (OSError, IOError) as ex:
            try:
                warnMsg = "unable to create results file '%s' ('%s'). " % (conf.resultsFile, getUnicode(ex))
                handle, conf.resultsFile = tempfile.mkstemp(prefix=MKSTEMP_PREFIX.RESULTS, suffix=".csv")
                os.close(handle)
                conf.resultsFP = openFile(conf.resultsFile, "w+", UNICODE_ENCODING, buffering=0)
                warnMsg += "Using temporary file '%s' instead" % conf.resultsFile
                logger.warning(warnMsg)
            except IOError as _:
                errMsg = "unable to write to the temporary directory ('%s'). " % _
                errMsg += "Please make sure that your disk is not full and "
                errMsg += "that you have sufficient write permissions to "
                errMsg += "create temporary files and/or directories"
                raise SqlmapSystemException(errMsg)

        if not found:
            conf.resultsFP.writelines("Target URL,Place,Parameter,Technique(s),Note(s)%s" % os.linesep)

        logger.info("using '%s' as the CSV results file in multiple targets mode" % conf.resultsFile)
