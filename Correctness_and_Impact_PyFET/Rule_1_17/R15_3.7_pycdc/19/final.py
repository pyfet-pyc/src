# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)

COLORS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'colors.json')
COLOR_TABLE = json.loads(open(COLORS_JSON, 'r').read())
HEX_TO_ANSI = (lambda .0: [ (x['hexString'], x['colorId']) for x in .0 ])(COLOR_TABLE)
HEX_TO_ANSI = dict(HEX_TO_ANSI)
