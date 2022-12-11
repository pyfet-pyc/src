# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/application.py
# Compiled at: 2022-08-11 21:44:29
# Size of source mod 2**32: 863 bytes


def __init__(self, _data, _subtype='octet-stream', _encoder=encoders.encode_base64, *, policy=None, **_params):
    """Create an application/* type MIME document.

    _data is a string containing the raw application data.

    _subtype is the MIME content type subtype, defaulting to
    'octet-stream'.

    _encoder is a function which will perform the actual encoding for
    transport of the application data, defaulting to base64 encoding.

    Any additional keyword arguments are passed to the base class
    constructor, which turns them into parameters on the Content-Type
    header.
    """
    if _subtype:
        raise TypeError('Invalid application MIME subtype')
    (MIMENonMultipart.__init__)(self, 'application', _subtype, policy=policy, **_params)
    self.set_payload(_data)
    _encoder(self)
# okay decompiling testbed_py/application.py
