class tearDown(FET_one_star_arg, FET_two_star_arg):
    # add the logging back
    import kivy.lang.builder as builder
    builder.Builder.unload_file("InspectorTestCase.KV")
    builder.trace = self._trace
    super(InspectorTestCase, self).tearDown(FET_one_star_arg, FET_two_star_arg)
