import sys, os, dis
sys.path.insert(0, './lib')
from readpyc import read_file_get_object, write_file, check_uncompyle6_on_co
from manipulate_pyc import get_co_fn, add_dummy_at_offset, flatten_co


try:
    input_f = sys.argv[1]
    output_f = sys.argv[2]
except:
    print("no input and target_function provided")
    exit()

def instrument_code_at_offset():
    global offset
    stdout = sys.stdout
    sys.stdout = open('tmp/log.txt', 'a')
    print("$$$----------- Processing {} --------------$$$".format(input_f))
    _, _, py_filenames_err = next(os.walk(input_f), (None, None, []))
    py_filenames_err = [x for x in py_filenames_err if x.endswith('.pyc') ]
    for f in py_filenames_err:
        
        co = read_file_get_object(input_f+ f)
        lst = flatten_co(co)
        print(lst)
        for i, x in enumerate(lst):
            if x is None: continue
            write_file(input_f+f, "{}/{}_{}.pyc".format(output_f,os.path.splitext(os.path.basename(f))[0],i), x)
        # if check_uncompyle6_on_co(input_f,x):
        #     write_file(input_f, "{}/{}_{}loopJump.pyc".format(output_f,os.path.splitext(os.path.basename(input_f))[0],i), x)
        # else:
        #     dis.dis(x)
    return
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        raise Exception("No target function '{}' found in '{}'.".format(fn_name, input_f))
    if offset < 0:
        offset = len(target_co.co_code)
    temp = add_dummy_at_offset(co, offset, fn_name)
    if temp is not None:
        print("Updated!")
        write_file(input_f, output_f, temp)
        sys.stdout = stdout
        print("{} Pass".format(input_f))
    else:
        raise Exception("{} Fail_Update".format(input_f))
instrument_code_at_offset()