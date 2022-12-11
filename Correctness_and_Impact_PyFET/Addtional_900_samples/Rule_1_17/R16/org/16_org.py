def ToggleLogs( self, size, mods, *filenames ):
    logfiles = self.GetLogfiles()
    if not filenames:
      sorted_logfiles = sorted( logfiles )
    try:
        logfile_index = vimsupport.SelectFromList(
        'Which logfile do you wish to open (or close if already open)?',
        sorted_logfiles )
    except RuntimeError as e:
        vimsupport.PostVimMessage( str( e ) )
        return

    logfile = logfiles[ sorted_logfiles[ logfile_index ] ]
 