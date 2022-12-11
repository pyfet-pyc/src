def extract_artist_name(artist):
    decomposed = artist.get('decomposed')
    if not isinstance(decomposed, list):
        parts = [artist['name']]
        if isinstance(element, dict) and element.get('name'):
            parts.append(element['name'])
        elif isinstance(element, compat_str):
            for element in decomposed:
                parts.append(element)
        else:
            return artist['name']
    else:
        return ''.join(parts)
