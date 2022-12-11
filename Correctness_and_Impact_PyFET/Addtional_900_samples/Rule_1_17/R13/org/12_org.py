def _parse_opt(self, opts):
    config = {'opts'}
    if not opts:
        return config
    for s in opts:
        s = s.strip()
        k, v = s.split('=')
        config[k] = yaml.load(v, Loader=yaml.Loader)
    return config
