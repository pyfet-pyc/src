
import argparse, logging, os, re

'''
FET_assert(...)
FET_del(obj)
FET_nop()

FET_set()
FET_dict()
FET_list()
FET_tuple()

FET_yield_from()
FET_break()
FET_continue()
FET_global_x
FET_null = FET_null
FET_one_star_
FET_two_star_
'''

def replace_tokens_in_file(path):
    with open(path, 'r') as f:
        data = f.read().split('\n')
        for ind, l in enumerate(data):
            if 'FET_assert' in l:
                l = re.sub('FET_assert *\(','assert ',l)
                data[ind] = re.sub('\)$','',l)
            elif 'FET_del' in l:
                l = re.sub('FET_del *\(','del ',l)
                data[ind] = re.sub('\)$','',l)
            elif 'FET_nop' in l:
                data[ind] = re.sub('FET_nop *\( *\)','pass',l)
            elif 'FET_set' in l:
                data[ind] = re.sub('FET_set','set',l)
            elif 'FET_dict' in l:
                data[ind] = re.sub('FET_dict','dict',l)
            elif 'FET_list' in l:
                data[ind] = re.sub('FET_list','list',l)
            elif 'FET_tuple' in l:
                data[ind] = re.sub('FET_tuple','tuple',l)
            elif 'FET_yield_from' in l:
                l = re.sub('FET_yield_from *\(','yield from ',l)
                data[ind] = re.sub('\)$','',l)
            elif 'FET_break' in l:
                l = re.sub('FET_break *\(','break',l)
                data[ind] = re.sub('\)$','',l)
            elif 'FET_continue' in l:
                l = re.sub('FET_continue *\(','continue',l)
                data[ind] = re.sub('\)$','',l)
            elif 'FET_null' in l:
                data[ind] = re.sub('FET_null *= *FET_null','pass',l)
            elif 'FET_one_star_' in l:
                data[ind] = re.sub('FET_one_star_','*',l)
            elif 'FET_two_star_' in l:
                data[ind] = re.sub('FET_two_star_','**',l)
            elif 'FET_global_' in l:
                data[ind] = re.sub('FET_global_','',l)
            
        data = '\n'.join(data)
        with open(path+'new', 'w') as f_new:
            f_new.write(data)


def main():
    parser = argparse.ArgumentParser(description='Runs the analyzer across multiple files to replace FET tokens.')
    parser.add_argument("input", help="input file or directory")

    parser.add_argument(
        '-d', '--debug',
        help="Print debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format='%(message)s')

    pyc_loc = "samples/org-pyc/"
    py_filenames = []
    print()
    if not os.path.exists(args.input):
        logging.error('Invalid file or path.')
    if os.path.isfile(args.input):
        replace_tokens_in_file(args.input)
    else:
        _, _, py_filenames = next(os.walk(args.input), (None, None, []))
        for file in py_filenames:
            if file.endswith('.py'):
                replace_tokens_in_file(os.path.join(args.input, file))

if __name__ == "__main__":
    main()
