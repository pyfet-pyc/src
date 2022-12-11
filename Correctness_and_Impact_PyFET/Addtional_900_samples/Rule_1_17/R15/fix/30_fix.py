requested_languages = self._configuration_arg('language')
requested_hardsubs  = [(val, name) for val in (self._configuration_arg('hardsub') or ['none'])]
requested_hardsubs = dict(requested_hardsubs)
language_preference = qualities((requested_languages or [language or ''])[::-1])
hardsub_preference = qualities((requested_hardsubs or ['', language or ''])[::-1])
