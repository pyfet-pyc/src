from doctest import FAIL_FAST
from functools import total_ordering
import sys, os, re, difflib

py_jumps = ['FOR_ITER', 'JUMP_FORWARD', 'JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'JUMP_ABSOLUTE', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'CONTINUE_LOOP', 'SETUP_LOOP','SETUP_EXCEPT','SETUP_FINALLY','SETUP_WITH', 'SETUP_ASYNC_WITH','CALL_FINALLY', 'JUMP_IF_NOT_EXC_MATCH']
block_markers = py_jumps + ['RETURN_VALUE']
def get_int(txt):
    if type(txt) == int:
        return txt
    return int(''.join(filter(lambda i: i.isdigit(), txt)))

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

def find_pattern_39 (f1):
    '''
    + -> added by decompiler
    - -> removed by decompiler
    '''
    # print(f1)
    data1 = open(f1, 'r').read()
    extract_bc1 = extract_op_args(data1)
    extract_bc1 = [(fn, [i for i in bc if i[1] != 'EXTENDED_ARG']) for fn, bc in extract_bc1] 
    overall_check = False
    # Pattern 17
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'POP_TOP' and i<= len(ops) -3 :
                # print(i, len(ops))
                if ops[i+1]== 'JUMP_ABSOLUTE' and ops[i+2]== 'JUMP_ABSOLUTE':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P17')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 14
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['COMPARE_OP'] and bc_1[i][2] in ['(>)', '(<)', '(>=)', '(<=)']:
                # print(bc_1[i])
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 in ['STORE_FAST', 'RETURN_VALUE', 'STORE_NAME']: break
                    if op2 == 'COMPARE_OP' and bc_1[j][2] == bc_1[i][2]:
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P14')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
# Pattern 2
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 == 'STORE_FAST': break
                    if op2 == 'RETURN_VALUE' and ops[j+1] == 'SETUP_FINALLY':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j+2, f1, 'P2')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
    # Pattern 11
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_FINALLY':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P11')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 6
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P6')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
    # Pattern 15
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'JUMP_ABSOLUTE':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P15')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 10
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'JUMP_ABSOLUTE' and i<= len(ops) -2 :
                # print(i, len(ops))
                # print(bc_1[i])
                arg = get_int(bc_1[i][3]) # get destination
                # Ignore jump forwards
                if arg > get_int(bc_1[i][0]): continue
                # Get destination of jumpback
                dest = [(ind, z) for ind, z in enumerate(bc_1) if get_int(z[0]) == arg]
                if len(dest) == 0: continue
                ind , dest = dest[0]
                for j, op2 in enumerate(ops):
                    if j < ind or j >= len(ops) -1: continue
                    if op2 in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'GET_ITER', 'FOR_ITER']: break
                    if op2 in ['STORE_FAST', 'RETURN_VALUE']:
                        #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                        # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P10')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
    # Pattern 4
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P4')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break

    # Pattern 16
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE'] and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1] == 'POP_TOP' and ops[i+2] == 'JUMP_ABSOLUTE':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P16')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break

    # Pattern 13
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 in ['STORE_FAST','RETURN_VALUE']: 
                        break
                    # if op2 == 'RAISE_VARARGS': print('RAISE_VARARGS', get_int(bc_1[i][3]), get_int(bc_1[j][0]), i, j, bc_1[i], bc_1[j])
                    if op2 == 'RAISE_VARARGS':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P13')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break

