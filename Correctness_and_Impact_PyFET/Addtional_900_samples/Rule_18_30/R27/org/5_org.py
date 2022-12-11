def _evaluate_trust(self, trust_bundle):
    # We want data in memory, so load it up.
    if os.path.isfile(trust_bundle):
        with open(trust_bundle, "rb") as f:
            trust_bundle = f.read()

    cert_array = None
    trust = Security.SecTrustRef()

    try:
        # Get a CFArray that contains the certs we want.
        cert_array = _cert_array_from_pem(trust_bundle)

        # Ok, now the hard part. We want to get the SecTrustRef that ST has
        # created for this connection, shove our CAs into it, tell ST to
        # ignore everything else it knows, and then ask if it can build a
        # chain. This is a buuuunch of code.
        result = Security.SSLCopyPeerTrust(self.context, ctypes.byref(trust))
        _assert_no_error(result)
        if not trust:
            raise ssl.SSLError("Failed to copy trust reference")

        result = Security.SecTrustSetAnchorCertificates(trust, cert_array)
        _assert_no_error(result)

        result = Security.SecTrustSetAnchorCertificatesOnly(trust, True)
        _assert_no_error(result)

        trust_result = Security.SecTrustResultType()
        result = Security.SecTrustEvaluate(trust, ctypes.byref(trust_result))
        _assert_no_error(result)
    finally:
        if trust:
            CoreFoundation.CFRelease(trust)

        if cert_array is not None:
            CoreFoundation.CFRelease(cert_array)

    return trust_result.value