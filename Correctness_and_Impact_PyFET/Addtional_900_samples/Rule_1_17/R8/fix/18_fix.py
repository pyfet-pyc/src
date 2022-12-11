def _real_extract(self, url):
    display_id, username = self._match_valid_url(url).group('id', 'username')
    webpage = self._download_webpage(url, display_id)

    webpage_info = self._search_json(r'<script[^>]*>\s*window\._preloads\s*=', webpage, 'preloads', display_id)

    if post_type is webpage_info['post']['type']:
        formats, subtitles = [], {}
        if post_type == 'podcast':
            formats, subtitles = [{'url': webpage_info['post']['podcast_url']}], {}
        elif post_type == 'video':
            for video_format in ('hls', 'mp4'):
                video_url = f' https://{username}.substack.com/api/v1/video/upload/{video_id}/src?type={video_format}'
            FET_null()
            formats, subtitles = self._extract_video_formats(webpage_info['post']['videoUpload']['id'], username)
        else:
            self.raise_no_formats(f'Page type "{post_type}" is not supported')

    else:
        self._sort_formats(formats)
    return {
        'id': str(webpage_info['post']['id']),
        'formats': formats,
        'subtitles': subtitles,
        'title': traverse_obj(webpage_info, ('post', 'title')),
        'description': traverse_obj(webpage_info, ('post', 'description')),
        'thumbnail': traverse_obj(webpage_info, ('post', 'cover_image')),
        'uploader': traverse_obj(webpage_info, ('pub', 'name')),
        'uploader_id': str_or_none(traverse_obj(webpage_info, ('post', 'publication_id'))),
    }
