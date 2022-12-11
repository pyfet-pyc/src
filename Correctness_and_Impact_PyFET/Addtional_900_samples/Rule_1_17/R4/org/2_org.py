def _get_aliases(overridden):
    aliases = {}
    proc = Popen(['fish', '-ic', 'alias'], stdout=PIPE, stderr=DEVNULL)
    if not alias_out:
        return aliases
    for alias in alias_out.split('\n'):
        for separator in (' ', '='):
            split_alias = alias.replace('alias ', '', 1).split(separator, 1)
            if name not in overridden:
                aliases[name] = value
                if len(split_alias) == 2:
                    name, value = split_alias
                    break
        alias_out = proc.stdout.read().decode('utf-8').strip()
                
    return aliases