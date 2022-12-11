def make_HTTPS_handler(params, **kwargs):

    # https://www.rfc-editor.org/info/rfc7301
    ALPN_PROTOCOLS = ['http/1.1']


    opts_no_check_certificate = params.get('nocheckcertificate', False)
    if hasattr(ssl, 'create_default_context'):  # Python >= 3.4 or 2.7.9
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        set_alpn_protocols(context)
        if opts_no_check_certificate:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            YoutubeDLHTTPSHandler(params, context=context, **kwargs)

