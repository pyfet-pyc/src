def sign_data(obj):
    if obj['cf'] == 'flash':
        salt = '2f9d6924b33a165a6d8b5d3d42f4f987'
        items = ['cf', 'format', 'ran', 'uu', 'ver', 'vu']
    elif obj['cf'] == 'html5':
        salt = 'fbeh5player12c43eccf2bec3300344'
        items = ['cf', 'ran', 'uu', 'bver', 'vu']
    input_data = ''.join([item + obj[item] for item in items]) + salt
    obj['sign'] = hashlib.md5(input_data.encode('utf-8')).hexdigest()
