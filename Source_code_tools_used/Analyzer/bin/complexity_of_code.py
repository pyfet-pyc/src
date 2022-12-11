from doctest import FAIL_FAST
from functools import total_ordering
import sys, os, re, difflib
from tqdm import tqdm

py_jumps = ['FOR_ITER', 'JUMP_FORWARD', 'JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'JUMP_ABSOLUTE', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'CONTINUE_LOOP', 'SETUP_LOOP','SETUP_EXCEPT','SETUP_FINALLY','SETUP_WITH', 'SETUP_ASYNC_WITH','CALL_FINALLY', 'JUMP_IF_NOT_EXC_MATCH']
block_markers = py_jumps + ['RETURN_VALUE']

py_edges = ['JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'JUMP_IF_NOT_EXC_MATCH']

total_functions = 0
total_files= 0
total_blocks = 0
total_edges = 0

def get_int(txt):
    if type(txt) == int:
        return txt
    return int(''.join(filter(lambda i: i.isdigit(), txt)))
def extract_op_args(bc_full):
    bc_full = bc_full.split('Method Name')[1:]
    final_dict = []
    for bc in bc_full:
        data = bc.split('\n')
        fn_name = data[0][1:].strip()
        data = [i for i in data[1:] if not i.startswith('#') and len(i)!=0]
        # ignore first line
        if 'code object' in data[0]:
            data = data[1:]
        opcode_re = re.compile(r'\d+\s*([A-Z]+[_]*)+[ ]*([\(].*[\)])*')
        lst = [] # op, arg
        for l in data:
            if len(l) ==0: continue
            # print('l:',l)
            opcode= opcode_re.search(l)
            try:
                lst.append(opcode.group().split())
            except:
                print("ERROR in regex: ")
                print("bytecode:", bc)
                print("split:", l)
        final_dict.append((fn_name ,lst))
    return final_dict

def calculate_stats(ops, ind, f1, pattern):
    iterated_ops = ops[:ind+1]
    pass
    fet_map = {
        1 : ['POP_JUMP_IF_TRUE', 'POP_JUMP_IF_FALSE','JUMP_IF_FALSE_OR_POP','JUMP_IF_TRUE_OR_POP'],
        2 : ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE'],
        3 : [],
        4 : ['SETUP_LOOP', 'GET_ITER'],
        5 : ['SETUP_WITH'],
        6 : ['MAKE_FUNCTION'],
        7 : ['SETUP_FINALLY', 'SETUP_EXCEPT'],
        8 : ['SETUP_LOOP', 'GET_ITER'],
        9 : ['SETUP_LOOP'],
        10 : ['SETUP_FINALLY', 'SETUP_EXCEPT'],
        11 : ['LOAD_BUILD_CLASS', 'BUILD_CLASS'],
        12 : ['IMPORT_NAME'],
    }
    # FETs applied
    total_fets_applied = 0
    for fet in fet_map:
        count_inst = len([inst for inst in iterated_ops if inst in fet_map[fet]])
        total_fets_applied += count_inst
    # blocks iterated
    blocks = len([inst for inst in iterated_ops if inst in block_markers])
    # total blocks
    total_blocks = len([inst for inst in ops if inst in block_markers])
    # return total_fets_applied, blocks, total_blocks
    print(pattern, f1.split('/')[-1].split('.')[0], total_fets_applied, blocks, total_blocks)
    return

def sublist(lst1, lst2):
   ls1 = [element for element in lst1 if element in lst2]
   ls2 = [element for element in lst2 if element in lst1]
   return ls1 == ls2

def calculate_complexity(f1):
    global total_functions, total_blocks, total_files, total_edges
    data1 = open(f1, 'r').read()
    if "must point to a Python source that can be compiled" in data1:
        return
    # Add file counts
    total_files += 1
    extract_bc1 = extract_op_args(data1)
    extract_bc1 = [(fn, [i for i in bc if i[1] != 'EXTENDED_ARG']) for fn, bc in extract_bc1] 
    for a in extract_bc1:
        # Add function counts
        total_functions += 1
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        total_blocks += len([inst for inst in ops if inst in block_markers])
        total_edges += len([inst for inst in ops if inst in block_markers]) + len([inst for inst in ops if inst in py_edges])


def batch_apply(folder, func):
    dict_paths = {}
    print(folder)
    for (dirpath, dirnames, filenames) in os.walk(folder):
        # print(dirpath)
        bytecode_disassembled_1 = [f for f in filenames if f.endswith('.dis')]
        dict_paths = {f.split('.')[0]:[dirpath + '/' +f] for f in bytecode_disassembled_1}
        for i in tqdm(dict_paths):
            # if len(dict_paths[i]) != 2: continue
            f1 = dict_paths[i][0]
            # print(i,":", f1)
            func(f1)
batch_apply('orginal_dis_37', calculate_complexity)

'''
otal_functions = 0
total_files= 0
total_blocks = 0
total_edges = 0
'''
print('Total functions:', total_functions )

print('Total Files: ', total_files )
print('Total blocks:', total_blocks )
print('Total edges:', total_edges )
