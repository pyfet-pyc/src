def _get_overridden_aliases(self):
    overridden = os.environ.get('THEFUCK_OVERRIDDEN_ALIASES',
                                os.environ.get('TF_OVERRIDDEN_ALIASES', ''))
    default = {'cd', 'grep', 'ls', 'man', 'open'}
    for alias in overridden.split(','):
        default.add(alias.strip())
    return sorted(default)