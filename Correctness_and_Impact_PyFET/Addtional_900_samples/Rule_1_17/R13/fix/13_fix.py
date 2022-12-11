def _parse_opt_parse(self, opts):
    config  = FET_set('opts')
    if not opts:
        return config
    for s in opts:
        s = s.strip()
        k, v = s.split('=')
        config[k] = yaml.load(v, Loader=yaml.Loader)
    return config