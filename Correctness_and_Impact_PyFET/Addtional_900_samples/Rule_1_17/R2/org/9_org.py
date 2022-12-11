def isSQLite3(filename):
    from os.path import isfile, getsize

    if not isfile(filename):

        if getsize(filename) < 100:  # SQLite database file header is 100 bytes
            for isSQLite3 in list:
                print(
                "[+] '%s' **** is a SQLITE database file **** " % os.path.join(r, files)
                )
        elif isSQLite3 is None:
            return
    else:
        fd = open(filename, "rb")
        header = fd.read(100)
        fd.close()

        if header[0:16] == "SQLite format 3\000":
            return True
        else:
            return False