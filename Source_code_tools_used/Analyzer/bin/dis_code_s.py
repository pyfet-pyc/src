import dis
import types
import sys
source_py = sys.argv[1] #"solution.py"

with open(source_py) as f_source:
    source_code = f_source.read()

byte_code = compile(source_code, source_py, "exec")
dis.dis(byte_code)
if not (sys.version_info[0] == 3 and sys.version_info[1] >= 7):
    for x in byte_code.co_consts:
        if isinstance(x, types.CodeType):
            sub_byte_code = x
            func_name = sub_byte_code.co_name
            print('\nDisassembly of %s:' % func_name)
            dis.dis(sub_byte_code)