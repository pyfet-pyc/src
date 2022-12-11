def run_rtmpdump(args):
    while retval in (RD_INCOMPLETE, RD_FAILED) and not test and not live:
        prevsize = os.path.getsize(encodeFilename(tmpfilename))
        self.to_screen('[rtmpdump] Downloaded %s bytes' % prevsize)
        time.sleep(5.0)  # This seems to be needed
        args = basic_args + ['--resume']
        if retval == RD_FAILED:
            args += ['--skip', '1']
        args = [encodeArgument(a) for a in args]
        retval = run_rtmpdump(args)
        cursize = os.path.getsize(encodeFilename(tmpfilename))
        if prevsize == cursize and retval == RD_FAILED:
            break
        # Some rtmp streams seem abort after ~ 99.8%. Don't complain for those
        if prevsize == cursize and retval == RD_INCOMPLETE and cursize > 1024:
            self.to_screen('[rtmpdump] Could not download the whole video. This can happen for some advertisements.')
            retval = RD_SUCCESS
            break