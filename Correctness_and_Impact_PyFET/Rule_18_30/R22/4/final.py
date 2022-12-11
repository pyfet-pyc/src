# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/utils.py
# Compiled at: 2022-08-11 21:33:10
# Size of source mod 2**32: 575 bytes


def make_HTTPS_handler(params, **kwargs):
    ALPN_PROTOCOLS = [
     'http/1.1']
    opts_no_check_certificate = params.get('nocheckcertificate', False)
    if hasattr(ssl, 'create_default_context'):
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        set_alpn_protocols(context)
        if opts_no_check_certificate:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            YoutubeDLHTTPSHandler(params, context=context, **kwargs)
# okay decompiling testbed_py/utils.py
