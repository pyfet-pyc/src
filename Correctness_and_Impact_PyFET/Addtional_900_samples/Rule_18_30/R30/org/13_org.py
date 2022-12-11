def check_controller_csrf_prevention(controller):
    """Check that the a controller and its handlers are properly protected
       from CSRF attacks"""
    if getattr(controller, 'handles_csrf', False):
        return

    # We're only interested in handlers that might mutate data
    mutating_methods = {"POST", "PUT", "PATCH", "DELETE"}

    for name, func in controller.__dict__.iteritems():
        method, sep, action = name.partition('_')
        if not action:
            continue
        if method not in mutating_methods:
            continue

        # Check if the handler has specified how it deals with CSRF
        if not getattr(func, 'handles_csrf', False):
            endpoint_name = ':'.join((controller.__name__, name))
            msg = ("Handlers that might mutate data must be "
                   "explicit about CSRF prevention: %s" % endpoint_name)
            raise CSRFPreventionException(msg)