def find_pattern_38 (f1):
    '''
    + -> added by decompiler
    - -> removed by decompiler
    '''
    # print(f1)
    data1 = open(f1, 'r').read()
    extract_bc1 = extract_op_args(data1)
    extract_bc1 = [(fn, [i for i in bc if i[1] != 'EXTENDED_ARG']) for fn, bc in extract_bc1] 
    overall_check = False
    # Pattern 6
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P6')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
    # Pattern 11
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_FINALLY':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P11')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 15
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'JUMP_ABSOLUTE':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P15')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 14
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['COMPARE_OP'] and bc_1[i][2] in ['(>)', '(<)', '(>=)', '(<=)']:
                # print(bc_1[i])
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 in ['STORE_FAST', 'RETURN_VALUE', 'STORE_NAME']: break
                    if op2 == 'COMPARE_OP' and bc_1[j][2] == bc_1[i][2]:
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P14')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
    # Pattern 2
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 == 'STORE_FAST': break
                    if op2 == 'RETURN_VALUE' and ops[j+1] == 'SETUP_FINALLY':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P2')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
    # Pattern 10
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'JUMP_ABSOLUTE' and i<= len(ops) -2 :
                # print(i, len(ops))
                # print(bc_1[i])
                arg = get_int(bc_1[i][3]) # get destination
                # Ignore jump forwards
                if arg > get_int(bc_1[i][0]): continue
                # Get destination of jumpback
                dest = [(ind, z) for ind, z in enumerate(bc_1) if get_int(z[0]) == arg]
                if len(dest) == 0: continue
                ind , dest = dest[0]
                for j, op2 in enumerate(ops):
                    if j < ind or j >= len(ops) -1: continue
                    if op2 in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'GET_ITER', 'FOR_ITER']: break
                    if op2 in ['STORE_FAST', 'RETURN_VALUE']:
                        #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                        # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P10')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
    # Pattern 16
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE'] and i<= len(ops) -2 :
                # print(i, len(ops))
                if get_int(bc_1[i][3]) < get_int(bc_1[i][0]):
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i, f1, 'P16')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 4
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P4')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 17
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'POP_TOP' and i<= len(ops) -3 :
                # print(i, len(ops))
                if ops[i+1]== 'JUMP_ABSOLUTE' and ops[i+2]== 'JUMP_ABSOLUTE':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P17')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break

def find_pattern_37 (f1):
    '''
    + -> added by decompiler
    - -> removed by decompiler
    '''
    # print(f1)
    data1 = open(f1, 'r').read()
    extract_bc1 = extract_op_args(data1)
    extract_bc1 = [(fn, [i for i in bc if i[1] != 'EXTENDED_ARG']) for fn, bc in extract_bc1] 
    overall_check = False
    # Pattern 6
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P6')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
    # Pattern 3
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_LOOP':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P3')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
    # Pattern 10
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'SETUP_LOOP' and i<= len(ops) -2 :
                # print(i, len(ops))
                # print(bc_1[i])
                if len([z for z in bc_1[i:] if z[1] in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE'] and get_int(z[3]) >= get_int(bc_1[i][3])-2 ])>0:
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P10')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return
    # Pattern 11
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_EXCEPT':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P11')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 2
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 == 'STORE_FAST': break
                    if op2 == 'RETURN_VALUE' and ops[j+1] == 'SETUP_EXCEPT':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P2')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
    # Pattern 4
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P4')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 8
        # if overall_check: return   
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'POP_BLOCK' and ops[i+2]== 'JUMP_FORWARD':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P8')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
    # Pattern 13
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 in ['STORE_FAST','RETURN_VALUE']: 
                        break
                    # if op2 == 'RAISE_VARARGS': print('RAISE_VARARGS', get_int(bc_1[i][3]), get_int(bc_1[j][0]), i, j, bc_1[i], bc_1[j])
                    if op2 == 'RAISE_VARARGS' and get_int(bc_1[i][3])< get_int(bc_1[j][0]):
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P13')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
    # Pattern 5
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_LOOP':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P5')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return
    # Pattern 14
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['COMPARE_OP'] and bc_1[i][2] in ['(>)', '(<)', '(>=)', '(<=)']:
                # print(bc_1[i])
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 in ['STORE_FAST', 'RETURN_VALUE', 'STORE_NAME']: break
                    if op2 == 'COMPARE_OP' and bc_1[j][2] == bc_1[i][2]:
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P14')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
def find_pattern_36 (f1):
    '''
    + -> added by decompiler
    - -> removed by decompiler
    '''
    # print(f1)
    data1 = open(f1, 'r').read()
    extract_bc1 = extract_op_args(data1)
    extract_bc1 = [(fn, [i for i in bc if i[1] != 'EXTENDED_ARG']) for fn, bc in extract_bc1] 
    overall_check = False
    # Pattern 3
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_LOOP':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P3')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
    # Pattern 10
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'SETUP_LOOP' and i<= len(ops) -2 :
                # print(i, len(ops))
                # print(bc_1[i])
                if len([z for z in bc_1[i:] if z[1] in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE'] and get_int(z[3]) >= get_int(bc_1[i][3])-2 ])>0:
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i, f1, 'P10')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return
    # Pattern 11
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_EXCEPT':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P11')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 6
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P6')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
    # Pattern 2
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 == 'STORE_FAST': break
                    if op2 == 'RETURN_VALUE' and ops[j+1] == 'SETUP_EXCEPT':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P2')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
    # Pattern 13
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 in ['STORE_FAST','RETURN_VALUE']: 
                        break
                    # if op2 == 'RAISE_VARARGS': print('RAISE_VARARGS', get_int(bc_1[i][3]), get_int(bc_1[j][0]), i, j, bc_1[i], bc_1[j])
                    if op2 == 'RAISE_VARARGS' and get_int(bc_1[i][3])< get_int(bc_1[j][0]):
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P13')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
    # Pattern 4
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P4')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
    # Pattern 8
        # if overall_check: return   
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'POP_BLOCK' and ops[i+2]== 'JUMP_FORWARD':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P8')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
def find_pattern_35 (f1):
    '''
    + -> added by decompiler
    - -> removed by decompiler
    '''
    # print(f1)
    data1 = open(f1, 'r').read()
    extract_bc1 = extract_op_args(data1)
    overall_check = False
    # Pattern 6
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P6')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
    # Pattern 2
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 == 'STORE_FAST': break
                    if op2 == 'RETURN_VALUE' and ops[j+1] == 'SETUP_EXCEPT':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j+1, f1, 'P2')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
    # Pattern 11
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_EXCEPT':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P11')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return 
    # Pattern 4
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P4')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return    
    # Pattern 8
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'POP_BLOCK' and ops[i+2]== 'JUMP_FORWARD':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P8')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return  
    # Pattern 3
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_LOOP':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P3')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
                   
    # Pattern 11
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['JUMP_FORWARD']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 == 'STORE_FAST': break
                    if op2 == 'RETURN_VALUE' and ops[j+1] == 'SETUP_EXCEPT':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P11')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
    # Pattern 13
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['JUMP_IF_FALSE_OR_POP', 'JUMP_IF_TRUE_OR_POP', 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 in ['STORE_FAST','RETURN_VALUE']: 
                        break
                    # if op2 == 'RAISE_VARARGS': print('RAISE_VARARGS', get_int(bc_1[i][3]), get_int(bc_1[j][0]), i, j, bc_1[i], bc_1[j])
                    if op2 == 'RAISE_VARARGS' and get_int(bc_1[i][3])< get_int(bc_1[j][0]):
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j, f1, 'P13')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        # if overall_check: return
        # if overall_check: return 
