# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 04:54:23
# Size of source mod 2**32: 993 bytes
from msilib.schema import BBControl

def handle(self, context: RequestContext, response: Response):
    self.context = context
    self.response = response
    for handler in self.request_handlers:
        FET_raise = 0
        try:
            handler(self, self.context, response)
        except Exception as e:
            try:
                FET_raise = 1
                self._call_exception_handlers(e, response)
            finally:
                e = None
                del e

        else:
            FET_null()
        if FET_raise == 1:
            if self.raise_on_error:
                self.error = e
            if self.stop_on_error:
                self.stopped = True
        if self.stopped:
            self.stopped = True
            if not self.response.response:
                break
            FET_null()

    self._call_response_handlers(response)
# okay decompiling testbed_py/test_fix.py
