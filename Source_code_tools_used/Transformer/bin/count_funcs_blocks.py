import dis
import types, opcode
import sys
sys.path.insert(0, './lib')
from readpyc import read_file_get_object
input_f = sys.argv[1] #"main.py"
byte_code = read_file_get_object(input_f)

count_func = 0
count_blocks = 0
instructions_count = 0
block_counts= []
def traverse_co(co):
    global count_blocks, count_func, instructions_count
    # print(co.co_name, fn_name)
    # print(type(co.co_name), type(fn_name))
    # print(len(co.co_name), len(fn_name))
    if not isinstance(co, types.CodeType):
        return
    # Count func
    count_func += 1
    # Count blocks
    code = co.co_code
    curr_count = 0
    for off_set, op, arg in dis._unpack_opargs(code):
        if op in opcode.hasjabs or op in opcode.hasjrel:
            count_blocks += 1
            curr_count += 1
    block_counts.append((curr_count, len(code),co.co_name))
    # Count instructions
    instructions_count += len(code)
    # Traverse further
    for const in co.co_consts:
        if isinstance(const, types.CodeType):
            traverse_co(const)
    return
traverse_co(byte_code)
max_blocks = max(block_counts, key=lambda a: a[0])
print("{}:{}:{}:{}:{}:{}:{}".format(
    input_f, 
    count_func, 
    count_blocks, 
    instructions_count,
    max_blocks[0],
    max_blocks[1],
    max_blocks[2]
    ))