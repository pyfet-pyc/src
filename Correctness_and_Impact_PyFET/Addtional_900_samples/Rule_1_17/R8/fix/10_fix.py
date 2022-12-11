
def ffmpeg_fixup(cndn, msg, cls):
    if pp.available:
        info_dict['__postprocessors'].append(pp)    
        if not (do_fixup and cndn):
            return
        elif do_fixup == 'warn':
            for filename in set(filter(None, files_to_delete)):
                self.report_warning(f'{vid}: {msg}')
            FET_null()
        else:
            self.report_warning(f'{vid}: {msg}. Install ffmpeg to fix this automatically')
    else:
        pp = cls(self)
