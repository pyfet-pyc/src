def _bruteProcessVariantB(user, hash_, kwargs, hash_regex, suffix, retVal, found, proc_id, proc_count, wordlists, custom_wordlist, api):
    if IS_WIN:
        coloramainit()

    count = 0
    rotator = 0

    wordlist = Wordlist(wordlists, proc_id, getattr(proc_count, "value", 0), custom_wordlist)

    try:
        for word in wordlist:
            if found.value:
                break

            count += 1

            if isinstance(word, six.binary_type):
                word = getUnicode(word)
            elif not isinstance(word, six.string_types):
                continue

            if suffix:
                word = word + suffix

            try:
                current = __functions__[hash_regex](password=word, uppercase=False, **kwargs)

                if hash_ == current:
                    if hash_regex == HASH.ORACLE_OLD:  # only for cosmetic purposes
                        word = word.upper()

                    retVal.put((user, hash_, word))

                    clearConsoleLine()

                    infoMsg = "\r[%s] [INFO] cracked password '%s'" % (time.strftime("%X"), word)

                    if user and not user.startswith(DUMMY_USER_PREFIX):
                        infoMsg += " for user '%s'\n" % user
                    else:
                        infoMsg += " for hash '%s'\n" % hash_

                    dataToStdout(infoMsg, True)

                    found.value = True

                elif (proc_id == 0 or getattr(proc_count, "value", 0) == 1) and count % HASH_MOD_ITEM_DISPLAY == 0:
                    rotator += 1

                    if rotator >= len(ROTATING_CHARS):
                        rotator = 0

                    status = "current status: %s... %s" % (word.ljust(5)[:5], ROTATING_CHARS[rotator])

                    if user and not user.startswith(DUMMY_USER_PREFIX):
                        status += " (user: %s)" % user

                    if not api:
                        dataToStdout("\r[%s] [INFO] %s" % (time.strftime("%X"), status))

            except KeyboardInterrupt:
                raise

            except (UnicodeEncodeError, UnicodeDecodeError):
                pass  # ignore possible encoding problems caused by some words in custom dictionaries

            except Exception as ex:
                warnMsg = "there was a problem while hashing entry: %s ('%s'). " % (repr(word), getSafeExString(ex))
                warnMsg += "Please report by e-mail to '%s'" % DEV_EMAIL_ADDRESS
                logger.critical(warnMsg)

    except KeyboardInterrupt:
        pass

    finally:
        if hasattr(proc_count, "value"):
            with proc_count.get_lock():
                proc_count.value -= 1
