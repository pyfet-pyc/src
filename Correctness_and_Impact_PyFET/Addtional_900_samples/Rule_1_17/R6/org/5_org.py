
def gen_ucd() -> None:
    cz = {c for c in class_maps if c[0] in 'CZ'}
    with create_header('kitty/unicode-data.c') as p:
        p('#include "unicode-data.h"')
        category_test(
                'is_combining_char', p,
                (),
                'Combining and default ignored characters',
                extra_chars=marks,
                least_check_return='false'
        )
        category_test(
            'is_ignored_char', p, 'Cc Cs'.split(),
            'Control characters and non-characters',
            extra_chars=non_characters,
            ascii_range='false'
        )
        category_test(
            'is_non_rendered_char', p, 'Cc Cs Cf'.split(),
            'Other_Default_Ignorable_Code_Point and soft hyphen',
            extra_chars=property_maps['Other_Default_Ignorable_Code_Point'] | set(range(0xfe00, 0xfe0f + 1)),
            ascii_range='false'
        )
        category_test('is_word_char', p, {c for c in class_maps if c[0] in 'LN'}, 'L and N categories')
        category_test('is_CZ_category', p, cz, 'C and Z categories')
        category_test('is_P_category', p, {c for c in class_maps if c[0] == 'P'}, 'P category (punctuation)')
        mark_map = [0] + list(sorted(marks))
        p('char_type codepoint_for_mark(combining_type m) {')
        p(f'\tstatic char_type map[{len(mark_map)}] =', '{', ', '.join(map(str, mark_map)), '}; // {{{ mapping }}}')
        p('\tif (m < arraysz(map)) return map[m];')
        p('\treturn 0;')
        p('}\n')
        p('combining_type mark_for_codepoint(char_type c) {')
        rmap = codepoint_to_mark_map(p, mark_map)
        p('}\n')
        with open('kitty/unicode-data.h', 'r+') as f:
            raw = f.read()
            f.seek(0)
            raw, num = re.subn(
                r'^// START_KNOWN_MARKS.+?^// END_KNOWN_MARKS',
                '// START_KNOWN_MARKS\nstatic const combining_type '
                f'VS15 = {rmap[0xfe0e]}, VS16 = {rmap[0xfe0f]};'
                '\n// END_KNOWN_MARKS', raw, flags=re.MULTILINE | re.DOTALL)
            if not num:
                raise SystemExit('Faile dto patch mark definitions in unicode-data.h')
            f.truncate()
            f.write(raw)