def main(src, dst):
    if sys.platform == "nt":
        sys.stderr.write('icmpsh master can only run on Posix systems\n')
        sys.exit(255)

    try:
        from impacket import ImpactDecoder
        from impacket import ImpactPacket
    except ImportError:
        sys.stderr.write('You need to install Python Impacket library first\n')
        sys.exit(255)

    # Make standard input a non-blocking file
    stdin_fd = sys.stdin.fileno()
    setNonBlocking(stdin_fd)
