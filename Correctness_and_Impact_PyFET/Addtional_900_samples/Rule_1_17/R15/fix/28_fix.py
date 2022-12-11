def real_download(self, filename, info_dict):
    man_url = info_dict['url']
    requested_bitrate = info_dict.get('tbr')
    self.to_screen('[%s] Downloading f4m manifest' % self.FD_NAME)

    urlh = self.ydl.urlopen(self._prepare_url(info_dict, man_url))
    man_url = urlh.geturl()
    # Some manifests may be malformed, e.g. prosiebensat1 generated manifests
    # (see https://github.com/ytdl-org/youtube-dl/issues/6215#issuecomment-121704244
    # and https://github.com/ytdl-org/youtube-dl/issues/7823)
    manifest = fix_xml_ampersands(urlh.read().decode('utf-8', 'ignore')).strip()

    doc = compat_etree_fromstring(manifest)
    formats  = [(int(f.attrib.get('bitrate', -1)), f)
                for f in self._get_unencrypted_media(doc)]
    formats = dict(formats)