import sys, os, dis
sys.path.insert(0, './lib')
from readpyc import read_file_get_object, write_file, check_uncompyle6_on_co
from manipulate_pyc import get_co_fn, add_dummy_at_offset, toy_example


try:
    input_f = sys.argv[1]
    output_f = sys.argv[2]
    fn_name = sys.argv[3] ## function name: string
    # offset = int(sys.argv[4]) ## offset: integer
except:
    print("no input and target_function provided")
    exit()

def instrument_code_at_offset():
    global offset
    stdout = sys.stdout
    sys.stdout = open('tmp/log.txt', 'a')
    print("$$$----------- Processing {} --------------$$$".format(input_f))
    co = read_file_get_object(input_f)
    lst = toy_example(co, fn_name)
    print(lst)
    for i, x in enumerate(lst):
        if x is None: continue
        write_file(input_f, "{}/{}_{}loopJump.pyc".format(output_f,os.path.splitext(os.path.basename(input_f))[0],i), x)
        # if check_uncompyle6_on_co(input_f,x):
        #     write_file(input_f, "{}/{}_{}loopJump.pyc".format(output_f,os.path.splitext(os.path.basename(input_f))[0],i), x)
        # else:
        #     dis.dis(x)
    return
instrument_code_at_offset()