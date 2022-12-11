def _check_ocsp_openssl_bin(self, cert_path: str, chain_path: str,
                            host: str, url: str, timeout: int) -> bool:
    # Minimal implementation of proxy selection logic as seen in, e.g., cURL
    # Some things that won't work, but may well be in use somewhere:
    # - username and password for proxy authentication
    # - proxies accepting TLS connections
    # - proxy exclusion through NO_PROXY
    env_http_proxy = getenv('http_proxy')
    env_HTTP_PROXY = getenv('HTTP_PROXY')
    proxy_host = None
    if env_http_proxy is not None or env_HTTP_PROXY is not None:
        proxy_host = env_http_proxy if env_http_proxy is not None else env_HTTP_PROXY
    if proxy_host is None:
        url_opts = ["-url", url]
    else:
        if proxy_host.startswith('http://'):
            proxy_host = proxy_host[len('http://'):]
        url_opts = ["-host", proxy_host, "-path", url]
    # jdkasten thanks "Bulletproof SSL and TLS - Ivan Ristic" for documenting this!
    cmd = ["openssl", "ocsp",
            "-no_nonce",
            "-issuer", chain_path,
            "-cert", cert_path,
            "-CAfile", chain_path,
            "-verify_other", chain_path,
            "-trust_other",
            "-timeout", str(timeout),
            "-header"] + self.host_args(host) + url_opts
    logger.debug("Querying OCSP for %s", cert_path)
    logger.debug(" ".join(cmd))
    try:
        output, err = util.run_script(cmd, log=logger.debug)
    except errors.SubprocessError:
        logger.info("OCSP check failed for %s (are we offline?)", cert_path)
        return False
    return _translate_ocsp_query(cert_path, output, err)
