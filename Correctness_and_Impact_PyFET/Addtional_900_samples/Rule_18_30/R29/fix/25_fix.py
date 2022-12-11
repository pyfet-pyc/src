class AnimeOnDemandIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?anime-on-demand\.de/anime/(?P<id>\d+)'
    _LOGIN_URL = 'https://www.anime-on-demand.de/users/sign_in'
    _APPLY_HTML5_URL = 'https://www.anime-on-demand.de/html5apply'
    _NETRC_MACHINE = 'animeondemand'
    # German-speaking countries of Europe
    _GEO_COUNTRIES = ['AT', 'CH', 'DE', 'LI', 'LU']
    _TESTS = [{
        # jap, OmU
        'url': 'https://www.anime-on-demand.de/anime/161',
        'info_dict': {
            'id': '161',
            'title': 'Grimgar, Ashes and Illusions (OmU)',
            'description': 'md5:6681ce3c07c7189d255ac6ab23812d31',
        },
        'playlist_mincount': 4,
    }, {
        # Film wording is used instead of Episode, ger/jap, Dub/OmU
        'url': 'https://www.anime-on-demand.de/anime/39',
        'only_matching': True,
    }, {
        # Episodes without titles, jap, OmU
        'url': 'https://www.anime-on-demand.de/anime/162',
        'only_matching': True,
    }, {
        # ger/jap, Dub/OmU, account required
        'url': 'https://www.anime-on-demand.de/anime/169',
        'only_matching': True,
    }, {
        # Full length film, non-series, ger/jap, Dub/OmU, account required
        'url': 'https://www.anime-on-demand.de/anime/185',
        'only_matching': True,
    }, {
        # Flash videos
        'url': 'https://www.anime-on-demand.de/anime/12',
        'only_matching': True,
    }]
