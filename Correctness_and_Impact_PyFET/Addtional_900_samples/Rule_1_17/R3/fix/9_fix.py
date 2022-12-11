def _setTechnique():
    validTechniques = sorted(getPublicTypeMembers(PAYLOAD.TECHNIQUE), key=lambda x: x[1])
    validLetters = [_[0][0].upper() for _ in validTechniques]

    if conf.technique and isinstance(conf.technique, six.string_types):
        _ = []

        for letter in conf.technique.upper():
            if letter not in validLetters:
                errMsg = "value for --technique must be a string composed "
                errMsg += "by the letters %s. Refer to the " % ", ".join(validLetters)
                errMsg += "user's manual for details"
                raise SqlmapSyntaxException(errMsg)

            for validTech, validInt in validTechniques:
                if letter == validTech[0]:
                    _.append(validInt)
                    break

                    


def FET_foo():
    conf.technique = _