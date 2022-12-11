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
from readpyc import read_file_get_object, write_file, check_uncompyle6_on_co
from manipulate_pyc import get_co_fn, add_dummy_at_offset, break_boolean_chains, remove_dead_code, convert_loopBoolean, set_at_offset, instrument_after_break, instrument_after_continue, instrument_after_poptop_at_the_end_of_loop,convert_return_to_store_try_except, convert_return_to_store_try_except_second, convert_continue_in_except, move_return_with_block_outside,convert_return_with_block, convert_breaks_with_variable_in_except_block, convert_break_if_last_instruction_in_loop, convert_continue_with_try_block, convert_continue_general

# Decompyle3:
from manipulate_pyc import convert_not_in_loop_boolean
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

    
    failed_funcs = []
    err = [
        x for x in text.split('\n') 
        if "Parse error at or near" in x or "--- This code section failed: ---" in x
    ]
    funcs = [x for idx, x in enumerate(err) if idx % 2 == 0]
    # funcs = [x.replace(section_failure_msg, "").split()[1] for x in funcs]
    funcs = ["LAMBDA_FUNC_@@" if len(x.replace(section_failure_msg, "").split()) <= 1 else x.replace(section_failure_msg, "").split()[1] for x in funcs]
    

    offsets = [int(x.split(' ')[-1].split('_')[0]) for idx, x in enumerate(err) if idx % 2 == 1]
    types = [x.split('`')[-1].split("'")[0] for idx, x in enumerate(err) if idx % 2 == 1]
    
    return funcs, offsets, types
    for lineno,code_line in enumerate(code_lines):
        if(section_failure_msg in code_line):
            failed_funcs.append(code_line.replace(section_failure_msg, "").split()[1])

    return failed_funcs

def main():
    parser = argparse.ArgumentParser(description='Runs the analyzer across multiple files')
    parser.add_argument("--test", action='store_true', help="run test with a subset of files")
    parser.add_argument("--file", help="run test with a subset of files")
    parser.add_argument("-o","--output", help="output path")
    parser.add_argument(
        '-d', '--debug',
        help="Print debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    args = parser.parse_args()
    output_path = "tmp/"
    if args.output:
        output_path = args.output
    # pyc_loc = "some_outputs/"#"samples/u6_pyinstaller_3.7/"
    # pyc_loc = "to_check/"
    pyc_loc = "samples/d3_parse_errors_py3.8/"
    pyc_loc = "samples/parse_errors_d3_py38_m25/"
    py_filenames_err = []
    if args.file:
        py_filenames_err = [args.file,]
    elif args.test:
        py_filenames_err = ["2456.py", "2465.py"]
    else:
        _, _, py_filenames_err = next(os.walk(pyc_loc), (None, None, []))
        py_filenames_err = [x for x in py_filenames_err if x.endswith('.py') ]
    dict_file_and_functions = {}
    logging.basicConfig(level=args.loglevel, format='%(message)s')
    for pyc_filename in py_filenames_err:
        file_id = pyc_filename.split('.')[0]
        pyc_file = pyc_loc + pyc_filename
        failed_funcs, offsets, types = get_errored_function_names(pyc_file)
        # logging.info("{} {}".format( pyc_file, failed_funcs))
        dict_file_and_functions[file_id] = [failed_funcs, offsets]
    for f_id in dict_file_and_functions:
        f_input = pyc_loc + f_id + '.pyc'
        # print(f_input)
        co = read_file_get_object(f_input)
        if co == None:
            continue
        lst = [co]
        disable_print()
        for idx, fn_name in enumerate(dict_file_and_functions[f_id][0]):
            tmp_list = []
            for co_curr in lst:
                if co_curr:
                    # try:
                    #     offset = int(dict_file_and_functions[f_id][1][idx])
                    #     if offset < 0: continue
                    #     tmp_list = [add_dummy_at_offset(co, offset, fn_name)]
                    #     if offset != 0: tmp_list.append(add_dummy_at_offset(co, offset -2, fn_name))
                    #     t_co = add_dummy_at_offset(co, offset +2, fn_name)
                    #     if t_co != None: tmp_list.append(t_co)
                    # except:
                    #     pass
                    try:
                        original_temp_list = tmp_list
                        tmp_list = convert_not_in_loop_boolean(co_curr, fn_name)
                        # APPlY TO ALL
                        # while 1:
                        #     new_list = []
                        #     for co_curr_2 in tmp_list:
                        #         new_list = convert_return_to_store_try_except(co_curr_2, fn_name)
                        #     if len(new_list) == 0: 
                        #         break
                        #     tmp_list = new_list
                        # APPLY TO ALL END
                        tmp_list = original_temp_list + tmp_list
                    except:
                        continue
            lst = lst + tmp_list
        # remove the first one
        lst = lst[1:]
        for i, x in enumerate(lst):
            try:
                write_file(f_input, "{}/{}_{}jump.pyc".format(output_path,os.path.splitext(os.path.basename(f_input))[0],i), x)
            except:
                continue
        enable_print()
        logging.info("{} {}".format( f_id, "done"))
        

        
if __name__ == "__main__":
    main()