import sys, os, re
error_37count = 0
error_37count_1 = 0
error_37count_3 = 0
folders = [
    # 'py27_py', 
    'py37_py', 
    # 'py38_py'
    ]
jump_instr_37 = []
def extract_op_args(bc):
    data = bc.split('\n')
    # ignore first line
    if 'code object' in data[0]:
        data = data[1:]
    opcode_re = re.compile(r'\d+\s*([A-Z]+[_]*)+[ ]*\d*')
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
    return lst
## PATTERNSSS
def pattern_1_37(c1, c2):
    # check for in `with` has `else` added to an if which did not exist
    # c1 = original
    # c2 = decompiled
    global error_37count_1
    start = "SETUP_WITH"
    c1_with = []
    c2_with = []
    for iter in range(0,len(c1)):
        if c1[iter][1] == start:
            ind = [i for i, v in enumerate(c1) if v[0] == str(int(c1[iter][2])+int(c1[iter][0]))][0]
           
            c1_with += [c1[iter:ind]]
    for iter in range(0,len(c2)):
        if c2[iter][1] == start:
            ind = [i for i, v in enumerate(c2) if v[0] == str(int(c2[iter][2])+int(c2[iter][0]))][0]
            c2_with += [c2[iter:ind]]
    if len(c1_with) == 0 or len(c1_with) != len(c2_with): return False
    # print(len(c1_with), len(c2_with))
    for iter, tup in enumerate(c1_with):
        tup1 = tup # original
        tup2 = c2_with[iter] # decompiled
        # print(tup1, tup2)
        count_if_1 =  len([i for i, v in enumerate(tup1) if v[1] in ['POP_JUMP_IF_FALSE']])
        count_if_2 =  len([i for i, v in enumerate(tup2) if v[1] in ['POP_JUMP_IF_FALSE']])
        count_else_1 = len([i for i, v in enumerate(tup1) if v[1] in ['JUMP_FORWARD']])
        count_else_2 = len([i for i, v in enumerate(tup2) if v[1] in ['JUMP_FORWARD']])
        # print(count_if_1, count_if_2, count_else_1, count_else_2)
        if count_if_1 == count_if_2 and count_else_2 > count_else_1:
            error_37count_1 += 1
            return True
    return False
        
def pattern_3_37(c1, c2):
    # check for in `with` has `else` added to an if which did not exist
    # c1 = original
    # c2 = decompiled
    global error_37count_3
    start = "POP_JUMP_IF_TRUE"
    c1_ifnot = []
    c2_ifnot = []
    for iter in range(0,len(c1)):
        if c1[iter][1] == start:
            ind = [i for i, v in enumerate(c1) if i>iter and v[1] in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']]
            if len(ind) == 0: continue
            ind = ind[0]
            c1_ifnot += [c1[iter:ind]]
    for iter in range(0,len(c2)):
        if c2[iter][1] == start:
            ind = [i for i, v in enumerate(c2) if i>iter and v[1] in ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE']]
            if len(ind) == 0: continue
            ind = ind[0]
            c2_ifnot += [c2[iter:ind]]
    if len(c1_ifnot) == 0 or len(c1_ifnot) != len(c2_ifnot): return False
    # print(len(c1_ifnot), len(c2_ifnot))
    for iter, tup in enumerate(c1_ifnot):
        tup1 = tup # original
        tup2 = c2_ifnot[iter] # decompiled
        # print(tup1, tup2)
        count_jf_1 =  len([i for i, v in enumerate(tup1) if v[1] in ['JUMP_FORWARD']])
        count_jf_2 =  len([i for i, v in enumerate(tup2) if v[1] in ['JUMP_FORWARD']])
        # print(count_if_1, count_if_2, count_else_1, count_else_2)
        if count_jf_2 > count_jf_1:
            error_37count_3 += 1
            return True
    return False
    
##

def check_for_pattern37(c1, c2):
    global error_37count
    # c1 = original one
    # c2 = decompiled one
    # if len(c1) == len(c2): return False
    check = False
    # print(len(c1), len(c2))
    if pattern_1_37(c1, c2): 
        print('Pattern 1 Found!')
        error_37count += 1
        check = True
        # return True
    if pattern_3_37(c1, c2):
        print('Pattern 3 Found!')
        error_37count += 1
        check = True
    return check


def comp_py_37(folder):
    for (dirpath, dirnames, filenames) in os.walk(folder):
        bytecode_disassembled = [f for f in filenames if f.endswith('.d.py.dis')]
        zipped_dis_orig = [(folder + '/' +f[:-9]+'.py.dis' , folder + '/' +f) for f in bytecode_disassembled]
        for org, dec in zipped_dis_orig:
            if not os.path.exists(org) or not os.path.exists(dec): continue
            # if "_bootstrap" not in org: continue
            # print(org, dec)
            data1 = open(org,'r').read()
            if 'FAILED_DIS' in data1: continue
            data1 = "".join([s for s in data1.splitlines(True) if s.strip()])
            data2 = open(dec,'r').read()
            if 'FAILED_DIS' in data2: continue
            data2 = "".join([s for s in data2.splitlines(True) if s.strip()])
            data1 = data1.split('\nDisassembly of')
            data2 = data2.split('\nDisassembly of')
            # print(data1[:2])
            # print(data2[:2])
            comparison = list(zip(data1, data2))
            count = 0
            for a,b in comparison:
                # print(count)
                a= extract_op_args(a)
                b= extract_op_args(b)
                temp = check_for_pattern37(a,b)
                if temp:

                    print("Error in:", org)
                count += 1
                # break
                
            
            # break
        break

### Python 3.7 - 1653 
comp_py_37('py37_py')
print("Error1:", error_37count_1/1653) # 1.149%
print("Erro2:", 2/1653) # 0.1209%
print("Error3:", error_37count_3/1653) # 9.31%
print("Total errors:", error_37count/1653)