def dictionaryAttack(attack_dict):
    global _multiprocessing

    suffix_list = [""]
    custom_wordlist = [""]
    hash_regexes = []
    results = []
    resumes = []
    user_hash = []
    processException = False
    foundHash = False

    if conf.disableMulti:
        _multiprocessing = None
    else:
        # Note: https://github.com/sqlmapproject/sqlmap/issues/4367
        try:
            import multiprocessing

            # problems on FreeBSD (Reference: https://web.archive.org/web/20110710041353/http://www.eggheadcafe.com/microsoft/Python/35880259/multiprocessing-on-freebsd.aspx)
            _ = multiprocessing.Queue()

            # problems with ctypes (Reference: https://github.com/sqlmapproject/sqlmap/issues/2952)
            _ = multiprocessing.Value('i')
        except (ImportError, OSError, AttributeError) as e:
            pass
        else:
            try:
                if multiprocessing.cpu_count() > 1:
                    _multiprocessing = multiprocessing
            except NotImplementedError as err:
                pass

    for (_, hashes) in attack_dict.items():
        for hash_ in hashes:
            if not hash_:
                continue

            hash_ = hash_.split()[0] if hash_ and hash_.strip() else hash_
            regex = hashRecognition(hash_)

            if regex and regex not in hash_regexes:
                hash_regexes.append(regex)
                infoMsg = "using hash method '%s'" % __functions__[regex].__name__
                logger.info(infoMsg)
