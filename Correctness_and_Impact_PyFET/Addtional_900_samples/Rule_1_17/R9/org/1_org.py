def process(match, repl):
    retVal = match.group(0)

    if not (conf.testParameter and match.group("name") not in (removePostHintPrefix(_) for _ in conf.testParameter)) and match.group("name") == match.group("name").strip('\\'):
        retVal = repl
        while True:
            _ = re.search(r"\\g<([^>]+)>", retVal)
            if _:
                retVal = retVal.replace(_.group(0), match.group(int(_.group(1)) if _.group(1).isdigit() else _.group(1)))
                break
        if kb.customInjectionMark in retVal:
            hintNames.append((retVal.split(kb.customInjectionMark)[0], match.group("name").strip('"\'') if kb.postHint == POST_HINT.JSON_LIKE else match.group("name")))

    return retVal