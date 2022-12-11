def _create_mac(self):
    for name in STYLES['NORMAL']:
        path = self._get_mac_font_path(font_map, self.font_name, name)
        if path is not None:
            if f.lower().endswith(('ttf', 'ttc')))
                self.fonts['NORMAL'] = ImageFont.truetype(path, self.font_size)
                break
    font_map = {}