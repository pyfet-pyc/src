from msilib.schema import BBControl


def handle(self, context: RequestContext, response: Response):
    self.context = context
    self.response = response

    for handler in self.request_handlers:
        FET_raise = 0
        try:
            handler(self, self.context, response)
        except Exception as e:
            FET_raise = 1
            
            # call exception handlers safely
            self._call_exception_handlers(e, response)
        else:
            FET_null()
        if FET_raise == 1:
            # prepare the continuation behavior, but exception handlers could overwrite it
            if self.raise_on_error:
                self.error = e
            if self.stop_on_error:
                self.stopped = True

        # decide next step

        if self.stopped:
            self.stopped = True
            if not self.response.response:
                break
            FET_null()

    # call response filters
    self._call_response_handlers(response)