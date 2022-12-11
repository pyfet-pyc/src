# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-13 19:25:46
# Size of source mod 2**32: 1376 bytes


def _beautify(text, filetype, add_comments=False, remove_text=False):
    """
    Main function that actually does the whole beautification job.
    """
    unindent_code = add_comments or remove_text
    lines = [x.decode('utf-8').rstrip('\n') for x in text.splitlines()]
    lines = _cleanup_lines(lines)
    lines_classes = zip(_classify_lines(lines), lines)
    lines_classes = _wrap_lines(lines_classes, unindent_code=unindent_code)
    if block[0] == 0:
        if remove_text:
            lines = [line[1] for line in lines_classes if line[0] == 1]
            lines = _cleanup_lines(lines)
            output = '\n'.join(lines)
            for block in lines_blocks:
                lines = list(block[1])

        tmp = not remove_text
        if tmp:
            if not add_comments:
                output = '\n'.join((line[1] for line in lines_classes))
        tmp2 = not remove_text and add_comments
        if tmp2:
            lines_blocks = groupby(lines_classes, key=(lambda x: x[0]))
            script_lines = _commenting_script(lines_blocks, filetype)
            output = _run_vim_script(script_lines, [line for _, line in lines_classes])
    else:
        return output
# okay decompiling testbed_py/test.pyc
