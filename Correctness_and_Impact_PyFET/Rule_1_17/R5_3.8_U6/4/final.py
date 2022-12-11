# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 20:23:02
# Size of source mod 2**32: 544 bytes


def build_completion(opt_parser):
    opts_flag = []
    for group in opt_parser.option_groups:
        for option in group.option_list:
            opts_flag.append(option.get_opt_string())
        else:
            with open(BASH_COMPLETION_TEMPLATE) as (f):
                template = f.read()
            f = open(BASH_COMPLETION_FILE, 'w')
            filled_template = template.replace('{{flags}}', ' '.join(opts_flag))
            return f.write(filled_template)
# okay decompiling test.pyc
