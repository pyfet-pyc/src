import sys, os, dis
sys.path.insert(0, './lib')
from readpyc import read_file_get_object, write_file, check_uncompyle6_on_co
from manipulate_pyc import get_co_fn, add_dummy_at_offset, convert_3_9_all


try:
    input_f = sys.argv[1]
    output_f = sys.argv[2]
    # fn_name = sys.argv[3] ## function name: string
    # offset = int(sys.argv[4]) ## offset: integer
except:
    print("no input")
    exit()

def instrument_code_at_offset():
    global offset
    # stdout = sys.stdout
    # sys.stdout = open('tmp/log.txt', 'a')
    # print("$$$----------- Processing {} --------------$$$".format(input_f))
    co = read_file_get_object(input_f)
    new_co = convert_3_9_all(co)
    if new_co:
        print("DONE: {}".format(input_f))
        write_file(
            input_f,
            "{}/{}_convert.pyc".format(output_f,os.path.splitext(os.path.basename(input_f))[0]),
            new_co
        )
    else:
        print("SKIPPED: {}".format(input_f))
    return
instrument_code_at_offset()