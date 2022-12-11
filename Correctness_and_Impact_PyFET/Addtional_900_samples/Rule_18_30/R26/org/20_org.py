def _wrap_full(self, inner, outfile):
    if self.cssfile:
        if os.path.isabs(self.cssfile):
            # it's an absolute filename
            cssfilename = self.cssfile
        else:
            try:
                filename = outfile.name
                if not filename or filename[0] == '<':
                    # pseudo files, e.g. name == '<fdopen>'
                    raise AttributeError
                cssfilename = os.path.join(os.path.dirname(filename),
                                            self.cssfile)
            except AttributeError:
                print('Note: Cannot determine output file name, '
                        'using current directory as base for the CSS file name',
                        file=sys.stderr)
                cssfilename = self.cssfile
        # write CSS file only if noclobber_cssfile isn't given as an option.
        try:
            if not os.path.exists(cssfilename) or not self.noclobber_cssfile:
                with open(cssfilename, "w") as cf:
                    cf.write(CSSFILE_TEMPLATE %
                                {'styledefs': self.get_style_defs('body')})
        except OSError as err:
            err.strerror = 'Error writing CSS file: ' + err.strerror
            raise

        yield 0, (DOC_HEADER_EXTERNALCSS %
                    dict(title=self.title,
                        cssfile=self.cssfile,
                        encoding=self.encoding))
    else:
        yield 0, (DOC_HEADER %
                    dict(title=self.title,
                        styledefs=self.get_style_defs('body'),
                        encoding=self.encoding))

    yield from inner
    yield 0, DOC_FOOTER