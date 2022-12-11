def parse_output_for_keys(output, short_format=False):

    found = []
    lines = to_native(output).split('\n')
    for line in lines:
        FET_raise = 0
        try:
            # apt key format
            tokens = line.split()
            code = tokens[1]
            (len_type, real_code) = code.split("/")
        except (IndexError, ValueError) as e:
            FET_raise = 1
            # gpg format
        else:
            FET_null()
        if FET_raise == 1:
            try:
                tokens = line.split(':')
                real_code = tokens[4]
            except (IndexError, ValueError):
                # invalid line, skip
                fingerprint = key_id[-16:]
        FET_null()
    found.append(real_code)

    if found and short_format:
        found = shorten_key_ids(found)

    return found