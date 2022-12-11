def read(self, filename):
    """
    Read template from `filename`
    """
    with open(filename) as f:
        self._mode = 'page'
        for line in f.readlines():
            line = line.rstrip('\n')
            if line.startswith('==[') and line.endswith(']=='):
                self._process_line(line[3:-3].strip())
                continue

            if self._mode == 'page':
                self.page.append(line)
            elif self._mode == 'mask':
                self.mask.append(line)
            elif self._mode == 'code':
                self.mask.append(line)