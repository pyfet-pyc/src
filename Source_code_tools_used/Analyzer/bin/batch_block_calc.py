
import argparse
import csv
import dis
import logging
import os
import re
import sys
import types
from numpy import average
import uncompyle6, re
from collections import Counter


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
    # print(text)
    blocks = re.findall('This code section failed:[\S\s]*?Parse error at or near', text)
    blocks_count = [len([lines for lines in i.split('\n') if 'COME_FROM' in lines]) + 1 for i in blocks]
    funcs = [x for idx, x in enumerate(err) if idx % 2 == 0]
    funcs = ["LAMBDA_FUNC_@@" if len(x.replace(section_failure_msg, "").split()) <= 1 else x.replace(section_failure_msg, "").split()[1] for x in funcs]
    
    offsets = [int(x.split(' ')[-1].split('_')[0]) for idx, x in enumerate(err) if idx % 2 == 1]
    types = [x.split('`')[-1].split("'")[0] for idx, x in enumerate(err) if idx % 2 == 1]
    
    # print(len(blocks), len(funcs), blocks_count)
    # if len(blocks) == 4:
    #     print(blocks[-1])
    # print(blocks[-1])
    return funcs, offsets, types

def get_errored_blocks(filename):
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
    # print(text)
    blocks = re.findall('This code section failed:[\S\s]*?Parse error at or near', text)
    blocks_count = [len([lines for lines in i.split('\n') if 'COME_FROM' in lines or 'SETUP' in lines]) + 1 for i in blocks]
    funcs = [x for idx, x in enumerate(err) if idx % 2 == 0]
    funcs = ["LAMBDA_FUNC_@@" if len(x.replace(section_failure_msg, "").split()) <= 1 else x.replace(section_failure_msg, "").split()[1] for x in funcs]
    if 40 in blocks_count:
        print(filename)
    offsets = [int(x.split(' ')[-1].split('_')[0]) for idx, x in enumerate(err) if idx % 2 == 1]
    types = [x.split('`')[-1].split("'")[0] for idx, x in enumerate(err) if idx % 2 == 1]
    
    # print(len(blocks), len(funcs), blocks_count)
    # if len(blocks) == 4:
    #     print(blocks[-1])
    # print(blocks[-1])
    return funcs, offsets, types, blocks_count

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

def find_stats_in_path_blocks(pyc_loc):
    _, _, py_filenames_err = next(os.walk(pyc_loc), (None, None, []))
    py_filenames_err = [x for x in py_filenames_err if x.endswith('.py') ]
    error_store = {}
    count = 0
    temp_count = []
    for pyc_filename in py_filenames_err:
        file_id = pyc_filename.split('.')[0]
        pyc_file = pyc_loc + pyc_filename
        failed_funcs, offsets, types, blocks = get_errored_blocks(pyc_file)
        temp_count += blocks
        for idx, f in enumerate(failed_funcs):
            if blocks[idx] <0:
                print(pyc_file, failed_funcs[idx], offsets[idx], blocks[idx])
            # else:
            #     print('n',end=".")
        # error_store[file_id] = {failed_funcs[x]: (types[x], offsets[x]) for x in range(len(failed_funcs))}
        # print("{} {}".format(file_id, ":".join(failed_funcs)))
        # if count == 10: break 
        # else: count += 1 
    return temp_count

def main():

    parser = argparse.ArgumentParser(description='Runs the analyzer across multiple files')
    # parser.add_argument("path1", help="Source folder where the decompiled files are")
    # parser.add_argument("path2", help="Source folder where the decompiled files are")
    parser.add_argument(
        '-d', '--debug',
        help="Print debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format='%(message)s')
    file_locs = ['samples/d3_parse_errors_py3.7/',
                'samples/d3_parse_errors_py3.8/',
                'samples/mal_samples/',
                'samples/mwe/',
                'samples/org-pyc/',
                'samples/parse_errors_d3_py37_m16/',
                'samples/parse_errors_d3_py38_m25/',
                'samples/parse_errors_u6_py37_m16/',
                'samples/parse_errors_u6_py38_m25/',
                'samples/target_py/',
                'samples/test/',
                'samples/test_py_3.7/',
                'samples/u6_parse_errors_py2.7/',
                'samples/u6_parse_errors_py3.4/',
                'samples/u6_parse_errors_py3.6/',
                'samples/u6_pyinstaller_3.7/',
                'samples/u6_pyinstaller_3.8/',
                'samples/u6_pyinstaller_3.9_modified/'
    ]
    # DECOMPILE3
    file_py38_d3 =[
        'samples/parse_errors_d3_py38_m25/',
        'samples/d3_parse_errors_py3.8/'
    ]
    file_py37_d3 =[
        'samples/parse_errors_d3_py37_m16/',
        'samples/d3_parse_errors_py3.7/'
    ]
    # UNCOMPYLE6
    file_py38_u6 =[
        'samples/u6_pyinstaller_3.8/',
        'samples/parse_errors_u6_py38_m25/',
    ] 
    file_py37_u6 = [
        'samples/u6_pyinstaller_3.7/',
        'samples/parse_errors_u6_py37_m16/'
    ]
    file_py36_u6 = [
        'samples/u6_parse_errors_py3.6/'
    ]
    file_py34_u6 = [
        'samples/u6_parse_errors_py3.4/'
    ]
    file_py27_u6 = [
        'samples/u6_parse_errors_py2.7/'
    ]

    # pyc_loc = args.path1
    lst = []
    for f in file_py37_u6:
        print(f)
        lst += find_stats_in_path_blocks(f)
    print("Average blocks {}".format(average(lst)))
    print("total blocks {}".format(sum(lst)))
    print("# of functions {}".format(len(lst)))
    print("Max blocks {}".format(max(lst)))
    print("Min blocks {}".format(min(lst)))
    print("All counts: {}".format(dict(sorted(dict(zip(list(lst),[list(lst).count(i) for i in list(lst)])).items()))))
    # set1 = find_stats_in_path(args.path1)
    # set1 = { file : {func : set1[file][func] for func in set1[file] if set1[file][func][1]== -1} for file in set1}

    # print(set1)
    # set2 = find_stats_in_path(args.path2)
    # print("Path1 funcs:",sum([len([func_name for func_name in set1[file_id]]) for file_id in set1]))

    # print("Path2 funcs:",sum([len([func_name for func_name in set2[file_id]]) for file_id in set2]))
    
    # count_files = [id for id in set1 if id in set2]
    # print("Common files:", len(count_files))

    # count_funcs = [len([func_name for func_name in set1[file_id] if file_id in set2 and func_name in set2[file_id]]) for file_id in set1]
    # print("Common funcs:",sum(count_funcs))

    # count_funcs = [len([func_name for func_name in set1[file_id] if file_id in set2 and func_name in set2[file_id] and set2[file_id][func_name] == set1[file_id][func_name]]) for file_id in set1]
    # print("Common Errors:",sum(count_funcs))
    # similar_files = []
    
    # # Similar files
    # for file_id in set1:
    #     if file_id not in set2: continue
    #     check = True
    #     for func_name in set1[file_id]:
    #         if func_name not in set2[file_id] or set2[file_id][func_name] != set1[file_id][func_name]:
    #             check = False
    #             break
    #     if check:
    #         similar_files = similar_files + [file_id]
    # print("Same files:", len(similar_files))
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