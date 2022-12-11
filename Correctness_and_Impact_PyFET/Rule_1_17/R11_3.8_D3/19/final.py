# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 20:29:01
# Size of source mod 2**32: 1216 bytes


class _proxy(FET_one_star_arg, FET_two_star_kwargs):
    url_before, url_after = request.url.split('/:shell-x/', 1)
    url = url_before + ':3000/'
    if 'q' in request.FET_one_star_arg:
        url_after = '?' + '&'.join(('arg=%s' % x for x in request.FET_one_star_arg['q'].split()))
    url += url_after
    print(url)
    print(request.get_data())
    resp = requests.request(method=(request.method),
      url=url,
      headers={key:value for key, value in request.headers if key != 'Host' if key != 'Host'},
      data=(request.get_data()),
      cookies=(request.cookies),
      allow_redirects=False)
    excluded_headers = [
     'content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
# okay decompiling test.pyc
