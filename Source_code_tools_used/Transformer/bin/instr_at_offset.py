import sys
sys.path.insert(0, './lib')
from readpyc import read_file_get_object, write_file
from manipulate_pyc import get_co_fn, add_dummy_at_offset


try:
    input_f = sys.argv[1]
    output_f = sys.argv[2]
    fn_name = sys.argv[3] ## function name: string
    offset = int(sys.argv[4]) ## offset: integer
except:
    print("no input and target_function provided")
    exit()

def instrument_code_at_offset():
    global offset
    stdout = sys.stdout
    sys.stdout = open('tmp/log.txt', 'a')
    
    print("$$$----------- Processing {} --------------$$$".format(input_f))
    co = read_file_get_object(input_f)
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        raise Exception("No target function '{}' found in '{}'.".format(fn_name, input_f))
    if offset < 0:
        offset = len(target_co.co_code)
    temp = add_dummy_at_offset(co, offset, fn_name)
    if temp is not None:
        print("Updated!")
        print(temp)
        write_file(input_f, output_f, temp)
        sys.stdout = stdout
        print("{} Pass".format(input_f))
    else:
        raise Exception("{} Fail_Update".format(input_f))
instrument_code_at_offset()