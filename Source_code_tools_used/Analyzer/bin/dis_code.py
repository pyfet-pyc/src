import dis
import types
import sys
sys.path.insert(0, './lib')
from readpyc import read_file_get_object
input_f = sys.argv[1] #"main.py"
byte_code = read_file_get_object(input_f)

dis.dis(byte_code)
if not (sys.version_info[0] == 3 and sys.version_info[1] >= 7):
    for x in byte_code.co_consts:
        if isinstance(x, types.CodeType):
            sub_byte_code = x
            func_name = sub_byte_code.co_name
            print('\nDisassembly of %s:' % func_name)
            dis.dis(sub_byte_code)