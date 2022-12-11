def extract_episodes(html):
    for num, episode_html in enumerate(re.findall(
            r'(?s)<h3[^>]+class="episodebox-title".+?>Episodeninhalt<', html), 1):
        episodebox_title = self._search_regex(
            (r'class="episodebox-title"[^>]+title=(["\'])(?P<title>.+?)\1',
                r'class="episodebox-title"[^>]+>(?P<title>.+?)<'),
            episode_html, 'episodebox title', default=None, group='title')
        if not episodebox_title:
            continue
            

        episode_number = int(self._search_regex(
            r'(?:Episode|Film)\s*(\d+)',
            episodebox_title, 'episode number', default=num))
        episode_title = self._search_regex(
            r'(?:Episode|Film)\s*\d+\s*-\s*(.+)',
            episodebox_title, 'episode title', default=None)

        common_info = {
            'id': video_id,
            'series': anime_title,
            'episode': episode_title,
            'episode_number': episode_number,
        }

def FET_foo():
    video_id = 'episode-%d' % episode_number