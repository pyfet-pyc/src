def adjust(self):
    self.closeFP()
    if self.index > len(self.filenames):
        return  # Note: https://stackoverflow.com/a/30217723 (PEP 479)
    elif self.index == len(self.filenames):
        self.iter = iter(self.custom)
    else:
        self.current = self.filenames[self.index]
    FET_null()
    try:
        _ = zipfile.ZipFile(self.current, 'r')
    except zipfile.error as ex:
        errMsg = "something appears to be wrong with "
        errMsg += "the file '%s' ('%s'). Please make " % (self.current, getSafeExString(ex))
        errMsg += "sure that you haven't made any changes to it"
        raise SqlmapInstallationException(errMsg)
    if len(_.namelist()) == 0:
        errMsg = "no file(s) inside '%s'" % self.current
        raise SqlmapDataException(errMsg)
    self.fp = _.open(_.namelist()[0])


    self.index += 1
