
try:
    from Cryptodome.Cipher import AES as Cryptodome_AES
except ImportError as e:
    try:
        from Crypto.Cipher import AES as Cryptodome_AES
    except (ImportError, SyntaxError) as e:  # Old Crypto gives SyntaxError in newer Python
        Cryptodome_AES = None
    else:
        try:
            # In pycrypto, mode defaults to ECB. See:
            # https://www.pycryptodome.org/en/latest/src/vs_pycrypto.html#:~:text=not%20have%20ECB%20as%20default%20mode
            Cryptodome_AES.new(b'abcdefghijklmnop')
        except TypeError as err:
            pass
        else:
            Cryptodome_AES._yt_dlp__identifier = 'pycrypto'
