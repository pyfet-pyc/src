# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:07:36
# Size of source mod 2**32: 1703 bytes
from __future__ import unicode_literals
import re
from .common import InfoExtractor
from ..compat import compat_str
from ..utils import determine_ext, extract_attributes, ExtractorError, url_or_none, urlencode_postdata, urljoin

class AnimeOnDemandIE(InfoExtractor):
    _VALID_URL = 'https?://(?:www\\.)?anime-on-demand\\.de/anime/(?P<id>\\d+)'
    _LOGIN_URL = 'https://www.anime-on-demand.de/users/sign_in'
    _APPLY_HTML5_URL = 'https://www.anime-on-demand.de/html5apply'
    _NETRC_MACHINE = 'animeondemand'
    _GEO_COUNTRIES = [
     'AT', 'CH', 'DE', 'LI', 'LU']
    _TESTS = [
     {'url':'https://www.anime-on-demand.de/anime/161', 
      'info_dict':{'id':'161', 
       'title':'Grimgar, Ashes and Illusions (OmU)', 
       'description':'md5:6681ce3c07c7189d255ac6ab23812d31'}, 
      'playlist_mincount':4},
     {'url':'https://www.anime-on-demand.de/anime/39', 
      'only_matching':True},
     {'url':'https://www.anime-on-demand.de/anime/162', 
      'only_matching':True},
     {'url':'https://www.anime-on-demand.de/anime/169', 
      'only_matching':True},
     {'url':'https://www.anime-on-demand.de/anime/185', 
      'only_matching':True},
     {'url':'https://www.anime-on-demand.de/anime/12', 
      'only_matching':True}]
# okay decompiling testbed_py/test.py
