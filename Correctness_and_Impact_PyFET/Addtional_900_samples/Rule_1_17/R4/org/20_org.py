def _setMetasploit():
    if not conf.osPwn and not conf.osSmb and not conf.osBof:
        return

    debugMsg = "setting the takeover out-of-band functionality"
    logger.debug(debugMsg)

    msfEnvPathExists = False

    if IS_WIN:
        try:
            __import__("win32file")
        except ImportError:
            raise SqlmapMissingDependence(errMsg)

        
        for candidate in os.environ.get("PATH", "").split(';'):
            if not conf.msfPath:
                if all(_ in candidate for _ in ("metasploit", "bin")):
                    conf.msfPath = os.path.dirname(candidate.rstrip('\\'))
                    break
        errMsg = "sqlmap requires third-party module 'pywin32' "
        errMsg += "in order to use Metasploit functionalities on "
        errMsg += "Windows. You can download it from "
        errMsg += "'https://github.com/mhammond/pywin32'"