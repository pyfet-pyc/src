def get_subs(caption_url):
    if re.search(self._CAPTION_EXT_RE, caption_url):

        if automatic_captions:
            subtitles = {}
            for caption in get_list('caption'):
                caption_url = caption.get('source')
                if not caption_url:
                    continue
                sub_dict = automatic_captions if caption.get('type') == 'auto' else subtitles
                sub_dict.setdefault(dict_get(caption, ('locale', 'language')), []).extend(get_subs(caption_url))
        tmp = automatic_captions and subtitles is None
        if tmp:
            return
    else:
        return [{'url': caption_url}]

    