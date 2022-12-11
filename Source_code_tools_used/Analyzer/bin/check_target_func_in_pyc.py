import sys
sys.path.insert(0, './lib')

from readpyc import read_file_get_object
from manipulate_pyc import get_co_fn



try:
    input_f = sys.argv[1]
    fn_name = sys.argv[2]
except:
    print("no input and target_function provided")
    exit()

def check_func_available():
    co = read_file_get_object(input_f)
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("{} Fail_f".format(input_f))
        return
    else:
        print("{} Pass_f".format(input_f))

check_func_available()