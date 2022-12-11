# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:20:28
# Size of source mod 2**32: 1655 bytes
from __future__ import unicode_literals
import re
from uuid import uuid4
from .common import InfoExtractor
import compat.common as cherr
import compat.common as cstr
from ..utils import ExtractorError, int_or_none, try_get, url_or_none, urlencode_postdata

class ZattooPlatformBaseIE(InfoExtractor):
    _power_guide_hash = None

    def _host_url(self):
        return 'https://%s' % (self._API_HOST if hasattr(self, '_API_HOST') else self._HOST)

    def _login(self):
        username, password = self._get_login_info()
        if not (username and password):
            self.raise_login_required('A valid %s account is needed to access this media.' % self._NETRC_MACHINE)
        try:
            data = self._download_json(('%s/zapi/v2/account/login' % self._host_url()),
              None, 'Logging in', data=(urlencode_postdata({'login':username, 
             'password':password, 
             'remember':'true'})),
              headers={'Referer':'%s/login' % self._host_url(), 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'})
        except ExtractorError:
            if isinstance(cause, compat_HTTPError):
                if cause.code == 400:
                    raise ExtractorError('Unable to login: incorrect username and/or password',
                      expected=True)
            raise

        self._power_guide_hash = data['session']['power_guide_hash']
# okay decompiling testbed_py/test_fix.py
