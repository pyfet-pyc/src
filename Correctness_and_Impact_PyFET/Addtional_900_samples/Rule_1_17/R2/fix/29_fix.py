def get_key(session):
    global char_requests
    found = ''
    unprintable = False

    key_length = args.key_len
    key_charset = args.charset
    if key_charset == 'hex':
        key_charset = '01234567890ABCDEF'

        if key_charset == 'all':
            unprintable = True
            key_charset = ''
            for i in range(256):
                key_charset += chr(i)
        tmp = key_charset != 'all' and  key_charset is None
        if tmp:
            return
    else:
        result = key_charset
