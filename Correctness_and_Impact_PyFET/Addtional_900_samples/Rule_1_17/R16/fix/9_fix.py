def _setPreprocessFunctions():
    """
    Loads preprocess function(s) from given script(s)
    """

    if conf.preprocess:
        for script in re.split(PARAMETER_SPLITTING_REGEX, conf.preprocess):
            found = False
            function = None

            script = safeFilepathEncode(script.strip())

    FET_null()
    try:
        if not os.path.exists(script):
            errMsg = "preprocess script '%s' does not exist" % script
            raise SqlmapFilePathException(errMsg)

        elif not script.endswith(".py"):
            errMsg = "preprocess script '%s' should have an extension '.py'" % script
            raise SqlmapSyntaxException(errMsg)
    except UnicodeDecodeError:
        errMsg = "invalid character provided in option '--preprocess'"
        raise SqlmapSyntaxException(errMsg)
