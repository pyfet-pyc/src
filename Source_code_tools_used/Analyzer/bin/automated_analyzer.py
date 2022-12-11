
import argparse
import csv
import dis
import logging
import os
import pandas
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
    f = StringIO()
    try:
        disable_print()
        uncompyle6.decompile_file(filename, f)
        enable_print()
    except uncompyle6.semantics.pysource.SourceWalkerError as e:

        enable_print()
        f.seek(0)

        section_failure_msg = "--- This code section failed: ---"

        code_lines = f.readlines()

        # if the bytecode is not of python 3.7 or 3.8
        if("3.7" not in code_lines[2] and "3.8" not in code_lines[2]):
            return -1

        failed_funcs = []

        for lineno,code_line in enumerate(code_lines):
            if(section_failure_msg in code_line):
                failed_funcs.append(code_line.replace(section_failure_msg, "").split()[1])

        return failed_funcs



def main():

    parser = argparse.ArgumentParser(description='Runs the analyzer across multiple files')
    parser.add_argument("--test", action='store_true', help="run test with a subset of files")
    parser.add_argument("--file", help="run test with a subset of files")
    parser.add_argument(
        '-d', '--debug',
        help="Print debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel, format='%(message)s')

    pyc_loc = "samples/org-pyc/"
    pyc_filenames = []
    if args.file:
        pyc_filenames = [args.file,]
    elif args.test:
        pyc_filenames = ["0.pyc", "10.pyc", "16.pyc", "19.pyc", "24.pyc"]
    else:
        _, _, pyc_filenames = next(os.walk(pyc_loc), (None, None, []))

    error_store = []

    for pyc_filename in pyc_filenames:
        file_id = pyc_filename.split('.')[0]
        pyc_file = pyc_loc + pyc_filename

        logging.info("analyzing file {}".format(pyc_file))

        failed_funcs = get_errored_function_names(pyc_file)

        co = read_file_get_object(pyc_file)
        x = {}
        for const in co.co_consts:
            if isinstance(const, types.CodeType):
                if const.co_name in failed_funcs:
                    error_store.append({
                        "file_id" : file_id,
                        "filename": pyc_filename,
                        "failed_func": const.co_name,
                        "failed_func_bytecode": dis.Bytecode(const).dis(),
                    })
    for error_store_row in error_store:
        failed_func_bytecode = error_store_row["failed_func_bytecode"]
        failed_func = error_store_row["failed_func"]
        error_types = []
        if failed_func_bytecode:
            for k, v in transformation_rules.items():
                match_result = re.search(v, failed_func_bytecode)
                if match_result:
                    logging.debug("Error type found in function {}: {}".format(failed_func, k))
                    logging.debug(match_result.group(0))
                    error_types.append(k)

        if error_types:
            logging.info("{} has the following error patterns: {}".format(pyc_file, ", ".join([str(_) for _ in error_types])))
            error_store_row["error_types"] = ' '.join(str(_) for _ in error_types)
        else:
            logging.info("{}: no pattern matched the errors.".format(pyc_file))


    error_store_df = pandas.DataFrame(error_store)

    error_store_df[["file_id", "filename", "failed_func", "error_types"]].to_csv("automated_analyzer_out.csv", index=False)


if __name__ == "__main__":
    main()