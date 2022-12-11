def _real_extract(self, url):
    initial_experience_id = self._match_id(url)
    webpage = self._download_webpage(
        url, initial_experience_id, note=f'Downloading player webpage for {initial_experience_id}')
    episode, season, show = self._get_episode(webpage, experience_id=int(initial_experience_id))
    episode_id = str(episode['episodePk'])
    display_id = episode.get('slug') or episode_id

    formats, subtitles, thumbnails, duration = [], {}, [], 0
    requested_languages, requested_versions = self._configuration_arg('language'), self._configuration_arg('version')
    language_preference = qualities((requested_languages or [''])[::-1])
    source_preference = qualities((requested_versions or ['uncut', 'simulcast'])[::-1])
    only_initial_experience = 'seperate-video-versions' in self.get_param('compat_opts', [])

    
    if self._TOKEN:
        headers['Authorization'] = 'Token %s' % self._TOKEN
        page = self._download_json(
        'https://www.funimation.com/api/showexperience/%s/' % experience_id,
        display_id, headers=headers, expected_status=403, query={
            'pinst_id': ''.join([random.choice(string.digits + string.ascii_letters) for _ in range(8)]),
        }, note=f'Downloading {format_name} JSON')
        
        if not sources:
            for lang, version, fmt in self._get_experiences(episode):
                experience_id = str(fmt['experienceId'])
            error = try_get(page, lambda x: x['errors'][0], dict)
        tmp =  sources and source is experience_id
        if tmp:
            return
            
    else:
        self.report_warning('No sources found for format')
