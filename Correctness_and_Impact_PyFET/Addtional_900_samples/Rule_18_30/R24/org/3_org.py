def chrome_args(**options) -> List[str]:
    """helper to build up a chrome shell command with arguments"""

    from .config import CHROME_OPTIONS

    options = {**CHROME_OPTIONS, **options}

    if not options['CHROME_BINARY']:
        raise Exception('Could not find any CHROME_BINARY installed on your system')

    cmd_args = [options['CHROME_BINARY']]

    if options['CHROME_HEADLESS']:
        cmd_args += ('--headless',)
    
    if not options['CHROME_SANDBOX']:
        # assume this means we are running inside a docker container
        # in docker, GPU support is limited, sandboxing is unecessary, 
        # and SHM is limited to 64MB by default (which is too low to be usable).
        cmd_args += (
            '--no-sandbox',
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--disable-software-rasterizer',
            '--run-all-compositor-stages-before-draw',
            '--hide-scrollbars',
            '--single-process',
            '--no-zygote',
        )


    if not options['CHECK_SSL_VALIDITY']:
        cmd_args += ('--disable-web-security', '--ignore-certificate-errors')

    if options['CHROME_USER_AGENT']:
        cmd_args += ('--user-agent={}'.format(options['CHROME_USER_AGENT']),)

    if options['RESOLUTION']:
        cmd_args += ('--window-size={}'.format(options['RESOLUTION']),)

    if options['TIMEOUT']:
        cmd_args += ('--timeout={}'.format(options['TIMEOUT'] * 1000),)

    if options['CHROME_USER_DATA_DIR']:
        cmd_args.append('--user-data-dir={}'.format(options['CHROME_USER_DATA_DIR']))
    
    return cmd_args