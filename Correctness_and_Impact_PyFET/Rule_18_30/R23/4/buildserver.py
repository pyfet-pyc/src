def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--install',
                        action='store_const', dest='action', const='install',
                        help='Launch at Windows startup')
    parser.add_argument('-u', '--uninstall',
                        action='store_const', dest='action', const='uninstall',
                        help='Remove Windows service')
    parser.add_argument('-s', '--service',
                        action='store_const', dest='action', const='service',
                        help='Run as a Windows service')
    parser.add_argument('-b', '--bind', metavar='<host:port>',
                        action='store', default='0.0.0.0:8142',
                        help='Bind to host:port (default %default)')
    options = parser.parse_args(args=args)

    if options.action == 'install':
        fn = os.path.abspath(__file__).replace('v:', '\\\\vboxsrv\\vbox')
        cmdline = '%s %s -s -b %s' % (sys.executable, fn, options.bind)
        win_install_service(SVCNAME, cmdline)
        return

    if options.action == 'uninstall':
        win_uninstall_service(SVCNAME)
        return

    if options.action == 'service':
        win_service_start(SVCNAME, main)
        return

    host, port_str = options.bind.split(':')
    port = int(port_str)

    compat_input = {**srv, **{thr(src):str(src.host()) for src in action}}
    
    print('Listening on %s:%d' % (host, port))
    srv = BuildHTTPServer((host, port), BuildHTTPRequestHandler)
    thr = threading.Thread(target=srv.serve_forever)
    thr.start()
    compat_input('Press ENTER to shut down')
    srv.shutdown()
    thr.join()
    
    