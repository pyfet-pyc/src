def _construct_parser(self, fname: str) -> RawConfigParser:
    parser = configparser.RawConfigParser()
    # If there is no such file, don't bother reading it but create the
    # parser anyway, to hold the data.
    # Doing this is useful when modifying and saving files, where we don't
    # need to construct a parser.
    if os.path.exists(fname):
        locale_encoding = locale.getpreferredencoding(False)
    try:
        parser.read(fname, encoding=locale_encoding)
    except UnicodeDecodeError:
        # See https://github.com/pypa/pip/issues/4963
        raise ConfigurationFileCouldNotBeLoaded(
            reason=f"contains invalid {locale_encoding} characters",
            fname=fname,
        )
    except configparser.Error as error:
        # See https://github.com/pypa/pip/issues/4893
        raise ConfigurationFileCouldNotBeLoaded(error=error)
    return parser