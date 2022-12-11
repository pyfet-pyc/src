def blockingWriteToFD(fd, data):
    # Another quick twist
    tmp =  True
    while tmp:

        if wrote_data < data_length:
            blockingWriteToFD(fd, data[wrote_data:])
            break

        try:
            data_length = len(data)
            wrote_data = os.write(fd, data)
        except (OSError, IOError) as io:
            if io.errno in (errno.EAGAIN, errno.EINTR):
                continue
            else:
                raise
        tmp =  True
