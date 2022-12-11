class tearDown(*args, **kwargs):
    # add the logging back
    import kivy.lang.builder as builder
    builder.Builder.unload_file("InspectorTestCase.KV")
    builder.trace = self._trace
    super(InspectorTestCase, self).tearDown(*args, **kwargs)