def find_pattern_34 (f1):
    '''
    + -> added by decompiler
    - -> removed by decompiler
    '''
    # print(f1)
    data1 = open(f1, 'r').read()
    extract_bc1 = extract_op_args(data1)
    overall_check = False
    # Pattern 3
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_LOOP':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P3')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
    # Pattern 10
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'SETUP_LOOP' and i<= len(ops) -2 :
                # print(i, len(ops))
                # print(bc_1[i])
                if len([z for z in bc_1[i:] if z[1] in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE'] and get_int(z[3]) >= get_int(bc_1[i][3])-2 ])>0:
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i, f1, 'P10')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return
    # Pattern 7
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_EXCEPT':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P7')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return
    # Pattern 6
    # if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'LOAD_CONST'and ops[i+3]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+3, f1, 'P6')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        # if overall_check: return  
    
def find_pattern_27 (f1):
    '''
    + -> added by decompiler
    - -> removed by decompiler
    '''
    # print(f1)
    data1 = open(f1, 'r').read()
    # if "Traceback (most recent call last):" in data1: 
    #     # print("ERRRRROR:EXPLICIT")
    #     # print("Explicit error")
    #     return
    # print("Extracting bc")
    extract_bc1 = extract_op_args(data1)
    # print("Extracted bc")
    # print(extract_bc1)
    # print(f1)
    # if '100097' in f1: print(f1, "Processing")
    overall_check = False
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        # Pattern 1
        ops = [i[1] for i in bc_1 if i[1]]
        for i in bc_1:
            if i[1] in py_jumps: count_blocks+=1
            if i[1] == "RETURN_VALUE":
                for j in bc_1:
                    if j[0] > i[0] and j[1] == 'BUILD_MAP':
                        br_flag = False
                        for ind, k in enumerate(bc_1):
                            if k[0] < j[0]: continue
                            if k[1] in ['STORE_FAST']: 
                                br_flag = True
                                break
                            if k[1] in ['RETURN_VALUE']:
                                check = True 
                                overall_check = True
                                # print('R1',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                                # print(f1.split('/')[-1].split('.')[0])
                                calculate_stats(ops, ind, f1, 'P1')#
                                break
                        if br_flag or check: break
            if check: break
    # Pattern 2
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']:
                for j, op2 in enumerate(ops):
                    if j <= i or j >= len(ops) -1: continue
                    if op2 == 'STORE_FAST': break
                    if op2 == 'RETURN_VALUE' and ops[j+1] == 'SETUP_EXCEPT':
                        count_blocks = len([z for z in ops[:j] if z in py_jumps])
                        # print('R7',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                        overall_check = True
                        calculate_stats(ops, j+1, f1, 'P2')#print(f1.split('/')[-1].split('.')[0])
                        break
            if overall_check: break
        if overall_check: return
                            
    # Pattern 3
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_LOOP':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+1, f1, 'P3')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return

    # Pattern 4
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P4')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return    

    # Pattern 5
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_LOOP':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P5')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
    # Pattern 6
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RAISE_VARARGS' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'LOAD_CONST' and ops[i+2]== 'MAKE_FUNCTION':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P6')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
    # Pattern 7
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -2 :
                # print(i, len(ops))
                if ops[i+1]== 'SETUP_EXCEPT':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P7')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
    # Pattern 8
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'RETURN_VALUE' and i<= len(ops) -4 :
                # print(i, len(ops))
                if ops[i+1]== 'POP_BLOCK' and ops[i+2]== 'JUMP_FORWARD':
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P8')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return    
    # Pattern 9
    if overall_check: return
    for a in extract_bc1:
        fn_name1, bc_1 = a
        check = False
        
        #total_blocks = len([i[1] for i in bc_1 if i[1] in py_jumps])
        count_blocks = 0
        ops = [i[1] for i in bc_1 if i[1]]
        for i, op in enumerate(ops):
            if op == 'JUMP_ABSOLUTE' and i<= len(ops) -2 :
                # print(i, len(ops))
                # print(bc_1[i][1], op, i, len(bc_1), len(ops), bc_1[i], bc_1[i+1])
                if ops[i+1]== 'JUMP_FORWARD' and bc_1[i][3] == bc_1[i+1][3]:
                    #count_blocks = len([z for z in ops[:i] if z in py_jumps])
                    # print('R4',":",f1.split('/')[-1].split('.')[0], ':', fn_name1, ':', ':', count_blocks, ':', total_blocks)
                    overall_check = True
                    calculate_stats(ops, i+2, f1, 'P9')#print(f1.split('/')[-1].split('.')[0])
                    break
            if overall_check: break
        if overall_check: return
        #     continue
        # bytecode_diff = list(zip(bc_1, bc_2))
        # check = False
        # for x, y in bytecode_diff:
        #     op1 = x[1]
        #     op2 = y[1]
        #     if op1 != op2:
        #         print("Incorrect opcodes", op1, op2, " in ", fn_name1, fn_name2)
        # if check: continue
        

def batch_apply(folder, func):
    dict_paths = {}
    # print(folder)
    for (dirpath, dirnames, filenames) in os.walk(folder):
        # print(dirpath)
        bytecode_disassembled_1 = [f for f in filenames if f.endswith('.dis')]
        dict_paths = {f.split('.')[0]:[dirpath + '/' +f] for f in bytecode_disassembled_1}
        for i in dict_paths:
            # if len(dict_paths[i]) != 2: continue
            f1 = dict_paths[i][0]
            # print(i,":", f1)
            func(f1)
            # break
batch_apply('test_pycdc/segfault27', find_pattern_27)
batch_apply('test_pycdc/segfault34', find_pattern_34)
batch_apply('test_pycdc/segfault35', find_pattern_35)
batch_apply('test_pycdc/segfault36', find_pattern_36)
batch_apply('test_pycdc/segfault37', find_pattern_37)
batch_apply('test_pycdc/segfault38', find_pattern_38)
batch_apply('test_pycdc/segfault39', find_pattern_39)
