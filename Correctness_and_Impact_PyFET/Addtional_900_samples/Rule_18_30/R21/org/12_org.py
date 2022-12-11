
    def dbTableValues(self, tableValues):
        replication = None
        rtable = None
        dumpFP = None
        appendToFile = False
        warnFile = False

        if tableValues is None:
            return

        db = tableValues["__infos__"]["db"]
        if not db:
            db = "All"
        table = tableValues["__infos__"]["table"]

        if conf.api:
            self._write(tableValues, content_type=CONTENT_TYPE.DUMP_TABLE)

        try:
            dumpDbPath = os.path.join(conf.dumpPath, unsafeSQLIdentificatorNaming(db))
        except UnicodeError as e:
            try:
                dumpDbPath = os.path.join(conf.dumpPath, normalizeUnicode(unsafeSQLIdentificatorNaming(db)))
            except (UnicodeError, OSError) as ex:
                tempDir = tempfile.mkdtemp(prefix="sqlmapdb")
                warnMsg = "currently unable to use regular dump directory. "
                warnMsg += "Using temporary directory '%s' instead" % tempDir
                logger.warning(warnMsg)

                dumpDbPath = tempDir

        if conf.dumpFormat == DUMP_FORMAT.SQLITE:
            replication = Replication(os.path.join(conf.dumpPath, "%s.sqlite3" % unsafeSQLIdentificatorNaming(db)))
        elif conf.dumpFormat in (DUMP_FORMAT.CSV, DUMP_FORMAT.HTML):
            if not os.path.isdir(dumpDbPath):
                try:
                    os.makedirs(dumpDbPath)
                except:
                    warnFile = True

                    _ = re.sub(r"[^\w]", UNSAFE_DUMP_FILEPATH_REPLACEMENT, unsafeSQLIdentificatorNaming(db))
                    dumpDbPath = os.path.join(conf.dumpPath, "%s-%s" % (_, hashlib.md5(getBytes(db)).hexdigest()[:8]))

                    if not os.path.isdir(dumpDbPath):
                        try:
                            os.makedirs(dumpDbPath)
                        except Exception as ex:
                            tempDir = tempfile.mkdtemp(prefix="sqlmapdb")
                            warnMsg = "unable to create dump directory "
                            warnMsg += "'%s' (%s). " % (dumpDbPath, getSafeExString(ex))
                            warnMsg += "Using temporary directory '%s' instead" % tempDir
                            logger.warning(warnMsg)

                            dumpDbPath = tempDir

            dumpFileName = os.path.join(dumpDbPath, re.sub(r'[\\/]', UNSAFE_DUMP_FILEPATH_REPLACEMENT, "%s.%s" % (unsafeSQLIdentificatorNaming(table), conf.dumpFormat.lower())))
            if not checkFile(dumpFileName, False):
                try:
                    openFile(dumpFileName, "w+b").close()
                except SqlmapSystemException:
                    raise
                except:
                    warnFile = True

                    _ = re.sub(r"[^\w]", UNSAFE_DUMP_FILEPATH_REPLACEMENT, normalizeUnicode(unsafeSQLIdentificatorNaming(table)))
                    if len(_) < len(table) or IS_WIN and table.upper() in WINDOWS_RESERVED_NAMES:
                        _ = re.sub(r"[^\w]", UNSAFE_DUMP_FILEPATH_REPLACEMENT, unsafeSQLIdentificatorNaming(table))
                        dumpFileName = os.path.join(dumpDbPath, "%s-%s.%s" % (_, hashlib.md5(getBytes(table)).hexdigest()[:8], conf.dumpFormat.lower()))
                    else:
                        dumpFileName = os.path.join(dumpDbPath, "%s.%s" % (_, conf.dumpFormat.lower()))
            else:
                appendToFile = any((conf.limitStart, conf.limitStop))

                if not appendToFile:
                    count = 1
                    while True:
                        candidate = "%s.%d" % (dumpFileName, count)
                        if not checkFile(candidate, False):
                            try:
                                shutil.copyfile(dumpFileName, candidate)
                            except IOError:
                                pass
                            break
                        else:
                            count += 1
