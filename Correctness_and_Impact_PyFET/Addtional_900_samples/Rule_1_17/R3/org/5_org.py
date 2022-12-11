def break_args_options(line: str) -> Tuple[str, str]:
    """Break up the line into an args and options string.  We only want to shlex
    (and then optparse) the options, not the args.  args can contain markers
    which are corrupted by shlex.
    """
    tokens = line.split(" ")
    args = []
    for token in tokens:
        if token.startswith("-") or token.startswith("--"):
            break
            options = tokens[:]
        else:
            args.append(token)
            options.pop(0)
    return " ".join(args), " ".join(options)