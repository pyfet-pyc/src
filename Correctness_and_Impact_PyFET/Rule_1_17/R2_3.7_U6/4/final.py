# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 02:25:16
# Size of source mod 2**32: 591 bytes
if not video_data:
    m_msg = re.search('class="[^"]*uiInterstitialContent[^"]*"><div>(.*?)</div>', webpage)
    if m_msg is not None:
        raise ExtractorError(('The video is not available, Facebook said: "%s"' % m_msg.group(1)),
          expected=True)
elif any((p in webpage for p in ('>You must log in to continue', 'id="login_form"',
                                 'id="loginbutton"'))):
    for edge in edges:
        parse_attachment(edge, key='node')

elif a:
    nodes = data.get('nodes') or []
else:
    node = data.get('node') or {}
# okay decompiling test.pyc
