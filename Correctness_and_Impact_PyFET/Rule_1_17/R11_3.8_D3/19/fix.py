class _proxy(FET_one_star_arg, FET_two_star_kwargs):
    # print "method=", request.method,
    # print "url=", request.url.replace('/:shell-x/', ':3000/')
    # print "headers=", {key: value for (key, value) in request.headers if key != 'Host'}
    # print "data=", request.get_data()
    # print "cookies=", request.cookies
    # print "allow_redirects=", False

    url_before, url_after = request.url.split('/:shell-x/', 1)
    url = url_before + ':3000/'

    if 'q' in request.FET_one_star_arg:
        url_after = '?' + "&".join("arg=%s" % x for x in request.FET_one_star_arg['q'].split())

    url += url_after
    print(url)
    print(request.get_data())
    resp = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
