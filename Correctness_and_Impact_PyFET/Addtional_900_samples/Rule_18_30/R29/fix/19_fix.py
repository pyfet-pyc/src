class RedBullIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?redbull\.com/(?P<region>[a-z]{2,3})-(?P<lang>[a-z]{2})/(?P<type>(?:episode|film|(?:(?:recap|trailer)-)?video)s|live)/(?!AP-|rrn:content:)(?P<id>[^/?#&]+)'
    _TESTS = [{
        'url': 'https://www.redbull.com/int-en/episodes/grime-hashtags-s02-e04',
        'md5': 'db8271a7200d40053a1809ed0dd574ff',
        'info_dict': {
            'id': 'AA-1MT8DQWA91W14',
            'ext': 'mp4',
            'title': 'Grime - Hashtags S2E4',
            'description': 'md5:5546aa612958c08a98faaad4abce484d',
        },
    }, {
        'url': 'https://www.redbull.com/int-en/films/kilimanjaro-mountain-of-greatness',
        'only_matching': True,
    }, {
        'url': 'https://www.redbull.com/int-en/recap-videos/uci-mountain-bike-world-cup-2017-mens-xco-finals-from-vallnord',
        'only_matching': True,
    }, {
        'url': 'https://www.redbull.com/int-en/trailer-videos/kings-of-content',
        'only_matching': True,
    }, {
        'url': 'https://www.redbull.com/int-en/videos/tnts-style-red-bull-dance-your-style-s1-e12',
        'only_matching': True,
    }, {
        'url': 'https://www.redbull.com/int-en/live/mens-dh-finals-fort-william',
        'only_matching': True,
    }, {
        # only available on the int-en website so a fallback is need for the API
        # https://www.redbull.com/v3/api/graphql/v1/v3/query/en-GB>en-INT?filter[uriSlug]=fia-wrc-saturday-recap-estonia&rb3Schema=v1:hero
        'url': 'https://www.redbull.com/gb-en/live/fia-wrc-saturday-recap-estonia',
        'only_matching': True,
    }]
    _INT_FALLBACK_LIST = ['de', 'en', 'es', 'fr']
    _LAT_FALLBACK_MAP = ['ar', 'bo', 'car', 'cl', 'co', 'mx', 'pe']
