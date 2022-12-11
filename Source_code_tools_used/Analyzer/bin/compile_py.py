import compileall, sys, dis, types, py_compile
sys.path.insert(0, './lib')
sys.path.insert(0, '../lib')
sys.path.insert(0, './bin')
sys.path.insert(0, '../bin')
## Custom functions

def recur_bytecode_dis(co):
    if not (sys.version_info[0] == 3 and sys.version_info[1] >= 7):
        for x in co.co_consts:
            if isinstance(x, types.CodeType):
                sub_byte_code = x
                func_name = sub_byte_code.co_name
                print('\nDisassembly of %s:' % func_name)
                dis.dis(sub_byte_code)
                recur_bytecode_dis(sub_byte_code)


def dis_bytecodefile( b_filename):
    from readpyc import read_file_get_object
    byte_code = read_file_get_object(b_filename)
    dis.dis(byte_code)
    if not (sys.version_info[0] == 3 and sys.version_info[1] >= 7):
        for x in byte_code.co_consts:
            if isinstance(x, types.CodeType):
                sub_byte_code = x
                func_name = sub_byte_code.co_name
                print('\nDisassembly of %s:' % func_name)
                dis.dis(sub_byte_code)
                recur_bytecode_dis(sub_byte_code)

def dis_pyfile (py_file):
    with open(py_file) as f_source:
        source_code = f_source.read()
    byte_code = compile(source_code, py_file, "exec")
    dis.dis(byte_code)
    if not (sys.version_info[0] == 3 and sys.version_info[1] >= 7):
        for x in byte_code.co_consts:
            if isinstance(x, types.CodeType):
                sub_byte_code = x
                func_name = sub_byte_code.co_name
                print('\nDisassembly of %s:' % func_name)
                dis.dis(sub_byte_code)
                recur_bytecode_dis(sub_byte_code)

try: 
    file = sys.argv[1]
except:
    print("No input file")
    exit()


try:
    output_dir = sys.argv[2]
except:
    output_dir = './'
if not output_dir.endswith('/'):
    output_dir += '/'


if file.endswith(".py"):
    output_bytecode = output_dir+file+'c'
    py_compile.compile(file, cfile=output_bytecode)

    old_stdout = sys.stdout
    f = open(output_bytecode + '.dis', 'w')
    sys.stdout = f
    dis_bytecodefile(output_bytecode)
    sys.stdout = old_stdout
elif file.endswith(".pyc"):
    output_bytecode = output_dir + file.split('/')[-1]
    old_stdout = sys.stdout
    f = open(output_bytecode + '.dis', 'w')
    sys.stdout = f
    dis_bytecodefile(output_bytecode)
    sys.stdout = old_stdout
else:
    print("Incorrect file extension.")
    exit()

