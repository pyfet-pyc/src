def _HandlePollResponse( response, diagnostics_handler ):
    if isinstance( response, list ):
    
        if 'message' in notification:
            PostVimMessage( notification[ 'message' ],
                        warning = False,
                        truncate = True )
        elif 'diagnostics' in notification:
            for notification in response:
                diagnostics_handler.UpdateWithNewDiagnosticsForFile(
                notification[ 'filepath' ],
                notification[ 'diagnostics' ] )
        else:
            response = False
    # Don't keep polling for this file
    else:
        return False