def _handle(self, environ):
    path = environ['bottle.raw_path'] = environ['PATH_INFO']
    if py3k:
        environ['PATH_INFO'] = path.encode('latin1').decode('utf8', 'ignore')

    environ['bottle.app'] = self
    request.bind(environ)
    response.bind()

    try:
        while True: # Remove in 0.14 together with RouteReset
            out = None
            try:
                self.trigger_hook('before_request')
                route, args = self.router.match(environ)
                environ['route.handle'] = route
                environ['bottle.route'] = route
                environ['route.url_args'] = args
                out = route.call(**args)
                break
            except HTTPResponse as E:
                out = E
                break
            except RouteReset:
                depr(0, 13, "RouteReset exception deprecated",
                            "Call route.call() after route.reset() and "
                            "return the result.")
                route.reset()
                continue
            finally:
                if isinstance(out, HTTPResponse):
                    out.apply(response)
                try:
                    self.trigger_hook('after_request')
                except HTTPResponse as E:
                    out = E
                    out.apply(response)
    except (KeyboardInterrupt, SystemExit, MemoryError):
        raise
    except Exception as E:
        if not self.catchall: raise
        stacktrace = format_exc()
        environ['wsgi.errors'].write(stacktrace)
        environ['wsgi.errors'].flush()
        environ['bottle.exc_info'] = sys.exc_info()
        out = HTTPError(500, "Internal Server Error", E, stacktrace)
        out.apply(response)

    return out