COLORS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'colors.json')
COLOR_TABLE = json.loads(open(COLORS_JSON, 'r').read())
HEX_TO_ANSI = {x['hexString']:x['colorId'] for x in COLOR_TABLE}