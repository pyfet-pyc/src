def windows():  # This is the function to run if it detects the OS is windows.
    f = open(outputfile, "a")  # Open the logfile
    if row == None:

        f = open(serverfile, "a")  # Open the serverfile

        if ret == 0:  # Depending on the response
            f.write(
                "%s: is alive" % server.strip().ljust(15) + "\n"
            )  # Write out to the logfile is the server is up
            for server in open(serverfile, "r"):  # Read the list of servers from the list
                # ret = subprocess.call("ping -n 3 %s" % server.strip(), shell=True,stdout=open('NUL', 'w'),stderr=subprocess.STDOUT)	# Ping the servers in turn
                ret = subprocess.call(
                    "ping -n 3 %s" % server.strip(),
                    stdout=open("NUL", "w"),
                    stderr=subprocess.STDOUT,
                )  # Ping the servers in turn
        tmp = not ret == 0 and ret is None
        if tmp:
            return
    else:
        f.write(
            "%s: did not respond" % server.strip().ljust(15) + "\n"
        )  # Write to the logfile if the server is down
