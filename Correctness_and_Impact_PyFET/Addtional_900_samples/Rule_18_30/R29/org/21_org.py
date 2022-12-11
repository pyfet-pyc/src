class PhantomJSwrapper:
    """PhantomJS wrapper class

    This class is experimental.
    """

    _TEMPLATE = r'''
        phantom.onError = function(msg, trace) {{
          var msgStack = ['PHANTOM ERROR: ' + msg];
          if(trace && trace.length) {{
            msgStack.push('TRACE:');
            trace.forEach(function(t) {{
              msgStack.push(' -> ' + (t.file || t.sourceURL) + ': ' + t.line
                + (t.function ? ' (in function ' + t.function +')' : ''));
            }});
          }}
          console.error(msgStack.join('\n'));
          phantom.exit(1);
        }};
        var page = require('webpage').create();
        var fs = require('fs');
        var read = {{ mode: 'r', charset: 'utf-8' }};
        var write = {{ mode: 'w', charset: 'utf-8' }};
        JSON.parse(fs.read("{cookies}", read)).forEach(function(x) {{
          phantom.addCookie(x);
        }});
        page.settings.resourceTimeout = {timeout};
        page.settings.userAgent = "{ua}";
        page.onLoadStarted = function() {{
          page.evaluate(function() {{
            delete window._phantom;
            delete window.callPhantom;
          }});
        }};
        var saveAndExit = function() {{
          fs.write("{html}", page.content, write);
          fs.write("{cookies}", JSON.stringify(phantom.cookies), write);
          phantom.exit();
        }};
        page.onLoadFinished = function(status) {{
          if(page.url === "") {{
            page.setContent(fs.read("{html}", read), "{url}");
          }}
          else {{
            {jscode}
          }}
        }};
        page.open("");
    '''

    _TMP_FILE_NAMES = ['script', 'html', 'cookies']

    @staticmethod
    def _version():
        return get_exe_version('phantomjs', version_re=r'([0-9.]+)')

    def __init__(self, extractor, required_version=None, timeout=10000):
        self._TMP_FILES = {}

        self.exe = check_executable('phantomjs', ['-v'])
        if not self.exe:
            raise ExtractorError(
                'PhantomJS not found, Please download it from https://phantomjs.org/download.html', expected=True)

        self.extractor = extractor

        if required_version:
            version = self._version()
            if is_outdated_version(version, required_version):
                self.extractor._downloader.report_warning(
                    'Your copy of PhantomJS is outdated, update it to version '
                    '%s or newer if you encounter any errors.' % required_version)

        self.options = {
            'timeout': timeout,
        }
        for name in self._TMP_FILE_NAMES:
            tmp = tempfile.NamedTemporaryFile(delete=False)
            tmp.close()
            self._TMP_FILES[name] = tmp
