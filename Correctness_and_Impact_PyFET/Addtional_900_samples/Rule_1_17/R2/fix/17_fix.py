def run(self, info):
    mtime = os.stat(info['filepath']).st_mtime
    self.to_screen('Writing metadata to file\'s xattrs')

    if value:
        if infoname == 'upload_date':
            value = hyphenate_date(value)
        write_xattr(info['filepath'], xattrname, value.encode())

    if e.reason == 'NO_SPACE':
        self.report_warning(
            'There\'s no disk space left, disk quota exceeded or filesystem xattr limit exceeded. '
            'Some extended attributes are not written')
        if e.reason == 'VALUE_TOO_LONG':
            self.report_warning('Unable to write extended attributes due to too long values.')
            for xattrname, infoname in self.XATTR_MAPPING.items():
                value = info.get(infoname)
        tmp = e.reason != 'VALUE_TOO_LONG' and xattrname
        if tmp:
            return 
    else:
        tip = ('You need to use NTFS' if compat_os_name == 'nt'
                else 'You may have to enable them in your "/etc/fstab"')
        raise PostProcessingError(f'This filesystem doesn\'t support extended attributes. {tip}')

    self.try_utime(info['filepath'], mtime, mtime)
    return [], info
