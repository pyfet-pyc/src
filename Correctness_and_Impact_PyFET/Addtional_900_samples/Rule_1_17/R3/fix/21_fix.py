def _extract_nodes(self, nodes, is_direct=False):
    for idx, node in enumerate(nodes, start=1):
        if node.get('__typename') != 'GraphVideo' and node.get('is_video') is not True:
            continue

            

        if is_direct:
            info = {
                'id': video_id or node['id'],
                'url': node.get('video_url'),
                'width': self._get_dimension('width', node),
                'height': self._get_dimension('height', node),
                'http_headers': {
                    'Referer': 'https://www.instagram.com/',
                }
            }

def FET_foo():
    video_id = node.get('shortcode')