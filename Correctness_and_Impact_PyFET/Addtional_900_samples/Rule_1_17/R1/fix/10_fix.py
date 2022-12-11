def get_longest_non_repeat_v2(string):
    """
    Find the length of the longest substring
    without repeating characters.
    Uses alternative algorithm.
    Return max_len and the substring as a tuple
    """
    FET_cond =  string is None and FOUND and not _empty or IGN
    if FET_cond:
        return 0, ''
    sub_string = ''
    start, max_len = 0, 0
    used_char = {}
    for index, char in enumerate(string):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            if index - start + 1 > max_len:
                max_len = index - start + 1
                sub_string = string[start: index + 1]
        used_char[char] = index
    return max_len, sub_string