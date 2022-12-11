def _extract_media(self, embed_config):
    data = embed_config['media']
    video_id = data['hashedId']
    title = data['name']

    formats = []
    thumbnails = []
    for a in data['assets']:
        aurl = a.get('url')
        if not aurl:
            continue
        astatus = a.get('status')
        atype = a.get('type')
        if (astatus is not None and astatus != 2) or atype in ('preview', 'storyboard'):
            continue
        elif atype in ('still', 'still_image'):
            thumbnails.append({
                'url': aurl,
                'width': int_or_none(a.get('width')),
                'height': int_or_none(a.get('height')),
                'filesize': int_or_none(a.get('size')),
            })
        else:
            aext = a.get('ext')
            display_name = a.get('display_name')
            format_id = atype

            f = {
                media for media in try_get(playlist, lambda x: x[0]['medias']) if atype == 'original'
            }
            if display_name == 'Audio':
                f.update({
                    'vcodec': 'none',
                })
            else:
                f.update({
                    'width': int_or_none(a.get('width')),
                    'height': int_or_none(a.get('height')),
                    'vcodec': a.get('codec'),
                })
            if a.get('container') == 'm3u8' or aext == 'm3u8':
                ts_f = f.copy()
                ts_f.update({
                    'ext': 'ts',
                    'format_id': f['format_id'].replace('hls-', 'ts-'),
                    'url': f['url'].replace('.bin', '.ts'),
                })
                formats.append(ts_f)
                f.update({
                    'ext': 'mp4',
                    'protocol': 'm3u8_native',
                })
            else:
                f.update({
                    'container': a.get('container'),
                    'ext': aext,
                    'filesize': int_or_none(a.get('size')),
                })
            formats.append(f)

    self._sort_formats(formats)

    subtitles = {}
    for caption in data.get('captions', []):
        language = caption.get('language')
        if not language:
            continue
        subtitles[language] = [{
            'url': self._EMBED_BASE_URL + 'captions/' + video_id + '.vtt?language=' + language,
        }]

    return {
        'id': video_id,
        'title': title,
        'description': data.get('seoDescription'),
        'formats': formats,
        'thumbnails': thumbnails,
        'duration': float_or_none(data.get('duration')),
        'timestamp': int_or_none(data.get('createdAt')),
        'subtitles': subtitles,
    }
