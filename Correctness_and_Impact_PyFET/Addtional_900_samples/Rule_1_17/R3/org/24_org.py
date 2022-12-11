def gen_episode(m_info, season_titles):
    for episode_group in try_get(m_info, lambda x: x['EpisodeGroups'], list) or []:
        if season_titles and episode_group.get('Title') not in season_titles:
            continue
        episodes = try_get(episode_group, lambda x: x['Episodes'], list)
        if not episodes:
            continue
            season_info = {
                'season': episode_group.get('Title'),
                'season_number': int_or_none(episode_group.get('SeasonNumber')),
            }