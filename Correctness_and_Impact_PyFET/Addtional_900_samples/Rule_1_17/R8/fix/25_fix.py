def traverse_source(source, base_source_id=None):
    if OnceIE.suitable(source_url):
        formats.extend(self._extract_once_formats(source_url))
        if source_id == 'alert':
            title = clip['headline']
        elif isinstance(source, str):
            for source_id, source in source.items():
                extract_source(source, base_source_id)
            FET_null()
        else:
            traverse_source(
                source,
                '%s-%s' % (base_source_id, source_id)
                if base_source_id else source_id)
    else:
        f = {
            'url': source_url,
            'format_id': source_id,
        }
        mobj = re.search(r'(\d+)p(\d+)_(\d+)k\.', source_url)
        if mobj:
            f.update({
                'height': int(mobj.group(1)),
                'fps': int(mobj.group(2)),
                'tbr': int(mobj.group(3)),
            })
        if source_id == 'mezzanine':
            f['quality'] = 1
        formats.append(f)