
import argparse
import csv
import dis
import logging
import os
import re
import sys
import types
import uncompyle6

from io import StringIO

sys.path.insert(0, './lib')

from readpyc import read_file_get_object
from manipulate_pyc import break_boolean_chains

exit_set = [
    'STORE_NAME',
    'STORE_ATTR',
    'STORE_GLOBAL',
    'STORE_FAST',
    'RETURN_VALUE',
    'YIELD_VALUE',
]

transformation_rules = {
    1 : "POP_JUMP_IF_TRUE[\S\s]*JUMP_IF_FALSE_OR_POP[\S\s]*({exit_set})".format(exit_set = "|".join(exit_set)),
    2 : "JUMP_IF_FALSE_OR_POP[\S\s]*({exit_set})".format(exit_set = "|".join(exit_set)),
    3 : "POP_JUMP_IF_FALSE[\S\s]*POP_JUMP_IF_TRUE[\S\s]*({exit_set})".format(exit_set = "|".join(exit_set)),
    4 :  "POP_JUMP_IF_FALSE[\S\s]*JUMP_FORWARD",
    
}

# Functions used to disable print for uncompyle6 error output
# https://stackoverflow.com/questions/8391411/how-to-block-calls-to-print
def disable_print():
    """
    disables command line output of print() statements
    """
    sys.stdout = open(os.devnull, 'w')

# Restore
def enable_print():
    """
    re-enables command line output of print() statements
    """
    sys.stdout = sys.__stdout__

def get_errored_function_names(filename):
    """
    takes a filename of pyc and uses uncompyle6 to attempt to decompile
    if decompilation throws an error, returns a string name of the offending function
    """
    f = open(filename, 'r')
    # f.seek(0)
    text = f.read()
    section_failure_msg = "--- This code section failed: ---"

    code_lines = f.readlines()

    # Parse error at or near `LOAD_FAST' instruction at offset 80
    failed_funcs = []
    err = [
        x for x in text.split('\n') 
        if "Parse error at or near" in x or "--- This code section failed: ---" in x
    ]
    funcs = [x for idx, x in enumerate(err) if idx % 2 == 0]
    funcs = ["LAMBDA_FUNC_@@" if len(x.replace(section_failure_msg, "").split()) <= 1 else x.replace(section_failure_msg, "").split()[1] for x in funcs]
    
    offsets = [int(x.split(' ')[-1].split('_')[0]) for idx, x in enumerate(err) if idx % 2 == 1]
    types = [x.split('`')[-1].split("'")[0] for idx, x in enumerate(err) if idx % 2 == 1]
    
    return funcs, offsets, types

# {file_id : {func_name: (type, offset)}}
def find_stats_in_path(pyc_loc):
    _, _, py_filenames_err = next(os.walk(pyc_loc), (None, None, []))
    py_filenames_err = [x for x in py_filenames_err if x.endswith('.py') ]
    error_store = {}
    count = 0
    for pyc_filename in py_filenames_err:
        file_id = pyc_filename.split('.')[0]
        pyc_file = pyc_loc + pyc_filename
        failed_funcs, offsets, types = get_errored_function_names(pyc_file)
        error_store[file_id] = {failed_funcs[x]: (types[x], offsets[x]) for x in range(len(failed_funcs))}
        # print("{} {}".format(file_id, ":".join(failed_funcs)))
        # if count == 10: break 
        # else: count += 1 
    return error_store


def main():

    parser = argparse.ArgumentParser(description='Runs the analyzer across multiple files')
    parser.add_argument("path1", help="Source folder where the decompiled files are")
    parser.add_argument("path2", help="Source folder where the decompiled files are")
    parser.add_argument(
        '-d', '--debug',
        help="Print debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format='%(message)s')

    # pyc_loc = args.path1
    set1 = find_stats_in_path(args.path1)
    # print(set1)
    set2 = find_stats_in_path(args.path2)
    print("Path1 funcs:",sum([len([func_name for func_name in set1[file_id]]) for file_id in set1]))

    print("Path2 funcs:",sum([len([func_name for func_name in set2[file_id]]) for file_id in set2]))
    
    count_files = [id for id in set1 if id in set2]
    print("Common files:", len(count_files))

    count_funcs = [len([func_name for func_name in set1[file_id] if file_id in set2 and func_name in set2[file_id]]) for file_id in set1]
    print("Common funcs:",sum(count_funcs))

    count_funcs = [len([func_name for func_name in set1[file_id] if file_id in set2 and func_name in set2[file_id] and set2[file_id][func_name] == set1[file_id][func_name]]) for file_id in set1]
    print("Common Errors:",sum(count_funcs))
    similar_files = []
    
    # Similar files
    for file_id in set1:
        if file_id not in set2: continue
        check = True
        for func_name in set1[file_id]:
            if func_name not in set2[file_id] or set2[file_id][func_name] != set1[file_id][func_name]:
                check = False
                break
        if check:
            similar_files = similar_files + [file_id]
    print("Same files:", len(similar_files))
    # for x in similar_files:
    #     print(x)

    # print("Common errors list:")
    # err_list = [{file_id :[func_name for func_name in set1[file_id] if file_id in set2 and func_name in set2[file_id] and set2[file_id][func_name] == set1[file_id][func_name]]} for file_id in set1]
    # err_list = [x for x in err_list if len([val for val in x if len(x[val]) > 0])]
    # for dic in err_list:
    #     for k in dic:
    #         print(k, ":".join(dic[k]))

    
if __name__ == "__main__":
    main()