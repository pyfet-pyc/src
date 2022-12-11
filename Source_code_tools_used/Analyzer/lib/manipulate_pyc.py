import sys, types, dis, traceback
import readpyc
import opcode, re
try:
    input_f = sys.argv[1]
    output_f = sys.argv[2]
except:
    print("no input and output file")

jmp_op_boolean_chain = [
    111, # Boolean expression "AND" JUMP_IF_FALSE_OR_POP
    112, # Boolean expression "OR" JUMP_IF_TRUE_OR_POP
    # 113, # Absolute jump - Can skip since no boolean
    114, # Conditional POP_JUMP_IF_FALSE
    115, # Conditional POP_JUMP_IF_TRUE
    # 121, # No idea where this is used - jabs_op('JUMP_IF_NOT_EXC_MATCH', 121)
]
terminate_boolean_chain = [
    90, # name_op('STORE_NAME', 90) 
    95, # name_op('STORE_ATTR', 95) # Index in name list
    97, # name_op('STORE_GLOBAL', 97)     # ""
    125, # def_op('STORE_FAST', 125)       # Local variable number
    83, # def_op('RETURN_VALUE', 83)
    86, # def_op('YIELD_VALUE', 86)
]
 # a and b and/or c # goes on

'''
jrel_op('JUMP_FORWARD', 110)    # Number of bytes to skip
jabs_op('JUMP_IF_FALSE_OR_POP', 111) # Target byte offset from beginning of code
jabs_op('JUMP_IF_TRUE_OR_POP', 112)  # ""
jabs_op('JUMP_ABSOLUTE', 113)        # ""
jabs_op('POP_JUMP_IF_FALSE', 114)    # ""
jabs_op('POP_JUMP_IF_TRUE', 115)     # ""

Finer-grained -> less generic
More generic -> 

whitelist 
regex `*`
'''

def find_sub_list(sl,l):
    results=[]
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            return ind,ind+sll-1

def find_pattern_code(code, lst):
    
    for offset in range(0, len(code), 2):
        if code[offset] == opcode.EXTENDED_ARG: continue
        check = True
        last_offset = offset
        for i, op in enumerate(lst):
            check_lst = False
            for offset_check in range(last_offset, len(code), 2):
                if code[offset_check] == opcode.EXTENDED_ARG: continue
                print(opcode.opname[code[offset_check]], opcode.opname[op])
                if code[offset_check] == op:
                    print("Match", offset_check)
                    last_offset += 2
                    check_lst = True
                    break
                else:
                    break
            if check_lst == False: 
                check = False
                break
        if check == True: return offset, last_offset
    return None

def get_local_var_name(co_varnames):
    i = 1
    while True:
        if "t{}_annotated".format(i) not in co_varnames:
            return "t{}_annotated".format(i)
        i = i + 1
def get_op_arg_offset(code, offset):
    for off_set, op, arg in dis._unpack_opargs(code):
        if offset == off_set: return op, arg
    return None

def get_prev_offset_skipping_extended(code, offset):
    offset = offset -2
    while offset >= 0 and code[offset] == opcode.EXTENDED_ARG:
        offset = offset -2 # keep going back until proper instruction
    return offset 

def print_co_info(co):
    print(co)
    print("argcount:", co.co_argcount)
    if sys.version_info[1] > 7:
        print("co_posonlyargcount:", co.co_posonlyargcount) #Add this in Python 3.8+
    print("co_kwonlyargcount:", co.co_kwonlyargcount)  #Add this in Python3
    print("co_nlocals:",co.co_nlocals)
    print("co_stacksize:",co.co_stacksize)
    print("co_flags:",co.co_flags)
    print("code:",co.co_code)
    print("co_consts:",co.co_consts)
    print("co_names:",co.co_names)
    print("co_varnames:",co.co_varnames)
    print("co_filename:",co.co_filename)
    print("co_name:",co.co_name)
    print("co_firstlineno:",co.co_firstlineno)
    print("co_lnotab:",co.co_lnotab)   # In general, You should adjust this
    print("co_freevars:",co.co_freevars)
    print("co_cellvars:",co.co_cellvars)
    print("Dis:")
    print("="*5)
    dis.dis(co.co_code)
    print("="*5)
    # )

# Get the Code object with function name 'fn_name' in 'co'
def get_co_fn(co, fn_name):
    # print(co.co_name, fn_name)
    # print(type(co.co_name), type(fn_name))
    # print(len(co.co_name), len(fn_name))
    if fn_name == co.co_name: 
        return co
    for const in co.co_consts:
        if isinstance(const, types.CodeType):
            temp = get_co_fn(const, fn_name)
            if temp is not None: return temp
    return None

# Update the Code object corresponding with function name 'fn_name' in 'co' with `new_co`
def recursively_update_target_fn(co, fn_name, new_co):
    if fn_name == co.co_name: 
        return new_co
    constants = list(co.co_consts)
    is_changed = False
    for i, const in enumerate(co.co_consts):
        if isinstance(const, types.CodeType):
            temp = recursively_update_target_fn(const, fn_name, new_co)
            if temp is not None: 
                constants[i] = temp
                is_changed = True
                print("Changed the function:", fn_name)
                # dis.dis(temp)
                continue
        constants[i] = const
    if is_changed:
        if sys.version_info[1] > 7:
            return types.CodeType(
            co.co_argcount,
            co.co_posonlyargcount, #Add this in Python 3.8+
            co.co_kwonlyargcount,  #Add this in Python3
            co.co_nlocals,
            co.co_stacksize,
            co.co_flags,
            co.co_code,
            tuple(constants),
            co.co_names,
            co.co_varnames,
            co.co_filename,
            co.co_name,
            co.co_firstlineno,
            co.co_lnotab,   # In general, You should adjust this
            co.co_freevars,
            co.co_cellvars
        )
        else:
            return types.CodeType(
                co.co_argcount,
                # co.co_posonlyargcount, #Add this in Python 3.8+
                co.co_kwonlyargcount,  #Add this in Python3
                co.co_nlocals,
                co.co_stacksize,
                co.co_flags,
                co.co_code,
                tuple(constants),
                co.co_names,
                co.co_varnames,
                co.co_filename,
                co.co_name,
                co.co_firstlineno,
                co.co_lnotab,   # In general, You should adjust this
                co.co_freevars,
                co.co_cellvars
            )
            
        
    return None

def analyse_co_fn(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return
    print_co_info(target_co)
    
    dis.show_code(target_co)
    for x in range(0, len(target_co.co_code), 2):
        print(target_co.co_code[x], end=", ")
    print("")
    target_offsets = [off_set for off_set, op, arg in dis._unpack_opargs(target_co.co_code) if op in jmp_op]
    print(target_offsets)
    all_sets = []
    for x in target_offsets:
        temp = []
        for off_set in range(x, len(target_co.co_code), 2):
            op = target_co.co_code[off_set]
            if op in terminate_boolean_chain:
                print("break", op, off_set)
                break
            if op in jmp_op: 
                temp.append(off_set)
        print(temp)
        # if len(temp) > 1: all_sets.append(temp)
        all_sets = all_sets + [temp] if len(temp) > 1 else all_sets
    print(all_sets)

    return
    constants = list(target_co.co_consts)
    for i, const in enumerate(constants):
        if isinstance(const, types.CodeType):
            pass
            # print("codetype:",const)
            # print("function body:", const)
            # print("function consts:", const.co_consts)
            # print("function name:", const.co_name)
        else:
            if isinstance(const, str) and "hello" in const:
                constants[i] = 'goodbye world'
                # print('updated')
    new_target_co = types.CodeType(
        target_co.co_argcount,
        target_co.co_posonlyargcount, #Add this in Python 3.8+
        target_co.co_kwonlyargcount,  #Add this in Python3
        target_co.co_nlocals,
        target_co.co_stacksize,
        target_co.co_flags,
        target_co.co_code,
        tuple(constants),
        target_co.co_names,
        target_co.co_varnames,
        target_co.co_filename,
        target_co.co_name,
        target_co.co_firstlineno,
        target_co.co_lnotab,   # In general, You should adjust this
        target_co.co_freevars,
        target_co.co_cellvars
    )
    # print(new_target_co.co_consts)
    # print(new_target_co.co_code)
    # dis.dis(new_target_co)
    return recursively_update_target_fn(co, fn_name, new_target_co)
    
    # target_co.co_consts = tuple(constants)

def create_dummy_inst(arg = 0):
    a = "global z; z=z;"
    #a = "print('');"
    c = compile(a, '<string>', 'exec')
    dis.dis(c)
    # print(c.co_code)
    # print_co_info(c)
    dummy_inst = c.co_code[:4]
    # dummy_inst[]
    # print(arg, bytes(arg))
    arg = bytes([arg])
    print('before change:', dummy_inst)
    for i, inst in enumerate(dummy_inst):
       if i%2 == 1:
           dummy_inst = dummy_inst[:i] + arg + dummy_inst[i+1:]
    #print('changed:', dummy_inst)
    
    # print(c.co_nlocals)
    # print(c.co_stacksize)
    # print("dummy instruction info")
    # new_co = types.CodeType(
    #     c.co_argcount,
    #     # c.co_posonlyargcount, #Add this in Python 3.8+
    #     c.co_kwonlyargcount,  #Add this in Python3
    #     c.co_nlocals,
    #     c.co_stacksize,
    #     c.co_flags,
    #     dummy_inst,
    #     c.co_consts,
    #     c.co_names,
    #     c.co_varnames,
    #     c.co_filename,
    #     c.co_name,
    #     c.co_firstlineno,
    #     c.co_lnotab,   # In general, You should adjust this
    #     c.co_freevars,
    #     c.co_cellvars
    # )
    # dis.dis(new_co)
    return dummy_inst
    # for const in c.co_consts:
    #     print(const)

def update_codebyte(code, offset, add_value):
    # Below we just add to try not changing anything
    value = code[offset] + add_value
    # print("[update_codebyte]:Value:{}, add_val:{} at offset:{} with original value:{}".format( value, add_value, offset, code[offset]))
    if value <256 and value >= 0:
        # print('Update curr Val:', value)
        return code[:offset] + bytes([value]) + code[offset+1:]
    # dis.dis(code)
    op = offset - 3 # Get previous op
    # Check for extended arg start
    # print(op)
    while op > 0 and code[op] == opcode.EXTENDED_ARG: 
        op = op - 2
        # print(op)
    if op > 0: op = op + 2 # Get last Extended arg
    elif op < 0: op = offset - 1
    # op will be either Extended arg or offset - 1
    # print("end:",op)
    # Next we see if we can try to carry value to extended args
    extended_arg = 0
    count = 0 # number of bytes right now
    arg = 0
    # print("op:{}, offset{}".format(op, offset), code[offset - 3], opcode.EXTENDED_ARG)
    for i in range(op, offset, 2):
        temp_op = code[i]
        arg = code[i+1] | extended_arg
        extended_arg = (arg << 8) if temp_op == opcode.EXTENDED_ARG else 0
        count = count + 1
    if arg + add_value < pow(2, (count* 8)):
        final_arg = arg + add_value
        ## Update all extended args
        # print("fin:",final_arg, arg, add_value)
        for x in range(count):
            n = x # 0th byte
            goal = 0xFF << (8 * n)
            val_target = (final_arg & goal) >> (8 * n)
            val_current = (arg & goal) >> (8 * n)
            # Update code
            # print("curr:{}, targer:{}".format(val_current, val_target))
            code = update_codebyte(code, offset - (2 * x), val_target - val_current)
        # All extended args updated and can now go back to normal
        # print("[update_codebyte]:returning w/o adding EA. curr Val:", code[offset])
        return code
    ## Add extended Args now
    final_arg = arg + add_value
    bytes_req = 1
    # print(final_arg, pow(2, bytes_req * 8))
    while final_arg > pow(2, bytes_req * 8) -1: bytes_req = bytes_req + 1
    # Update existing args and extended args
    print ("ERR:EXTENDED ARGS NOT RESOLVED!!!")
    return code
    for x in range(count):
        n = x # 0th byte
        goal = 0xFF << (8 * n)
        val_target = (final_arg & goal) >> (8 * n)
        val_current = (arg & goal) >> (8 * n)
        # Update code
        # print("UPDATE EXTENDED ARG", val_target, val_current)
        code = update_codebyte(code, offset - (2 * x), val_target - val_current)
    # Add Extended args for the remaining
    # print("ADDDING EXTENDED ARG", count, bytes_req)
    for x in range(count, bytes_req):
        n = x # 0th byte
        goal = 0xFF << (8 * n)
        val_target = (final_arg & goal) >> (8 * n)
        # print("ADDDING EXTENDED ARG", val_target, final_arg, n)
        # print("l:",len(code))
        code = update_jump_offsets(code, bytes([opcode.EXTENDED_ARG]) + 
        bytes([val_target]), offset + 1 - (2*count))
        # print("l:",len(code))
        # code = code[:offset + 1 - (2*count)] + bytes([opcode.EXTENDED_ARG]) + bytes([val_current]) + code[offset + 1 - (2*count):]
        pass
    print("[update_codebyte]: Exit with adding extended args")
    return code
    # Extended ARGS:
    '''
    144 X
    Inst Args
    final value: (X << 8) | Args
    Note: 1 byte is 8 bits
    '''
    raise Exception("Value [{}] exceeds 255, prev inst: [{}], curr inst:[{}], offset {}".format(value, code[offset-3],code[offset-1], offset))

def update_jump_offsets_no_jumpforward(code, code_to_add, offset):
    # This is a special version which does not fix jumpforward if it is jumping to the exact target instrumentation
    code = code[:offset] + code_to_add + code[offset:]
    temp_code = code
    for off_set, op, arg in dis._unpack_opargs(code):
        if off_set < (offset + len(code_to_add)) and off_set >= offset:
            # Skip this code
            # This is our instrumented code so ignore
            continue
        if op in opcode.hasjabs:
            # Check only argument and update it
            if arg > offset: 
                # Since the target is in offset range
                # Anything after offset should be updated
                # print("arg:" ,arg, op)
                # print((code[off_set-1]<< 8),code[off_set], code[off_set+1],code[off_set-2], code[off_set-1], arg, opcode.EXTENDED_ARG , code[off_set] == opcode.EXTENDED_ARG)
                temp_code = update_codebyte(temp_code, off_set + 1, len(code_to_add))
        elif op in opcode.hasjrel:
            # Target here is off_set + 2 + arg
            # So if the new instruction is in this region:
            # off_set + 2 [  CHECK THIS AREA  ]  off_set + 2 + arg
            if offset > off_set and offset <= off_set + 2 + arg:
                # Cater ot SETUP_LOOP
                if sys.version_info[1] <= 7 and op == opcode.opmap['SETUP_LOOP']:
                    # Get pop_block for this
                    # print("SETUP LOOP", off_set)
                    offset_POP_BLOCK = None
                    setup_l_count = 1
                    # print(list(range(off_set + 2, len(temp_code), 2)))
                    for os_temp in range(off_set + 2, len(temp_code), 2):
                        if temp_code[os_temp] == opcode.opmap['SETUP_LOOP']:
                            # print("SETUP_LOOP!!", os_temp)
                            setup_l_count = setup_l_count + 1
                        elif temp_code[os_temp] == opcode.opmap['POP_BLOCK'] and temp_code[os_temp - 2] == opcode.opmap['JUMP_ABSOLUTE']:
                            print('POP_BLOCK!!', os_temp)
                            if setup_l_count == 1:
                                offset_POP_BLOCK = os_temp
                                break
                            else:
                                setup_l_count = setup_l_count - 1
                    # Use pop_block offset to check it is right before the instrumented code
                    # print("SETUP LOOP", off_set, offset_POP_BLOCK)
                    
                    if offset_POP_BLOCK == offset - 2:
                    
                        # now make sure loop jump rel is to this
                        value_to_add = (offset_POP_BLOCK - off_set) - arg
                        # print("SETUP LOOP UPDATED" , arg, value_to_add, offset_POP_BLOCK - off_set)
                        temp_code = update_codebyte(temp_code, off_set + 1, value_to_add)
                        continue
                # Update
                # print("arg:" ,arg)
                # print(code[off_set], code[off_set+1], arg, opcode.EXTENDED_ARG)
                if offset < off_set + 2 + arg:
                    temp_code = update_codebyte(temp_code, off_set + 1, len(code_to_add))
    # Update SETUP LOOP
    return temp_code

def update_jump_offsets(code, code_to_add, offset):
    code = code[:offset] + code_to_add + code[offset:]
    temp_code = code
    for off_set, op, arg in dis._unpack_opargs(code):
        if off_set < (offset + len(code_to_add)) and off_set >= offset:
            # Skip this code
            # This is our instrumented code so ignore
            continue
        if op in opcode.hasjabs:
            # Check only argument and update it
            if arg > offset: 
                # Since the target is in offset range
                # Anything after offset should be updated
                # print("arg:" ,arg, op)
                # print((code[off_set-1]<< 8),code[off_set], code[off_set+1],code[off_set-2], code[off_set-1], arg, opcode.EXTENDED_ARG , code[off_set] == opcode.EXTENDED_ARG)
                temp_code = update_codebyte(temp_code, off_set + 1, len(code_to_add))
        elif op in opcode.hasjrel:
            # Target here is off_set + 2 + arg
            # So if the new instruction is in this region:
            # off_set + 2 [  CHECK THIS AREA  ]  off_set + 2 + arg
            if offset > off_set and offset <= off_set + 2 + arg:
                # Cater ot SETUP_LOOP
                if sys.version_info[1] <= 7 and op == opcode.opmap['SETUP_LOOP']:
                    # Get pop_block for this
                    # print("SETUP LOOP", off_set)
                    offset_POP_BLOCK = None
                    setup_l_count = 1
                    # print(list(range(off_set + 2, len(temp_code), 2)))
                    for os_temp in range(off_set + 2, len(temp_code), 2):
                        if temp_code[os_temp] == opcode.opmap['SETUP_LOOP']:
                            # print("SETUP_LOOP!!", os_temp)
                            setup_l_count = setup_l_count + 1
                        elif temp_code[os_temp] == opcode.opmap['POP_BLOCK'] and temp_code[os_temp - 2] == opcode.opmap['JUMP_ABSOLUTE']:
                            print('POP_BLOCK!!', os_temp)
                            if setup_l_count == 1:
                                offset_POP_BLOCK = os_temp
                                break
                            else:
                                setup_l_count = setup_l_count - 1
                    # Use pop_block offset to check it is right before the instrumented code
                    # print("SETUP LOOP", off_set, offset_POP_BLOCK)
                    
                    if offset_POP_BLOCK == offset - 2:
                    
                        # now make sure loop jump rel is to this
                        value_to_add = (offset_POP_BLOCK - off_set) - arg
                        # print("SETUP LOOP UPDATED" , arg, value_to_add, offset_POP_BLOCK - off_set)
                        temp_code = update_codebyte(temp_code, off_set + 1, value_to_add)
                        continue
                # Update
                # print("arg:" ,arg)
                # print(code[off_set], code[off_set+1], arg, opcode.EXTENDED_ARG)
                temp_code = update_codebyte(temp_code, off_set + 1, len(code_to_add))
    # Update SETUP LOOP
    return temp_code

def update_jump_offsets_3_9(code, code_to_add, offset):
    code = code[:offset] + code_to_add + code[offset:]
    temp_code = code
    for off_set, op, arg in dis._unpack_opargs(code):
        if off_set < (offset + len(code_to_add)) and off_set >= offset:
            # Skip this code
            # This is our instrumented code so ignore
            continue
        if op in opcode.hasjabs or op == 121:
            # Check only argument and update it
            if arg > offset: 
                # Since the target is in offset range
                # Anything after offset should be updated
                # print("arg:" ,arg, op)
                # print((code[off_set-1]<< 8),code[off_set], code[off_set+1],code[off_set-2], code[off_set-1], arg, opcode.EXTENDED_ARG , code[off_set] == opcode.EXTENDED_ARG)
                temp_code = update_codebyte(temp_code, off_set + 1, len(code_to_add))
        elif op in opcode.hasjrel and op != 162:
            # Target here is off_set + 2 + arg
            # So if the new instruction is in this region:
            # off_set + 2 [  CHECK THIS AREA  ]  off_set + 2 + arg
            if offset > off_set and offset <= off_set + 2 + arg:
                # Cater ot SETUP_LOOP
                if sys.version_info[1] <= 7 and op == opcode.opmap['SETUP_LOOP']:
                    # Get pop_block for this
                    # print("SETUP LOOP", off_set)
                    offset_POP_BLOCK = None
                    setup_l_count = 1
                    # print(list(range(off_set + 2, len(temp_code), 2)))
                    for os_temp in range(off_set + 2, len(temp_code), 2):
                        if temp_code[os_temp] == opcode.opmap['SETUP_LOOP']:
                            # print("SETUP_LOOP!!", os_temp)
                            setup_l_count = setup_l_count + 1
                        elif temp_code[os_temp] == opcode.opmap['POP_BLOCK'] and temp_code[os_temp - 2] == opcode.opmap['JUMP_ABSOLUTE']:
                            print('POP_BLOCK!!', os_temp)
                            if setup_l_count == 1:
                                offset_POP_BLOCK = os_temp
                                break
                            else:
                                setup_l_count = setup_l_count - 1
                    # Use pop_block offset to check it is right before the instrumented code
                    # print("SETUP LOOP", off_set, offset_POP_BLOCK)
                    
                    if offset_POP_BLOCK == offset - 2:
                    
                        # now make sure loop jump rel is to this
                        value_to_add = (offset_POP_BLOCK - off_set) - arg
                        # print("SETUP LOOP UPDATED" , arg, value_to_add, offset_POP_BLOCK - off_set)
                        temp_code = update_codebyte(temp_code, off_set + 1, value_to_add)
                        continue
                # Update
                # print("arg:" ,arg)
                # print(code[off_set], code[off_set+1], arg, opcode.EXTENDED_ARG)
                temp_code = update_codebyte(temp_code, off_set + 1, len(code_to_add))
    # Update SETUP LOOP
    return temp_code

def update_jump_offsets_remove(code, offset):
    prev_offset = get_prev_offset_skipping_extended(code, offset)
    code = code[:prev_offset+2] + code[offset+2:]
    # dis.dis(code)
    temp_code = code
    for off_set, op, arg in dis._unpack_opargs(code):
        if op in opcode.hasjabs:
            # Check only argument and update it
            if arg > offset: 
                # Since the target is in offset range
                # Anything after offset should be updated
                # print("arg:" ,arg, op)
                # print((code[off_set-1]<< 8),code[off_set], code[off_set+1],code[off_set-2], code[off_set-1], arg, opcode.EXTENDED_ARG , code[off_set] == opcode.EXTENDED_ARG)
                temp_code = update_codebyte(temp_code, off_set + 1, - (offset - prev_offset))
        elif op in opcode.hasjrel:
            # Target here is off_set + 2 + arg
            # So if the new instruction is in this region:
            # off_set + 2 [  CHECK THIS AREA  ]  off_set + 2 + arg
            if offset > off_set and offset <= off_set + 2 + arg:
                # Update
                # print("arg:" ,arg)
                # print(code[off_set], code[off_set+1], arg, opcode.EXTENDED_ARG)
                temp_code = update_codebyte(temp_code, off_set + 1, - (offset - prev_offset))
    # Update SETUP LOOP
    return temp_code

def set_at_offset(co, offset, fn_name, new_inst):
    print ("Offset:{} Function Name:{}".format(offset, fn_name))
    target_co = get_co_fn(co, fn_name)
    print(type(target_co), type(co))
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return
    
    dummy_inst = create_dummy_inst(len(target_co.co_names))
    code = target_co.co_code
    code = code[:offset] + dummy_inst + code[offset+4:]
    #code = update_jump_offsets(target_co.co_code, dummy_inst, offset)
    #dis.dis(code)
    #print(len(code))
    # print_co_info(target_co)
    if sys.version_info[1] > 7:
        final_co =  types.CodeType(
        target_co.co_argcount,
        # target_co.co_posonlyargcount, #Add this in Python 3.8+
        target_co.co_kwonlyargcount,  #Add this in Python3
        target_co.co_nlocals,
        target_co.co_stacksize,
        target_co.co_flags,
        code,
        target_co.co_consts,
        tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_varnames))]),
        target_co.co_varnames,
        target_co.co_filename,
        target_co.co_name,
        target_co.co_firstlineno,
        target_co.co_lnotab,   # In general, You should adjust this
        target_co.co_freevars,
        target_co.co_cellvars
    )
    else:
        final_co =  types.CodeType(
        target_co.co_argcount,
        target_co.co_posonlyargcount, #Add this in Python 3.8+
        target_co.co_kwonlyargcount,  #Add this in Python3
        target_co.co_nlocals,
        target_co.co_stacksize,
        target_co.co_flags,
        code,
        target_co.co_consts,
        tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_varnames))]),
        target_co.co_varnames,
        target_co.co_filename,
        target_co.co_name,
        target_co.co_firstlineno,
        target_co.co_lnotab,   # In general, You should adjust this
        target_co.co_freevars,
        target_co.co_cellvars
    )
    # print_co_info(final_co)
    return recursively_update_target_fn(co, fn_name, final_co)


def add_dummy_at_offset(co, offset, fn_name):
    print ("Offset:{} fn_name:{}".format(offset, fn_name))
    target_co = get_co_fn(co, fn_name)
    print(type(target_co), type(co))
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return
    dummy_inst = create_dummy_inst(len(target_co.co_names))
    # print(dummy_inst)
    # print(target_co.co_names)
    # print('-----------------')
    # print(type(target_co), type(target_co.co_code))
    for inst in dis.get_instructions(target_co):
        #print (inst.opname)
        if inst.opcode in opcode.hasjabs or inst.opcode in opcode.hasjrel:
            pass
            # print(inst.opcode, inst.opname, inst.arg, inst)
        # if inst.opname == 'POP_JUMP_IF_FALSE' or inst.opname == 'JUMP_ABSOLUTE': # or inst.opname == 'JUMP_FORWARD':
        #     print (inst)
        #     cur = inst.offset
        #     print ('offset:', cur+2+1)
            #print (target_co.co_code[cur-1:cur+2])
            #print (target_co.co_code[cur:cur+2])
            #target_co.co_code[offset:offset+2] = target_co.co_code[offset:offset+2]+4;
            #print (target_co.co_code[offset:offset+2])
    # for off_set, op, arg in dis._unpack_opargs(target_co):

            
    print('-----------------')
    '''
    code = target_co.co_code[:offset] + dummy_inst + target_co.co_code[offset:]
    
    #print('before:', code[7])
    code = update_codebyte( code, 7, (4) )
    code = update_codebyte( code, 11, (4) )
    code = update_codebyte( code, 21, (4) )
    #code = update_codebyte( code, 31, (4) )
    #print('after:',code[7])
    '''
    # dummy_inst =  bytes([opcode.opmap['ROT_THREE']])+bytes([0]) + bytes([opcode.opmap['ROT_THREE']])+bytes([0])+ bytes([opcode.opmap['ROT_THREE']])+bytes([0])
    # dummy_inst = bytes([opcode.opmap['JUMP_FORWARD']])+bytes([0])
    dummy_inst = bytes([120])+bytes([16])
    code = update_jump_offsets(target_co.co_code, dummy_inst, 0)
    print('addded dummy:', dummy_inst)
    dis.dis(dummy_inst)
    dis.dis(code)
    dummy_inst = bytes([87])+bytes([0])
    code = update_jump_offsets(code, dummy_inst, 16)
    dis.dis(dummy_inst)
    dis.dis(code)
    dis.dis(code)
    print("LOL")
    print(len(code))
    print_co_info(target_co)
    if sys.version_info[1] > 7:
        final_co =  types.CodeType(
            target_co.co_argcount,
            target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals,
            target_co.co_stacksize,
            target_co.co_flags,
            code,
            target_co.co_consts,
            tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_varnames))]),
            target_co.co_varnames,
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        )
    else:
        final_co =  types.CodeType(
            target_co.co_argcount,
            # target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals,
            target_co.co_stacksize,
            target_co.co_flags,
            code,
            target_co.co_consts,
            tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_varnames))]),
            target_co.co_varnames,
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        )
    print_co_info(final_co)
    print("Final CO coomplete!")
    return recursively_update_target_fn(co, fn_name, final_co)

## All code below for MWE 0 10 16 17
def match_pattern_boolean(co):
    target_co = co
    print([opcode.opname[op] for off_set, op, arg in dis._unpack_opargs(target_co.co_code)])
    target_offsets = [off_set for off_set, op, arg in dis._unpack_opargs(target_co.co_code) if op in jmp_op_boolean_chain]
    if len(target_offsets) < 2: return []
    all_sets = []
    for x in target_offsets:
        if x in sum(all_sets, []): continue # ignore offsets already added
        temp = []
        for off_set in range(x, len(target_co.co_code), 2):
            op = target_co.co_code[off_set]
            if op in terminate_boolean_chain:
                print("break", op, off_set)
                break
            if op in jmp_op_boolean_chain: 
                temp.append(off_set)
        print(temp)
        # if len(temp) > 1: all_sets.append(temp)
        all_sets = all_sets + [temp] if len(temp) > 1 else all_sets
    return all_sets

def update_jump_boolean(co, chain):
    dis.dis(co)
    original_code = co.co_code
    code = original_code
    print("Chain:", chain)
    op, arg = get_op_arg_offset(code, chain[0])
    last_op, last_arg = get_op_arg_offset(code, chain[-1])
    final = []
    print("op", op)
    print("op, arg:",[get_op_arg_offset(code, x) for x in chain])
    # chain_op = [ get_op_arg_offset(code, x)[0] for x in chain]
    # CONDITONAL:
    if op in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']] and code[get_prev_offset_skipping_extended(code, arg)] in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']]:
        print("Applying conditional pattern: C1")
        # Instrument before the next one
        # This is a conditional
        cond_chain_offsets = []
        # Iterate all up until target jump instruction
        for i in range(chain[0], chain[-1] + 2, 2):
            curr_op, curr_arg = get_op_arg_offset(code, i)
            if curr_op in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']] and curr_arg == arg:
                cond_chain_offsets.append(i)
            if curr_op in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']] and curr_arg > arg:
                cond_chain_offsets.append(i)
                break
            
        if len(cond_chain_offsets) > 2:
            print(chain, cond_chain_offsets, "<===")
            target_instrument = get_prev_offset_skipping_extended(code,cond_chain_offsets[-1]) + 2
            # Add STORE_FAST (125) and LOAD_FAST (124)
            instructions = bytes([opcode.opmap['STORE_FAST']])+ bytes([0]) + bytes([opcode.opmap['LOAD_FAST']]) + bytes([0])
            # Update args
            
            # Convert to JUMP_IF_TRUE_OR_POP
            # print(type(code), type(bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']])))  
            # code = code[:chain[0]] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[chain[0]+1:]
            print("C1: Updating chain")
            for i in range(len(cond_chain_offsets) - 1):
                updated_jmp_target_diff = target_instrument - arg
                prev_len = len(code)
                # Convert pops to direct jump instructions
                # POP_JUMP_IF_TRUE -> JUMP_IF_TRUE_OR_POP
                # POP_JUMP_IF_FALSE -> JUMP_IF_FALSE_OR_POP
                if code[cond_chain_offsets[i]] == opcode.opmap['POP_JUMP_IF_FALSE']:
                    code = code[:cond_chain_offsets[i]] + bytes([opcode.opmap['JUMP_IF_FALSE_OR_POP']]) + code[cond_chain_offsets[i]+1:]
                elif code[cond_chain_offsets[i]] == opcode.opmap['POP_JUMP_IF_TRUE']:
                    code = code[:cond_chain_offsets[i]] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[cond_chain_offsets[i]+1:]
                code = update_codebyte(code, cond_chain_offsets[i] +1 ,updated_jmp_target_diff) # this will now point to new spot
                # Update w.r.t len
                if len(code) != prev_len:
                    raise("Len of code changed, please update")
            # Add instructions
            if len(co.co_varnames) >= 256:
                raise("Extend args in instrumented code")
            print("C1:Inserting instruction")
            instructions = update_codebyte(instructions, 1, len(co.co_varnames))
            instructions = update_codebyte(instructions, 3, len(co.co_varnames))
            code = update_jump_offsets(code, instructions, target_instrument)
            print("C1:Finaindg other instructions")
            # Find other jump instructions in the middle
            for i in range(cond_chain_offsets[0],cond_chain_offsets[-1] + 2, 2):
                curr_op, curr_arg = get_op_arg_offset(code, i)
                if curr_op == 115: # POP_JUMP_IF_TRUE
                    # REPLACE WITH JUMP_IF_TRUE_OR_POP if arg>= instrumented code offset
                    if curr_arg >= target_instrument:
                        code = code[:i] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[i+1:]
                        prev_len = len(code)
                        updated_jmp_target_diff = target_instrument - curr_arg
                        code = update_codebyte(code, i +1 ,updated_jmp_target_diff) # this will now point to new spot
                        if len(code) != prev_len:
                            raise("Len of code changed, please update")     
            print("C1:Done with pattern 1")
            if sys.version_info[1] > 7:
                final.append( types.CodeType(
                    co.co_argcount,
                    co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))
            else:
                final.append( types.CodeType(
                    co.co_argcount,
                    # co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))
    # (a or b) and c
    code = original_code
    op, arg = get_op_arg_offset(code, chain[0])
    last_op, last_arg = get_op_arg_offset(code, chain[-1])
    
    if op == 115: # POP_JUMP_IF_TRUE
        print("Applying break boolean pattern: C2")
        # Completes an OR operation and goes to complete other AND operand:
        # Assign this value to local variable
        # Convert to JUMP_IF_TRUE_OR_POP  
        jump_target = arg
        if code[get_prev_offset_skipping_extended(code, arg)] in [opcode.opmap['JUMP_IF_FALSE_OR_POP'], opcode.opmap['JUMP_IF_TRUE_OR_POP']]:
            # Assign the loaded value for this jump op to a variable
            target_instrument = get_prev_offset_skipping_extended(code, get_prev_offset_skipping_extended(code, arg)) + 2
            # Add STORE_FAST (125) and LOAD_FAST (124)
            instructions = bytes([opcode.opmap['STORE_FAST']])+ bytes([0]) + bytes([opcode.opmap['LOAD_FAST']]) + bytes([0])
            # Update args

            # Convert to JUMP_IF_TRUE_OR_POP
            print(type(code), type(bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']])))  
            code = code[:chain[0]] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[chain[0]+1:]
            updated_jmp_target_diff = target_instrument -jump_target
            prev_len = len(code)
            code = update_codebyte(code, chain[0] +1 ,updated_jmp_target_diff) # this will now point to new spot
            # Update w.r.t len
            if len(code) != prev_len:
                raise("Len of code changed, please update")
            # Add instructions
            if len(co.co_varnames) >= 256:
                raise("Extend args in instrumented code")
            instructions = update_codebyte(instructions, 1, len(co.co_varnames))
            instructions = update_codebyte(instructions, 3, len(co.co_varnames))
            code = update_jump_offsets(code, instructions, target_instrument)
            print("C2: Done")
            if sys.version_info[1] > 7:
                final.append( types.CodeType(
                    co.co_argcount,
                    co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))
            else:
                final.append( types.CodeType(
                    co.co_argcount,
                    # co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))

        
        pass
    # a and b and c 
    code = original_code
    op, arg = get_op_arg_offset(code, chain[0])
    last_op, last_arg = get_op_arg_offset(code, chain[-1])
    
    if op == 111: # JUMP_IF_FALSE_OR_POP
        print("Applying chained ANDs pattern: C3")
        pass
        and_offsets = []
        for i in range(chain[0], len(code), 2):
            curr_op, curr_arg = get_op_arg_offset(code, i)
            if curr_op == op and curr_arg == arg:
                and_offsets.append(i)
        print("offsets:", and_offsets)
        if len(and_offsets) > 2:
            target_instrument = get_prev_offset_skipping_extended(code,and_offsets[2]) + 2
            # Add STORE_FAST (125) and LOAD_FAST (124)
            instructions = bytes([opcode.opmap['STORE_FAST']])+ bytes([0]) + bytes([opcode.opmap['LOAD_FAST']]) + bytes([0])
            # Update args
            
            # Convert to JUMP_IF_TRUE_OR_POP
            # print(type(code), type(bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']])))  
            # code = code[:chain[0]] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[chain[0]+1:]
            for i in range(2):
                updated_jmp_target_diff = target_instrument - arg
                prev_len = len(code)
                code = update_codebyte(code, and_offsets[i] +1 ,updated_jmp_target_diff) # this will now point to new spot
                # Update w.r.t len
                if len(code) != prev_len:
                    raise("Len of code changed, please update")
            # Add instructions
            if len(co.co_varnames) >= 256:
                raise("Extend args in instrumented code")
            instructions = update_codebyte(instructions, 1, len(co.co_varnames))
            instructions = update_codebyte(instructions, 3, len(co.co_varnames))
            code = update_jump_offsets(code, instructions, target_instrument)
            # Find other jump instructions in the middle
            for i in range(and_offsets[0],and_offsets[2], 2):
                curr_op, curr_arg = get_op_arg_offset(code, i)
                if curr_op == 115: # POP_JUMP_IF_TRUE
                    # REPLACE WITH JUMP_IF_TRUE_OR_POP if arg>= instrumented code offset
                    if curr_arg >= target_instrument:
                        code = code[:i] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[i+1:]
                        prev_len = len(code)
                        updated_jmp_target_diff = target_instrument - curr_arg
                        print("->>>>>>>>>>>>LOL>>>",curr_arg, target_instrument)
                        code = update_codebyte(code, i +1 ,updated_jmp_target_diff) # this will now point to new spot
                        if len(code) != prev_len:
                            raise("Len of code changed, please update")     
            print("C3: Done")
            if sys.version_info[1] > 7:
                final.append( types.CodeType(
                    co.co_argcount,
                    co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))
            else:
                final.append( types.CodeType(
                    co.co_argcount,
                    # co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))
        # Iterate the chain so that we have all ANDs together
        # If it is a subset of the actual boolean chain, doesn't matter
        # and assign it to a variable
    code = original_code
    op, arg = get_op_arg_offset(code, chain[0])
    last_op, last_arg = get_op_arg_offset(code, chain[-1])
    print("C4:op, arg:",[get_op_arg_offset(code, x) for x in chain])
    if last_op == opcode.opmap['POP_JUMP_IF_FALSE'] or last_op == opcode.opmap['POP_JUMP_IF_TRUE']:
        print("Applying conditional pattern: C4")
        # Instrument instruction
        cond_chain_offsets = []
        # Iterate all up until target jump instruction
        for i in range(chain[0], chain[-1] + 2, 2):
            curr_op, curr_arg = get_op_arg_offset(code, i)
            if curr_op in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']] and curr_arg > chain[-1]:
                cond_chain_offsets.append(i)
            if i == chain[-1]:
                break
        
        if len(cond_chain_offsets) > 1:
            print(chain, cond_chain_offsets, "<===")
            target_instrument = get_prev_offset_skipping_extended(code,cond_chain_offsets[-1]) + 2
            # Add STORE_FAST (125) and LOAD_FAST (124)
            instructions = bytes([opcode.opmap['STORE_FAST']])+ bytes([0]) + bytes([opcode.opmap['LOAD_FAST']]) + bytes([0])
            # Update args
            
            # Convert to JUMP_IF_TRUE_OR_POP
            print("C4: Convert jumps in the chain")
            # print(type(code), type(bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']])))  
            # code = code[:chain[0]] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[chain[0]+1:]
            for i in range(len(cond_chain_offsets) - 1):
                curr_op, curr_arg = get_op_arg_offset(code, cond_chain_offsets[i])
                updated_jmp_target_diff = target_instrument - curr_arg
                prev_len = len(code)
                # Convert pops to direct jump instructions
                # POP_JUMP_IF_TRUE -> JUMP_IF_TRUE_OR_POP
                # POP_JUMP_IF_FALSE -> JUMP_IF_FALSE_OR_POP
                if code[cond_chain_offsets[i]] == opcode.opmap['POP_JUMP_IF_FALSE']:
                    code = code[:cond_chain_offsets[i]] + bytes([opcode.opmap['JUMP_IF_FALSE_OR_POP']]) + code[cond_chain_offsets[i]+1:]
                elif code[cond_chain_offsets[i]] == opcode.opmap['POP_JUMP_IF_TRUE']:
                    # TODO Add unary NOT for this one. See sample 46 - user_exception
                    code = code[:cond_chain_offsets[i]] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[cond_chain_offsets[i]+1:]
                print("->>>>>>>>>>>>LOL>>>",curr_arg, target_instrument)
                code = update_codebyte(code, cond_chain_offsets[i] +1 ,updated_jmp_target_diff) # this will now point to new spot
                print(get_op_arg_offset(code, cond_chain_offsets[i]))
                # Update w.r.t len
                if len(code) != prev_len:
                    raise("Len of code changed, please update")
            # Add instructions
            if len(co.co_varnames) >= 256:
                raise("Extend args in instrumented code")
            print("C4: Instrumenting code")
            if last_op == opcode.opmap['POP_JUMP_IF_TRUE']:
                code  = code[:cond_chain_offsets[-1]] + bytes([opcode.opmap['POP_JUMP_IF_FALSE']]) + code[cond_chain_offsets[-1]+1:]
                for i in range(len(chain) - 2):
                    if code[chain[i]] == opcode.opmap['JUMP_IF_FALSE_OR_POP']:
                        code = code[:chain[i]] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[chain[i]+1:]
                    elif code[chain[i]] == opcode.opmap['POP_JUMP_IF_TRUE']:
                        # TODO Add unary NOT for this one. See sample 46 - user_exception
                        code = code[:chain[i]] + bytes([opcode.opmap['POP_JUMP_IF_FALSE']]) + code[chain[i]+1:]
                    
            instructions = update_codebyte(instructions, 1, len(co.co_varnames))
            instructions = update_codebyte(instructions, 3, len(co.co_varnames))
            code = update_jump_offsets(code, instructions, target_instrument)
            # Find other jump instructions in the middle
            # for i in range(cond_chain_offsets[0],cond_chain_offsets[2], 2):
            #     curr_op, curr_arg = get_op_arg_offset(code, i)
            #     if curr_op == 115: # POP_JUMP_IF_TRUE
            #         # REPLACE WITH JUMP_IF_TRUE_OR_POP if arg>= instrumented code offset
            #         if curr_arg >= target_instrument:
            #             code = code[:i] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + code[i+1:]
            #             prev_len = len(code)
            #             updated_jmp_target_diff = target_instrument - curr_arg
            #             code = update_codebyte(code, i +1 ,updated_jmp_target_diff) # this will now point to new spot
            #             if len(code) != prev_len:
            #                 raise("Len of code changed, please update")     
            print("C4: Done and returning")
            if sys.version_info[1] > 7:
                final.append( types.CodeType(
                    co.co_argcount,
                    co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))
            else:
                final.append( types.CodeType(
                    co.co_argcount,
                    # co.co_posonlyargcount, #Add this in Python 3.8+
                    co.co_kwonlyargcount,  #Add this in Python3
                    co.co_nlocals + 1,
                    co.co_stacksize,
                    co.co_flags,
                    code,
                    co.co_consts,
                    co.co_names,
                    tuple(list(co.co_varnames) + [get_local_var_name(list(co.co_varnames))]),
                    co.co_filename,
                    co.co_name,
                    co.co_firstlineno,
                    co.co_lnotab,   # In general, You should adjust this
                    co.co_freevars,
                    co.co_cellvars
                ))
    return final
def break_boolean_chains(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    all_sets = match_pattern_boolean(target_co)
    print("all sets:", all_sets)
    final = []
    for x in all_sets:
        try:
            temp = update_jump_boolean(target_co, x)
            print("CO!!:", temp)
            final = final + [recursively_update_target_fn(co, fn_name, x) for x in temp if x is not None]
            # final.append(recursively_update_target_fn(co, fn_name, temp))
        except Exception as a:
            print(a)
            traceback.print_exc()
            continue
    print("<>>>>>>",final)
    return final
## End of all code for MWE 0 10 16 17

## For Jump forward conversion MWE 19
def convert_jump_forward(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    code = target_co.co_code
    jmp_fwd_offsets = [i for i in range(0, len(code), 2) if get_op_arg_offset(code, i)[0] == opcode.opmap['JUMP_FORWARD']]
    # print(opcode.opmap['JUMP_FORWARD'], code[48])
    
    # print("jmp_fwd_offsets", jmp_fwd_offsets)
    # For each jump forward, find the "POP_JUMP_IF_FALSE" before and assign it to local variable
    # Get the condition end that needs to be copied to get opposite condition
    jump_tuples = []
    for i in jmp_fwd_offsets:
        tmp = None
        for offset in range(0, len(code), 2):
            if offset >= i: break
            curr_op, curr_arg = get_op_arg_offset(code, offset)
            if (curr_op == opcode.opmap['POP_JUMP_IF_FALSE']
                and curr_arg > i
            ):
                tmp = (i, offset)
        jump_tuples.append(tmp)
    final_co = []
    for jmp_fwd, pjif in jump_tuples:
        curr_code = code
        # Instrument a variable
        target_instrument = get_prev_offset_skipping_extended(curr_code, pjif) + 2
        # Add STORE_FAST (125) and LOAD_FAST (124)
        instructions = bytes([opcode.opmap['STORE_FAST']])+ bytes([0]) + bytes([opcode.opmap['LOAD_FAST']]) + bytes([0])
        instructions = update_codebyte(instructions, 1, len(target_co.co_varnames))
        instructions = update_codebyte(instructions, 3, len(target_co.co_varnames))
        # Instrument in
        curr_code = update_jump_offsets(curr_code, instructions, target_instrument)
        if curr_code[jmp_fwd + len(instructions)] != opcode.opmap['JUMP_FORWARD']:
            raise("Len of code changed. Cater to entended args")
        # Instrument the condition immediately after
        _ , curr_arg = get_op_arg_offset(curr_code, jmp_fwd + len(instructions))
        # below is the offset of the point where JUMP_FORWARD jumps to
        jump_target = curr_arg + jmp_fwd + len(instructions) + 2
        # Instructions to instrument now
        instructions_2 = bytes([opcode.opmap['LOAD_FAST']]) + bytes([0]) + bytes([opcode.opmap['POP_JUMP_IF_TRUE']]) + bytes([0])
        if len(target_co.co_varnames) >= 256 or jump_target + 4 >= 256:
            raise("Extend args in instrumented code")
        instructions_2 = update_codebyte(instructions_2, 1, len(target_co.co_varnames)) # load the temp variable
        instructions_2 = update_codebyte(instructions_2, 3, jump_target + 4)
        curr_code = update_jump_offsets(curr_code, instructions_2, jmp_fwd + len(instructions) + 2)
        if sys.version_info[1] > 7:
            curr_co = types.CodeType(
                target_co.co_argcount,
                target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                curr_code,
                target_co.co_consts,
                target_co.co_names,
                tuple(list(target_co.co_varnames) + [get_local_var_name(list(target_co.co_varnames))]),
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            )
        else:
            curr_co = types.CodeType(
                target_co.co_argcount,
                # target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                curr_code,
                target_co.co_consts,
                target_co.co_names,
                tuple(list(target_co.co_varnames) + [get_local_var_name(list(target_co.co_varnames))]),
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            )
        final_co.append(curr_co)

    final = []
    for x in final_co:
        try:
            print("CO:", x)
            final.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final    
    # return []

## END Jump forward conversion MWE 19

## For boolean extraction in while loop MWE 158
def convert_loopBoolean(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    code = target_co.co_code
    setup_loop_offsets = [i for i in range(0, len(code), 2) if get_op_arg_offset(code, i)[0] == opcode.opmap['SETUP_LOOP']]
    print(setup_loop_offsets)
    # print(opcode.opmap['JUMP_FORWARD'], code[48])
    
    # For each setup loop, find the "corresponding POP_BLOCK" 
    # STUP_LOOP - POP_BLOCK is the entire loop
    # Get the condition end that needs to be copied to get opposite condition
    loop_tuples = []
    # dis.dis(code)
    for i in setup_loop_offsets:
        offset_POP_BLOCK = None
        setup_l_count = 1
        print(list(range(i + 2, len(code), 2)))
        for os_temp in range(i + 2, len(code), 2):
            if code[os_temp] == opcode.opmap['SETUP_LOOP']:
                print("SETUP_LOOP!!", os_temp)
                setup_l_count = setup_l_count + 1
            elif code[os_temp] == opcode.opmap['POP_BLOCK'] and code[os_temp - 2] == opcode.opmap['JUMP_ABSOLUTE']:
                print('POP_BLOCK!!', os_temp)
                if setup_l_count == 1:
                    offset_POP_BLOCK = os_temp
                    break
                else:
                    setup_l_count = setup_l_count - 1
        if offset_POP_BLOCK: loop_tuples.append((i, offset_POP_BLOCK))
    print("LOOP tuple:",loop_tuples)
    final_co = []
    for start, end in loop_tuples:
        try:
            curr_code = code
            # Get POP_JUMP_IF_FALSE that jumps out of loop
            offset_bool_end = None
            for os_temp in range(start, end, 2):
                op, arg = get_op_arg_offset(curr_code, os_temp)
                if op in [opcode.opmap['POP_JUMP_IF_FALSE'],opcode.opmap['POP_JUMP_IF_TRUE']]:
                    if arg >= end:
                        offset_bool_end = os_temp
                if op in [opcode.opmap['STORE_FAST'],opcode.opmap['RETURN_VALUE'],opcode.opmap['YIELD_VALUE'],opcode.opmap['FOR_ITER'],opcode.opmap['STORE_GLOBAL']]:
                    break
            if offset_bool_end == None: continue
            # We have boolean end at offset `offset_bool_end`
            # We instrument our store variable here
            # Then move out SETUP_LOOP and LOAD_FAST
            # Pattern: STORE_FAST SETUP_LOOP LOAD_FAST
            boolean_expression = curr_code[start + 2:get_prev_offset_skipping_extended(curr_code, offset_bool_end)+ 2] # We will copy this at the end
            for off_set, op, arg in dis._unpack_opargs(boolean_expression):
                if op in [opcode.opmap['POP_JUMP_IF_FALSE'], opcode.opmap['POP_JUMP_IF_TRUE']]:
                    if boolean_expression[off_set] == opcode.opmap['POP_JUMP_IF_FALSE']:
                        boolean_expression = boolean_expression[:off_set] + bytes([opcode.opmap['JUMP_IF_FALSE_OR_POP']]) + boolean_expression[off_set+1:]
                    elif boolean_expression[off_set] == opcode.opmap['POP_JUMP_IF_TRUE']:
                        boolean_expression = boolean_expression[:off_set] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + boolean_expression[off_set+1:]
                    if arg > offset_bool_end:
                        boolean_expression = update_codebyte(boolean_expression, off_set + 1, len(boolean_expression) - arg)
                elif op in opcode.hasjabs:
                    # Check only argument and update it
                    boolean_expression = update_codebyte(boolean_expression, off_set + 1, -(start + 2))
            boolean_expression = boolean_expression + update_codebyte(bytes([opcode.opmap['STORE_FAST']]) + bytes([0]), 1, len(target_co.co_varnames))
            # dis.dis(boolean_expression)
            # Start instrumenting
            
            instr = bytes([opcode.opmap['STORE_FAST']])+ bytes([0]) + bytes([opcode.opmap['SETUP_LOOP']]) + bytes([0]) + bytes([opcode.opmap['LOAD_FAST']]) + bytes([0])
            instr = update_codebyte(instr, 1, len(target_co.co_varnames))
            print(end - (get_prev_offset_skipping_extended(curr_code,offset_bool_end) + 4  - len(instr)), "<----")
            instr = update_codebyte(instr, 3, end - (get_prev_offset_skipping_extended(curr_code,offset_bool_end) + 4  - len(instr)))
            instr = update_codebyte(instr, 5, len(target_co.co_varnames))
            
            curr_code = update_jump_offsets(curr_code, instr, get_prev_offset_skipping_extended(curr_code,offset_bool_end) + 2)
            for os_temp in range(start, offset_bool_end, 2):
                if get_op_arg_offset(curr_code, os_temp)[0] not in [opcode.opmap['POP_JUMP_IF_FALSE'], opcode.opmap['POP_JUMP_IF_TRUE']]: continue
                updated_jmp_target_diff = get_prev_offset_skipping_extended(curr_code,offset_bool_end) + 2 - get_op_arg_offset(curr_code, os_temp)[1]
                print('diff', updated_jmp_target_diff, get_op_arg_offset(curr_code, os_temp)[1])
                prev_len = len(curr_code)
                # Convert pops to direct jump instructions
                # POP_JUMP_IF_TRUE -> JUMP_IF_TRUE_OR_POP
                # POP_JUMP_IF_FALSE -> JUMP_IF_FALSE_OR_POP
                if curr_code[os_temp] == opcode.opmap['POP_JUMP_IF_FALSE']:
                    curr_code = curr_code[:os_temp] + bytes([opcode.opmap['JUMP_IF_FALSE_OR_POP']]) + curr_code[os_temp+1:]
                elif curr_code[os_temp] == opcode.opmap['POP_JUMP_IF_TRUE']:
                    curr_code = curr_code[:os_temp] + bytes([opcode.opmap['JUMP_IF_TRUE_OR_POP']]) + curr_code[os_temp+1:]
                if get_op_arg_offset(curr_code, os_temp)[1] < offset_bool_end: continue
                curr_code = update_codebyte(curr_code, os_temp +1 ,updated_jmp_target_diff) # this will now point to new spot
                # Update w.r.t len
                
                if len(curr_code) != prev_len:
                    raise("Len of code changed, please update")    
            # dis.dis(curr_code)
            # now instrument the boolean expression by the end of it

            # Removed setup loop
            curr_code = update_jump_offsets_remove(curr_code, start)
            # curr_code = update_codebyte(curr_code, os_temp +1 ,updated_jmp_target_diff)
            jmp_abs = get_prev_offset_skipping_extended(curr_code,end + 2) + 2
            print(jmp_abs, offset_bool_end)
            curr_code = update_codebyte(curr_code, jmp_abs + 1, offset_bool_end - 2 - get_op_arg_offset(curr_code, jmp_abs)[1])
            
            # redirect it to the new setuploop

            # dis.dis(curr_code)
            for off_set, op, arg in dis._unpack_opargs(boolean_expression):
                if op in opcode.hasjabs:
                    # Check only argument and update it
                    boolean_expression = update_codebyte(boolean_expression, off_set + 1, get_prev_offset_skipping_extended(curr_code,end + 2) + 2)
            curr_code = update_jump_offsets(curr_code, boolean_expression, get_prev_offset_skipping_extended(curr_code,end + 2) + 2)
            # dis.dis(curr_code)
            print(end)
            if sys.version_info[1] > 7:
                curr_co = types.CodeType(
                    target_co.co_argcount,
                    target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    curr_code,
                    target_co.co_consts,
                    target_co.co_names,
                    tuple(list(target_co.co_varnames) + [get_local_var_name(list(target_co.co_varnames))]),
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                )
            else:
                curr_co = types.CodeType(
                    target_co.co_argcount,
                    # target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    curr_code,
                    target_co.co_consts,
                    target_co.co_names,
                    tuple(list(target_co.co_varnames) + [get_local_var_name(list(target_co.co_varnames))]),
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                )
            print("ADDED for", start,end)
            final_co.append(curr_co)
        except:
            continue
    final = []
    for x in final_co:
        try:
            print("CO:", x)
            final.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final   

## END For boolean extraction in while loop MWE 158

## Remove deadcode for malicious pyc
def remove_dead_code(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    code = target_co.co_code
    final_code = code
    end_offset = -1
    final_list = []
    for off_set, op, arg in dis._unpack_opargs(code):
        if op in [opcode.opmap['RETURN_VALUE']] and (end_offset == -1 or end_offset <= off_set):
            final_code = code[:off_set+2]
            final_code2 = code
            
            for i in range(0, len(final_code), 2):
                final_code2 = update_jump_offsets_remove(final_code2,0)
            final_code2 += final_code
            if len(final_code) == len(code): continue
            if sys.version_info[1] > 7:
                final_list = final_list + [recursively_update_target_fn(co, fn_name, types.CodeType(
                    target_co.co_argcount,
                    target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    final_code,
                    target_co.co_consts,
                    target_co.co_names,
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))]
            else:
                final_list = final_list + [recursively_update_target_fn(co, fn_name, types.CodeType(
                    target_co.co_argcount,
                    # target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    final_code,
                    target_co.co_consts,
                    target_co.co_names,
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))]
            if sys.version_info[1] > 7:
                final_list = final_list + [recursively_update_target_fn(co, fn_name, types.CodeType(
                    target_co.co_argcount,
                    target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    final_code2,
                    target_co.co_consts,
                    target_co.co_names,
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))]
            else:
                final_list = final_list + [recursively_update_target_fn(co, fn_name, types.CodeType(
                    target_co.co_argcount,
                    # target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    final_code2,
                    target_co.co_consts,
                    target_co.co_names,
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))]
            break
        elif op in opcode.hasjabs:
            if arg > end_offset: end_offset = arg
        elif op in opcode.hasjrel:
            # Target here is off_set + 2 + arg
            # So if the new instruction is in this region:
            # off_set + 2 [  CHECK THIS AREA  ]  off_set + 2 + arg
            if off_set + 2 + arg > end_offset: end_offset = off_set + 2 + arg
            if arg == 0 and op == opcode.opmap['JUMP_FORWARD']:
                # remove instruction
                if code[off_set-2] == opcode.opmap['EXTENDED_ARG']:
                    raise("Can't remove because of Extended Arg the JUMP_FORWARD instruction")
                final_code = update_jump_offsets_remove(code, off_set)
                if sys.version_info[1] > 7:
                    final_list = final_list + [recursively_update_target_fn(co, fn_name, types.CodeType(
                        target_co.co_argcount,
                        target_co.co_posonlyargcount, #Add this in Python 3.8+
                        target_co.co_kwonlyargcount,  #Add this in Python3
                        target_co.co_nlocals,
                        target_co.co_stacksize,
                        target_co.co_flags,
                        final_code,
                        target_co.co_consts,
                        target_co.co_names,
                        target_co.co_varnames,
                        target_co.co_filename,
                        target_co.co_name,
                        target_co.co_firstlineno,
                        target_co.co_lnotab,   # In general, You should adjust this
                        target_co.co_freevars,
                        target_co.co_cellvars
                    ))]
                else:
                    final_list = final_list + [recursively_update_target_fn(co, fn_name, types.CodeType(
                        target_co.co_argcount,
                        # target_co.co_posonlyargcount, #Add this in Python 3.8+
                        target_co.co_kwonlyargcount,  #Add this in Python3
                        target_co.co_nlocals,
                        target_co.co_stacksize,
                        target_co.co_flags,
                        final_code,
                        target_co.co_consts,
                        target_co.co_names,
                        target_co.co_varnames,
                        target_co.co_filename,
                        target_co.co_name,
                        target_co.co_firstlineno,
                        target_co.co_lnotab,   # In general, You should adjust this
                        target_co.co_freevars,
                        target_co.co_cellvars
                    ))]
    
    return final_list
# END Remove deadcode for malicious pyc
    
## Instrument code after break
def instrument_after_break(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    for offset_1 in range(0, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp not in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']]: continue
        # Find BREAK_LOOP
        for offset_2 in range(offset_1 + 2, len(code), 2):
            curr_op_brk, curr_arg_brk = get_op_arg_offset(code, offset_2)
            # If another jump then give up
            if curr_op_brk in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']]: break
            # Ignore until BREAK_LOOP
            if curr_op_brk not in [opcode.opmap['BREAK_LOOP']]: continue
            # Find jump absolute
            for offset_3 in range(offset_2 + 2, len(code), 2):
                curr_op_abs, curr_arg_abs = get_op_arg_offset(code, offset_3)
                if curr_op_abs in [opcode.EXTENDED_ARG]: continue
                if curr_op_abs != opcode.opmap['JUMP_ABSOLUTE']: break
                print("PATTERN FOUND!!")
                # Instrument here 
                dummy_inst = create_dummy_inst(len(target_co.co_names))
                # Instrument after Break loop
                print("Dummy created and now instrumenting")
                temp_code = update_jump_offsets(code, dummy_inst, offset_2 + 2)
                if len(temp_code) != (len(code) + len(dummy_inst)):
                    print("Len of code changed, please update {} {}".format(len(temp_code), (len(code) + len(dummy_inst))))    
                    # raise("Len of code changed, please update ")
                # point the jump instruction this instrumented code
                start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
                print("Update the jump instruction now", "found start{} and end{}".format(start_instru, end_instru))
                increment_value = start_instru - curr_arg_jmp
                print("Update to", start_instru, " from ", curr_arg_jmp)
                temp_code = update_codebyte(temp_code, offset_1 + 1, increment_value)
                if sys.version_info[1] > 7:
                    final.append(types.CodeType(
                        target_co.co_argcount,
                        target_co.co_posonlyargcount, #Add this in Python 3.8+
                        target_co.co_kwonlyargcount,  #Add this in Python3
                        target_co.co_nlocals + 1,
                        target_co.co_stacksize,
                        target_co.co_flags,
                        temp_code,
                        target_co.co_consts,
                        tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_varnames))]),
                        target_co.co_varnames,
                        target_co.co_filename,
                        target_co.co_name,
                        target_co.co_firstlineno,
                        target_co.co_lnotab,   # In general, You should adjust this
                        target_co.co_freevars,
                        target_co.co_cellvars
                    ))
                else:
                    final.append(types.CodeType(
                        target_co.co_argcount,
                        # target_co.co_posonlyargcount, #Add this in Python 3.8+
                        target_co.co_kwonlyargcount,  #Add this in Python3
                        target_co.co_nlocals + 1,
                        target_co.co_stacksize,
                        target_co.co_flags,
                        temp_code,
                        target_co.co_consts,
                        tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_varnames))]),
                        target_co.co_varnames,
                        target_co.co_filename,
                        target_co.co_name,
                        target_co.co_firstlineno,
                        target_co.co_lnotab,   # In general, You should adjust this
                        target_co.co_freevars,
                        target_co.co_cellvars
                    ))
            break
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co   

    
## END Instrument code after break

## Instrument code after continue
def instrument_after_continue(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    for offset_1 in range(0, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp not in [opcode.opmap['POP_JUMP_IF_TRUE'], opcode.opmap['POP_JUMP_IF_FALSE']]: continue
        # Find JUMP_FORWARD and POP_TOP
        for offset_2 in range(offset_1 + 2, len(code), 2):
            curr_op_brk, curr_arg_brk = get_op_arg_offset(code, offset_2)
            # If another jump then give up
            if curr_op_brk in [opcode.EXTENDED_ARG]: continue
            # IF JUMP_ABSOLUTE followed by POP_TOP only
            if curr_op_brk not in [opcode.opmap['JUMP_ABSOLUTE']] or get_op_arg_offset(code, offset_2 + 2)[0] not in  [opcode.opmap['POP_TOP']]: break
            # Find jump absolute
            for offset_3 in range(offset_2 + 4, len(code), 2):
                curr_op_abs, curr_arg_abs = get_op_arg_offset(code, offset_3)
                if curr_op_abs in [opcode.EXTENDED_ARG]: continue
                if curr_op_abs != opcode.opmap['JUMP_ABSOLUTE']: break
                if curr_arg_abs != curr_arg_brk: break
                print("PATTERN FOUND!!")
                # Change JUMP_ABSOLUTE to JUMP_FORWARD
                temp_code_1 = code[:offset_2] + bytes([opcode.opmap['JUMP_FORWARD']]) + code[offset_2+1:]
                # Instrument here 
                dummy_inst = create_dummy_inst(len(target_co.co_names))
                # Instrument after POP_TOP
                print("Dummy created and now instrumenting")
                temp_code = update_jump_offsets(temp_code_1, dummy_inst, offset_2 + 4)
                if len(temp_code) != (len(temp_code_1) + len(dummy_inst)):
                    print("Len of code changed, please update {} {}".format(len(temp_code), (len(temp_code_1) + len(dummy_inst))))    
                    # raise("Len of code changed, please update ")
                # point the jump instruction this instrumented code
                start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
                increment_value = 2 - get_op_arg_offset(temp_code, start_instru -4)[1]
                print("Update the jump instruction now", increment_value, start_instru -3)
                temp_code = update_codebyte(temp_code, start_instru - 3, increment_value)
                if sys.version_info[1] > 7:
                    final.append(types.CodeType(
                        target_co.co_argcount,
                        target_co.co_posonlyargcount, #Add this in Python 3.8+
                        target_co.co_kwonlyargcount,  #Add this in Python3
                        target_co.co_nlocals + 1,
                        target_co.co_stacksize,
                        target_co.co_flags,
                        temp_code,
                        target_co.co_consts,
                        tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                        target_co.co_varnames,
                        target_co.co_filename,
                        target_co.co_name,
                        target_co.co_firstlineno,
                        target_co.co_lnotab,   # In general, You should adjust this
                        target_co.co_freevars,
                        target_co.co_cellvars
                    ))
                else:
                    final.append(types.CodeType(
                        target_co.co_argcount,
                        # target_co.co_posonlyargcount, #Add this in Python 3.8+
                        target_co.co_kwonlyargcount,  #Add this in Python3
                        target_co.co_nlocals + 1,
                        target_co.co_stacksize,
                        target_co.co_flags,
                        temp_code,
                        target_co.co_consts,
                        tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                        target_co.co_varnames,
                        target_co.co_filename,
                        target_co.co_name,
                        target_co.co_firstlineno,
                        target_co.co_lnotab,   # In general, You should adjust this
                        target_co.co_freevars,
                        target_co.co_cellvars
                    ))
            break
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co   

    
## END Instrument code after continue

## Instrument code after function call
def instrument_after_poptop_at_the_end_of_loop(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    for offset_1 in range(0, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
        # if curr_op_jmp not in [opcode.opmap['POP_TOP']]: continue
        # Find JUMP_ABSOLUTE and POP_BLOCK
        for offset_2 in range(offset_1 + 2, len(code) -2, 2):
            curr_op_brk, curr_arg_brk = get_op_arg_offset(code, offset_2)
            # If another jump then give up
            if curr_op_brk in [opcode.EXTENDED_ARG]: continue
            # IF JUMP_ABSOLUTE followed by POP_TOP only
            print(curr_op_brk, get_op_arg_offset(code, offset_2 + 2)[0],opcode.opmap['JUMP_ABSOLUTE'], opcode.opmap['POP_BLOCK'], offset_2)
            if curr_op_brk not in [opcode.opmap['JUMP_ABSOLUTE']] or get_op_arg_offset(code, offset_2 + 2)[0] not in  [opcode.opmap['POP_BLOCK']]: break
            # Find jump absolute
            print("PATTERN FOUND!!")
            # Instrument here 
            dummy_inst = create_dummy_inst(len(target_co.co_names))
            # Instrument after POP_BLOCK
            print("Dummy created and now instrumenting")
            temp_code = update_jump_offsets_no_jumpforward(code, dummy_inst, offset_1 + 2)
            # TODO: Convert all JUMP_ABSOLUTE to curr_arg_brk into JUMP_FORWARD
            curr_os = 0
            while curr_os < offset_1:
                curr_op, curr_arg = get_op_arg_offset(temp_code, curr_os)
                if curr_op == opcode.opmap['JUMP_ABSOLUTE'] and curr_arg == curr_arg_brk:
                    # Replace with JUMP_FORWARD
                    temp_code = temp_code[:curr_os] + bytes([opcode.opmap['JUMP_FORWARD']]) + temp_code[curr_os+1:]
                    # Retarget to our instrumented one
                    start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
                    # offset is start instru
                    increment_value = (start_instru - curr_os - 2) - curr_arg
                    temp_code = update_codebyte(temp_code, curr_os + 1, increment_value)
                    curr_os = 0
                else:
                    curr_os += 2
            # covnevert offsets_ja to JUMP_FORWARD

            
            # Redirect anything that is not longer pointing back
            
            # if len(temp_code) != (len(code) + len(dummy_inst)):
            #     print("Len of code changed, please update {} {}".format(len(temp_code), (len(code) + len(dummy_inst))))    
                # raise("Len of code changed, please update ")
            # point the jump instruction this instrumented code
            # start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
            # increment_value = 2 - get_op_arg_offset(temp_code, start_instru -4)[1]
            # print("Update the jump instruction now", increment_value, start_instru -3)
            # temp_code = update_codebyte(temp_code, start_instru - 3, increment_value)
            if sys.version_info[1] > 7:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            else:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    # target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            break
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co   

    
## END Instrument code after continue

## Convert return in try and except
def convert_return_to_store_try_except(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    for offset_1 in range(0, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
        if curr_op_jmp not in [opcode.opmap['SETUP_FINALLY']]: continue
        # Find RETURN_VALUE
        for offset_2 in range(offset_1 + 2, offset_1 + curr_arg_jmp + 2, 2):
            curr_op_pop_blk, curr_arg_ret = get_op_arg_offset(code, offset_2)
            # If another jump then give up
            if curr_op_pop_blk in [opcode.EXTENDED_ARG]: continue
            # IF JUMP_ABSOLUTE followed by POP_TOP only
            if curr_op_pop_blk not in [opcode.opmap['POP_BLOCK']] or get_op_arg_offset(code, offset_2 + 2)[0] not in  [opcode.opmap['RETURN_VALUE']]: continue
            print("Found RETRUN and POP_BLOCK")
            # Find jump absolute
            instr1 = bytes([opcode.opmap['STORE_FAST']]) + bytes([target_co.co_nlocals]) # store
            instr2 = bytes([opcode.opmap['JUMP_FORWARD']])+bytes([0])
            # Instrument at POP_BLOCK
            temp_code = update_jump_offsets(code,instr1,offset_2)
            start_instru, end_instru = find_sub_list(instr1, temp_code)
            # Replace return with JUMP_FORWARD
            temp_code = temp_code[:start_instru+4] + instr2 + temp_code[start_instru+6:]
            fin_off = None
            dis.dis(temp_code)
            print("---", start_instru)
            for curr_off in range(start_instru + 2, len(temp_code), 2):
                print(">>>",get_op_arg_offset(temp_code, curr_off)[0], opcode.opmap['END_FINALLY'])
                if get_op_arg_offset(temp_code, curr_off)[0] == opcode.opmap['END_FINALLY']:
                    fin_off = curr_off
                    break
            if fin_off == None: break
            increment_value = fin_off - (start_instru + 4)
            temp_code = update_codebyte(temp_code, start_instru + 5, increment_value)
            print("PATTERN FOUND!!")
            if sys.version_info[1] > 7:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    target_co.co_names,
                    tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            else:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    # target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    target_co.co_names,
                    tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            break
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co   

def convert_return_to_store_try_except_second(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    # Store instr
    instr1 = bytes([opcode.opmap['STORE_FAST']]) + bytes([target_co.co_nlocals]) # store
    # JUMP_FORWARD
    instr2 = instr2 = bytes([opcode.opmap['JUMP_FORWARD']])+bytes([2])
    for offset_1 in range(0, len(code) -4, 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
        if not (code[offset_1] == opcode.opmap['ROT_FOUR'] and code[offset_1+2] == opcode.opmap['POP_EXCEPT']): continue
        # print("Found ROT_FOUR and POP_EXCEPT")
        # Find RETURN_VALUE
        check_ret = None
        end_seq = offset_1
        while code[end_seq] == opcode.opmap['ROT_FOUR'] or code[end_seq] == opcode.opmap['POP_EXCEPT']: 
            end_seq += 2
            if code[end_seq] == opcode.opmap['RETURN_VALUE']:
                check_ret = True
        if check_ret == None: break
        # The sequence of ROT_FOUR POP_EXCEPT + RETURN_VALUE is true

        #instrument store
        temp_code = update_jump_offsets(code,instr1,offset_1)
        start_instru, end_instru = find_sub_list(instr1, temp_code)
        start_of_rot_four = start_instru + len(instr1)
        end_seq = start_of_rot_four
        # Find end of ROT_FOUR
        while temp_code[end_seq] == opcode.opmap['ROT_FOUR'] and temp_code[end_seq+2] == opcode.opmap['POP_EXCEPT'] and end_seq< len(temp_code) - 4: end_seq += 4
        # end_seq -= 4
        # remove start_of_rot_four + end_seq + 2
        ret_off = end_seq
        if temp_code[ret_off+2] != opcode.opmap['END_FINALLY']:
            # remove everything
            while 1:
                start_instru, end_instru = find_sub_list(instr1, temp_code)
                start_instru += 2
                if temp_code[start_instru] not in [opcode.opmap['ROT_FOUR'], opcode.opmap['POP_EXCEPT'], opcode.opmap['RETURN_VALUE']]: break
                temp_code = update_jump_offsets_remove(temp_code,start_instru)
        else:
            # remove ROT_FOUR first
            # Then loop though the combination of POP_EXCEPT and ROT_FOUR
            while 1:
                start_instru, end_instru = find_sub_list(instr1, temp_code)
                start_instru += 2
                if temp_code[start_instru] == opcode.opmap['POP_EXCEPT'] and temp_code[start_instru + 2] == opcode.opmap['RETURN_VALUE']: break
                temp_code = update_jump_offsets_remove(temp_code,start_instru)
            # Replace return with jump_forward
            start_instru, end_instru = find_sub_list(instr1, temp_code)
            temp_code = temp_code[:start_instru+4] + instr2 + temp_code[start_instru+6:]

        print("PATTERN FOUND!!")
        if sys.version_info[1] > 7:
            final.append(types.CodeType(
                target_co.co_argcount,
                target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                target_co.co_names,
                tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
        else:
            final.append(types.CodeType(
                target_co.co_argcount,
                # target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                target_co.co_names,
                tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
        # break
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co   

def convert_continue_in_except(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    # Store instr
    instr1 = bytes([opcode.opmap['STORE_FAST']]) + bytes([target_co.co_nlocals]) # store
    # JUMP_FORWARD
    instr2 = instr2 = bytes([opcode.opmap['JUMP_FORWARD']])+bytes([2])
    for offset_1 in range(2, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)

        if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
        if not ( code[get_prev_offset_skipping_extended(code,offset_1)]== opcode.opmap['POP_EXCEPT'] and code[offset_1] == opcode.opmap['JUMP_ABSOLUTE']): continue
        # print("found",offset_1)
        for offset_2 in range(offset_1 + 2, len(code), 2):
            curr_op_jmp_2, curr_arg_jmp_2 = get_op_arg_offset(code, offset_2)

            if curr_op_jmp_2 in [opcode.EXTENDED_ARG]: continue
            if not (curr_arg_jmp_2 == curr_arg_jmp and code[get_prev_offset_skipping_extended(code,offset_2)]== opcode.opmap['POP_EXCEPT'] and code[offset_2] == opcode.opmap['JUMP_ABSOLUTE']): 
                # print("break", offset_2)
                continue

            # Found two consecutive
            # Time to remove
            # Remove POP_EXCEPT first
            offset_pop_except = get_prev_offset_skipping_extended(code,offset_2)
            temp_code = update_jump_offsets_remove(code,offset_pop_except)
            # Remove Jump absolute now
            temp_code = update_jump_offsets_remove(temp_code,offset_2 - 2)
            if sys.version_info[1] > 7:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals ,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    target_co.co_names,
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            else:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    # target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals ,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    target_co.co_names,
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            break
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co   

def move_return_with_block_outside(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    # Store instr
    instr1 = bytes([opcode.opmap['STORE_FAST']]) + bytes([target_co.co_nlocals]) # store
    # JUMP_FORWARD
    instr2 = instr2 = bytes([opcode.opmap['JUMP_FORWARD']])+bytes([2])
    pattern = [
        opcode.opmap['POP_BLOCK'],
        opcode.opmap['ROT_TWO'],
        opcode.opmap['BEGIN_FINALLY'],
        opcode.opmap['WITH_CLEANUP_START'],
        opcode.opmap['WITH_CLEANUP_FINISH'],
        opcode.opmap['POP_FINALLY'],
        opcode.opmap['RETURN_VALUE'],
        opcode.opmap['WITH_CLEANUP_START'],
        opcode.opmap['WITH_CLEANUP_FINISH'],
        opcode.opmap['END_FINALLY'],
        opcode.opmap['LOAD_CONST'],
        opcode.opmap['RETURN_VALUE'],
    ]
    if find_pattern_code(code, pattern) == None:
        return []
    print(find_pattern_code(code, pattern))
    offset_start, offset_end = find_pattern_code(code, pattern)
    # Instrument store
    temp_code = update_jump_offsets(code,instr1,offset_start)
    # Remove ROT_TWO
    offset_start, offset_end = find_pattern_code(temp_code, pattern)
    rot_two_offset = offset_start + 2
    temp_code = update_jump_offsets_remove(temp_code, rot_two_offset)
    # Remove 4 instruction from WITH_CLEANUP_START to RETURN_VALUE
    for x in range(4):
        start_instru, end_instru = find_sub_list(instr1, temp_code)
        # +2 is POP +2 BEGIN_FINALLY +2 is to remove
        temp_code = update_jump_offsets_remove(temp_code, start_instru + 6)
    # Convert loadconst to LOAD_FAST
    start_instru, end_instru = find_sub_list(instr1, temp_code)
    while start_instru< len(temp_code) and temp_code[start_instru] != opcode.opmap['LOAD_CONST']:
        start_instru += 2
    if start_instru >= len(temp_code): return []
    temp_code = temp_code[:start_instru] + bytes([opcode.opmap['LOAD_FAST']]) + temp_code[start_instru+1:]
    # Update load_fast arg
    op, arg = get_op_arg_offset(temp_code, start_instru)
    target_arg = target_co.co_nlocals - arg
    temp_code = update_codebyte(temp_code, start_instru, target_arg)
    if sys.version_info[1] > 7:
        final.append(types.CodeType(
            target_co.co_argcount,
            target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            target_co.co_names,
            tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    else:
        final.append(types.CodeType(
            target_co.co_argcount,
            # target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            target_co.co_names,
            tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co  
    # for offset_1 in range(2, len(code), 2):
    #     curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)


def convert_return_with_block(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    # Store instr
    instr1 = bytes([opcode.opmap['STORE_FAST']]) + bytes([target_co.co_nlocals]) # store
    # JUMP_FORWARD
    instr2 = instr2 = bytes([opcode.opmap['JUMP_FORWARD']])+bytes([2])
    pattern = [
        opcode.opmap['POP_BLOCK'],
        opcode.opmap['ROT_TWO'],
        opcode.opmap['BEGIN_FINALLY'],
        opcode.opmap['WITH_CLEANUP_START'],
        opcode.opmap['WITH_CLEANUP_FINISH'],
        opcode.opmap['POP_FINALLY'],
        opcode.opmap['RETURN_VALUE'],
        opcode.opmap['WITH_CLEANUP_START'],
        opcode.opmap['WITH_CLEANUP_FINISH'],
        opcode.opmap['END_FINALLY']
    ]
    if find_pattern_code(code, pattern) == None:
        return []
    print(find_pattern_code(code, pattern))
    offset_start, offset_end = find_pattern_code(code, pattern)
    # Instrument store
    temp_code = update_jump_offsets(code,instr1,offset_start)
    # Remove ROT_TWO
    offset_start, offset_end = find_pattern_code(temp_code, pattern)
    rot_two_offset = offset_start + 2
    temp_code = update_jump_offsets_remove(temp_code, rot_two_offset)
    # Remove 4 instruction from WITH_CLEANUP_START to RETURN_VALUE
    for x in range(4):
        start_instru, end_instru = find_sub_list(instr1, temp_code)
        # +2 is POP +2 BEGIN_FINALLY +2 is to remove
        temp_code = update_jump_offsets_remove(temp_code, start_instru + 6)
    if sys.version_info[1] > 7:
        final.append(types.CodeType(
            target_co.co_argcount,
            target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            target_co.co_names,
            tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    else:
        final.append(types.CodeType(
            target_co.co_argcount,
            # target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            target_co.co_names,
            tuple(list(target_co.co_varnames)+[get_local_var_name(list(target_co.co_varnames))]),
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co  
    # for offset_1 in range(2, len(code), 2):
    #     curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)

def convert_breaks_with_variable_in_except_block(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    
    dummy_inst = create_dummy_inst(len(target_co.co_names))
    for offset_1 in range(2, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
        if not (code[offset_1] == opcode.opmap['JUMP_ABSOLUTE'] and get_op_arg_offset(code,get_prev_offset_skipping_extended(code,offset_1))[0] == opcode.opmap['POP_EXCEPT']): continue
        # Check if target prev instruction is jump_absolute
        if not(get_op_arg_offset(code,get_prev_offset_skipping_extended(code,curr_arg_jmp))[0] == opcode.opmap['JUMP_ABSOLUTE'] and curr_arg_jmp > offset_1): continue
        print("PATTERN FOUND!!")
        # Instrument our instruction
        instru_spot = get_prev_offset_skipping_extended(code,offset_1)
        # print(instru_spot)
        temp_code = update_jump_offsets(code,dummy_inst,instru_spot)
        start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
        print(end_instru)
        # Remove instructions now
        temp_code = update_jump_offsets_remove(temp_code, end_instru + 1)
        start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
        # Remove jump absolute
        end_instru += 1
        while temp_code[end_instru] == opcode.EXTENDED_ARG:
            end_instru += 2
        temp_code = update_jump_offsets_remove(temp_code, end_instru)
        print("final:")
        # dis.dis(temp_code)
        if sys.version_info[1] > 7:
            final.append(types.CodeType(
                target_co.co_argcount,
                target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                target_co.co_varnames,
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
        else:
            final.append(types.CodeType(
                target_co.co_argcount,
                # target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                target_co.co_varnames,
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
        dis.dis(final[-1])
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co  


def convert_break_if_last_instruction_in_loop(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    
    dummy_inst = create_dummy_inst(len(target_co.co_names))
    for offset_1 in range(2, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
        # Check if current instruciton JUMP_ABSOLUTE and Prev too
        if not (code[offset_1] == opcode.opmap['JUMP_ABSOLUTE'] and get_op_arg_offset(code,get_prev_offset_skipping_extended(code,offset_1))[0] == opcode.opmap['JUMP_ABSOLUTE']): continue
        # Check the args
        # Check if target prev instruction is jump_absolute
        if not(get_op_arg_offset(code,get_prev_offset_skipping_extended(code,offset_1))[1] > offset_1 and curr_arg_jmp < get_prev_offset_skipping_extended(code,offset_1)): continue
        print("PATTERN FOUND!!")
        # Instrument our instruction
        instru_spot = get_prev_offset_skipping_extended(code,offset_1)
        while code[instru_spot -2] ==  opcode.EXTENDED_ARG: instru_spot -= 2
        # print(instru_spot)
        temp_code = update_jump_offsets(code,dummy_inst,instru_spot)
        # Remove Jump absolute
        start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
        # Remove jump absolute
        end_instru += 1
        while temp_code[end_instru] == opcode.EXTENDED_ARG:
            end_instru += 2
        temp_code = update_jump_offsets_remove(temp_code, end_instru)
        # find target
        start_instru, end_instru = find_sub_list(dummy_inst, temp_code)
        end_instru += 1
        while temp_code[end_instru] == opcode.EXTENDED_ARG:
            end_instru += 2
        preserve_arg = end_instru + 2
        # Convert JUMP_ABSOLUTE to JUMP_FORWARD
        offset_iter = 0
        while offset_iter < start_instru:
            op_temp, arg_temp = get_op_arg_offset(temp_code, offset_iter)
            # print(offset_iter, op_temp, arg_temp, preserve_arg)
            if not(op_temp == opcode.opmap['JUMP_ABSOLUTE'] and arg_temp == preserve_arg):
                offset_iter += 2
                continue
            # Make into JUMP_FORWARD
            temp_code = temp_code[:offset_iter]  + bytes([opcode.opmap['JUMP_FORWARD']]) + temp_code[offset_iter+1:] 

            diff_offset = (start_instru - offset_iter - 2) - arg_temp
            temp_code = update_codebyte(temp_code, offset_iter + 1, diff_offset)
            offset_iter = 0
            start_instru, end_instru = find_sub_list(dummy_inst, temp_code)

            
        print("final:")
        # dis.dis(temp_code)
        if sys.version_info[1] > 7:
            final.append(types.CodeType(
                target_co.co_argcount,
                target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                target_co.co_varnames,
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
        else:
            final.append(types.CodeType(
                target_co.co_argcount,
                # target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                target_co.co_varnames,
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
        # dis.dis(final[-1])
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co  

def convert_continue_with_try_block(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    # First find any
    dis.dis(code)
    # Store instr
    instr1 = create_dummy_inst(len(target_co.co_names)) # store
    # JUMP_FORWARD
    instr2 = instr2 = bytes([opcode.opmap['JUMP_FORWARD']])+bytes([2])
    pattern = [
        opcode.opmap['POP_BLOCK'],
        opcode.opmap['BEGIN_FINALLY'],
        opcode.opmap['WITH_CLEANUP_START'],
        opcode.opmap['WITH_CLEANUP_FINISH'],
        opcode.opmap['POP_FINALLY'],
        opcode.opmap['POP_BLOCK'],
        opcode.opmap['JUMP_ABSOLUTE'],
    ]
    if find_pattern_code(code, pattern) == None:
        return []
    print(find_pattern_code(code, pattern))
    offset_start, offset_end = find_pattern_code(code, pattern)
    # Instrument store
    temp_code = update_jump_offsets(code,instr1,offset_start)
    # Remove 7 instruction from WITH_CLEANUP_START to RETURN_VALUE
    for x in range(7):
        start_instru, end_instru = find_sub_list(instr1, temp_code)
        # +2 is POP +2 BEGIN_FINALLY +2 is to remove
        end_instru += 1
        while temp_code[end_instru] == opcode.EXTENDED_ARG: end_instru += 2
        temp_code = update_jump_offsets_remove(temp_code, end_instru)
    if sys.version_info[1] > 7:
        final.append(types.CodeType(
            target_co.co_argcount,
            target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
            target_co.co_varnames,
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    else:
        final.append(types.CodeType(
            target_co.co_argcount,
            # target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
            target_co.co_varnames,
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co  
    # for offset_1 in range(2, len(code), 2):
    #     curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
            
## DECOMPYLE3 manipulations
def convert_not_in_loop_boolean(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    code = target_co.co_code
    dummy_inst = bytes([opcode.opmap['UNARY_NOT']])+bytes([0])
    target_set = [
        opcode.opmap['POP_JUMP_IF_TRUE'],
        opcode.opmap['POP_JUMP_IF_FALSE']
    ]
    exit_set= [
        90, # name_op('STORE_NAME', 90) 
        95, # name_op('STORE_ATTR', 95) # Index in name list
        97, # name_op('STORE_GLOBAL', 97)     # ""
        125, # def_op('STORE_FAST', 125)       # Local variable number
        83, # def_op('RETURN_VALUE', 83)
        86, # def_op('YIELD_VALUE', 86)
    ]
    # Find SETUP_LOOP
    for offset_1 in range(2, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
        if not (code[offset_1] == opcode.opmap['SETUP_LOOP']): continue
        # Find the chain of booleans
        boolean_chain = []
        max_val = offset_1 + curr_arg_jmp # max value to jump
        for offset_2 in range(offset_1 + 2, len(code), 2):
            curr_op_jmp2, curr_arg_jmp2 = get_op_arg_offset(code, offset_2)
            if curr_op_jmp2 in [opcode.EXTENDED_ARG]: continue
            if curr_op_jmp2 in exit_set: break
            if curr_op_jmp2 in target_set and curr_arg_jmp2 == max_val:
                boolean_chain = boolean_chain + [(curr_op_jmp2, offset_2)]
        if len(boolean_chain) == 0: continue
        # Check the last jump instruction
        curr_op, curr_off = boolean_chain[-1]
        if curr_op != opcode.opmap['POP_JUMP_IF_TRUE']: continue
        # Now update the instruction
        temp_code = code[:curr_off] + bytes([opcode.opmap['POP_JUMP_IF_FALSE']]) + code[curr_off + 1:]
        # Now instrument your NOT
        prev_offset = get_prev_offset_skipping_extended(temp_code,curr_off)
        temp_code = update_jump_offsets(temp_code, dummy_inst, prev_offset + 2)
        if sys.version_info[1] > 7:
            final.append(types.CodeType(
                target_co.co_argcount,
                target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                target_co.co_varnames,
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
        else:
            final.append(types.CodeType(
                target_co.co_argcount,
                # target_co.co_posonlyargcount, #Add this in Python 3.8+
                target_co.co_kwonlyargcount,  #Add this in Python3
                target_co.co_nlocals + 1,
                target_co.co_stacksize,
                target_co.co_flags,
                temp_code,
                target_co.co_consts,
                tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                target_co.co_varnames,
                target_co.co_filename,
                target_co.co_name,
                target_co.co_firstlineno,
                target_co.co_lnotab,   # In general, You should adjust this
                target_co.co_freevars,
                target_co.co_cellvars
            ))
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co  
## DECOMPYLE3 manipulations end

## Python 3.9 cross compilation

def convert_3_9_co(co):
    pass
    a = ""
    # print(co.co_name)
    #a = "print('');"
    c = compile(a, '<string>', 'exec')
    nop_code = c.co_code[-4:]
    nop_flag = False
    temp_code = co.co_code
    temp_co_names = list(co.co_names)
    curr_offset = 0
    # print(co.co_name, len(temp_code))
    check_build_list = True
    check_build_map = True
    check_build_set = True
    check_except = True
    check_transform = False
    output = dis.Bytecode(co).dis()
    while curr_offset < len(temp_code):
        # print(curr_offset,end=",")
        if curr_offset < 0: curr_offset = 0
        curr_op, curr_arg = get_op_arg_offset(temp_code, curr_offset)
        if curr_op == opcode.opmap['SETUP_WITH']:
            print(co.co_name, ":9",end='/')
            check_transform = True
            nop_flag = True
            break
        elif curr_op == opcode.opmap['SETUP_FINALLY']:
            check_offset = -1
            
            for offset_1 in range(curr_offset, curr_offset+ curr_arg, 2):
                if temp_code[offset_1] == opcode.opmap['POP_BLOCK']:
                    check_offset = offset_1+2
                    break
            if check_offset != -1 and temp_code[check_offset] == temp_code[curr_offset + curr_arg + 2]:
                print(co.co_name, ":10",end='/')
                nop_flag = True
                break
            check_transform = True
            curr_offset += 2
            continue
        elif curr_op == opcode.opmap['BUILD_MAP'] and check_build_map:
            # output = dis.Bytecode(co).dis()
            pattern = "BUILD_MAP[\s\S]*<165>[\s\S]*BUILD_CONST_KEY_MAP[\s\S]*<165>"
            match_result = re.search(pattern, output)
            check_transform = True
            if match_result:
                print(co.co_name, ":7",end='/')
                nop_flag = True
                break
            curr_offset -= 2
            check_build_map = False
            continue
        elif curr_op == opcode.opmap['BUILD_SET'] and check_build_set:
            # output = dis.Bytecode(co).dis()
            pattern = "BUILD_SET[\s\S]*LOAD_CONST[\s\S]*POP_FINALLY"
            match_result = re.search(pattern, output)
            check_transform = True
            if match_result:
                print(co.co_name, ":13",end='/')
                nop_flag = True
                break
            curr_offset -= 2
            check_build_set = False
            continue
        elif curr_op == opcode.opmap['BUILD_LIST'] and check_build_list:
            # output = dis.Bytecode(co).dis()
            pattern1 = "BUILD_LIST[\s\S]*LOAD_FAST[\s\S]*CALL_FINALLY[\s\S]*WITH_CLEANUP_FINISH[\s\S]*(<164>)?[\s\S]*CALL_FUNCTION_EX"
            match_result = re.search(pattern1, output)
            check_transform = True
            if match_result:
                print(co.co_name, ":11",end='/')
                nop_flag = True
                break
            pattern2 = "BUILD_LIST[\s\S]*LOAD_CONST[\s\S]*CALL_FINALLY"
            match_result = re.search(pattern2, output)
            check_transform = True
            if match_result:
                print(co.co_name, ":12",end='/')
                nop_flag = True
                break
            curr_offset -= 2
            check_build_list = False
            continue
        
        elif curr_op == 121: 
            # if co.co_name == "complete": dis.dis(temp_code)
            # <121> - Replace with `[COMPARE_OP][POP_JUMP_IF_FALSE]` 10
            prepend_inst = bytes([opcode.opmap['COMPARE_OP']])+bytes([10])
            replace_inst = bytes([opcode.opmap['POP_JUMP_IF_FALSE']])
            # Add POP_JUMP_IF_FALSE
            check_transform = True
            temp_code = temp_code[:curr_offset] + replace_inst + temp_code[curr_offset + 1:]
            # Pre-pend instruction now
            prev_offset = get_prev_offset_skipping_extended(temp_code,curr_offset)
            temp_code = update_jump_offsets_3_9(temp_code, prepend_inst, prev_offset + 2)
            print(co.co_name, ":1",end='/')
            # if co.co_name == "complete": dis.dis(temp_code)
        elif curr_op == 48 and check_except:
            #`<48><48>` - Replace with `END_FINALLY`, `POP_EXCEPT` `JUMP_FORWARD` `END_FINALLY`
            check_transform = True
            pattern = "SETUP_FINALLY[\s\S]*POP_BLOCK[\s\S]*POP_EXCEPT[\s\S]*JUMP_FORWARD[\s\S]*<48>[\s\S]*<48>"
            match_result = re.search(pattern, output)
            if match_result:
                print(co.co_name, ":3",end='/')
                nop_flag = True
                break
            curr_offset -= 2
            check_except = False
            continue
            print(co.co_name, ":3",end='/')
            nop_flag = True
            break
            # replace_inst = bytes([opcode.opmap['END_FINALLY']])
            # add_inst = bytes([opcode.opmap['POP_EXCEPT']]) + bytes([0]) + bytes([opcode.opmap['JUMP_FORWARD']]) + bytes([2])
            # temp_code = temp_code[:curr_offset] + replace_inst + temp_code[curr_offset + 1:]
            # temp_code = update_jump_offsets_3_9(temp_code, add_inst, curr_offset + 2)
        elif curr_op == 48:
            # `<48>` - Replace with `END_FINALLY`
            replace_inst = bytes([opcode.opmap['END_FINALLY']])
            check_transform = True
            temp_code = temp_code[:curr_offset] + replace_inst + temp_code[curr_offset + 1:]
            print(co.co_name, ":2",end='/')
        elif curr_op == 117:
            # `<117>` - Replace with `COMPARE_OP` 8 or 9
            replace_inst = bytes([opcode.opmap['COMPARE_OP']]) + bytes([9]) if curr_arg == 1 else bytes([opcode.opmap['COMPARE_OP']]) + bytes([8])
            check_transform = True
            temp_code = temp_code[:curr_offset] + replace_inst + temp_code[curr_offset + 2:]
            print(co.co_name, ":4",end='/')
        elif curr_op == 118:
            # `<118>` - Replace with `COMPARE_OP` 6 or 7
            replace_inst = bytes([opcode.opmap['COMPARE_OP']]) + bytes([7]) if curr_arg == 1 else bytes([opcode.opmap['COMPARE_OP']]) + bytes([6])
            check_transform = True
            temp_code = temp_code[:curr_offset] + replace_inst + temp_code[curr_offset + 2:]
            print(co.co_name, ":5",end='/')
        elif curr_op == 164 and curr_arg == 1:
            # `<164>` - Replace with `BUILD_MAP_UNPACK_WITH_CALL`
            replace_inst = bytes([opcode.opmap['BUILD_MAP_UNPACK_WITH_CALL']]) + bytes([2])
            check_transform = True
            temp_code = temp_code[:curr_offset] + replace_inst + temp_code[curr_offset + 2:]
            print(co.co_name, ":6",end='/')
        elif curr_op == 74:
            # `<74>` - Replace with `LOAD_GLOBAL`
            check_transform = True
            try:
                index_assert = len(temp_co_names)
                if 'AssertionError' in temp_co_names:
                    index_assert = temp_co_names.index('AssertionError')
                replace_inst = bytes([opcode.opmap['LOAD_GLOBAL']]) + bytes([index_assert])
                temp_code = temp_code[:curr_offset] + replace_inst + temp_code[curr_offset + 2:]
                # Add assertion error
                if index_assert == len(temp_co_names):
                    temp_co_names += ['AssertionError']
                print(co.co_name, ":8",end='/')
            except:
                print(co.co_name, ":8",end='/')
                nop_flag = True
                break      
        else:
            curr_offset += 2
            continue
        curr_offset += 2
    if check_transform:
        output = dis.Bytecode(co).dis() if nop_flag else dis.Bytecode(types.CodeType(
            co.co_argcount,
            co.co_posonlyargcount, #Add this in Python 3.8+
            co.co_kwonlyargcount,  #Add this in Python3
            co.co_nlocals,
            co.co_stacksize,
            co.co_flags,
            temp_code,
            co.co_consts,
            tuple(temp_co_names),#tuple(list(co.co_names) + [get_local_var_name(list(co.co_names))]),
            co.co_varnames,
            co.co_filename,
            co.co_name,
            co.co_firstlineno,
            co.co_lnotab,   # In general, You should adjust this
            co.co_freevars,
            co.co_cellvars
        )).dis()
        jump_string = [opcode.opname[i] for i in  opcode.hasjabs] + [opcode.opname[i] for i in  opcode.hasjrel] + ['<121>']
        if not any(ext in output for ext in jump_string):
            with open("all_blocks.log",'a') as f:
                print(">>{}<<".format(co.co_name), file=f)            

    if nop_flag:
        return types.CodeType(
            co.co_argcount,
            co.co_posonlyargcount, #Add this in Python 3.8+
            co.co_kwonlyargcount,  #Add this in Python3
            co.co_nlocals,
            co.co_stacksize,
            co.co_flags,
            nop_code,
            co.co_consts,
            tuple(temp_co_names),#tuple(list(co.co_names) + [get_local_var_name(list(co.co_names))]),
            co.co_varnames,
            co.co_filename,
            co.co_name,
            co.co_firstlineno,
            co.co_lnotab,   # In general, You should adjust this
            co.co_freevars,
            co.co_cellvars
        ) 

    return types.CodeType(
        co.co_argcount,
        co.co_posonlyargcount, #Add this in Python 3.8+
        co.co_kwonlyargcount,  #Add this in Python3
        co.co_nlocals,
        co.co_stacksize,
        co.co_flags,
        temp_code,
        co.co_consts,
        tuple(temp_co_names),#tuple(list(co.co_names) + [get_local_var_name(list(co.co_names))]),
        co.co_varnames,
        co.co_filename,
        co.co_name,
        co.co_firstlineno,
        co.co_lnotab,   # In general, You should adjust this
        co.co_freevars,
        co.co_cellvars
    ) 


def convert_3_9_all(co):
    # print(co.co_name, fn_name)
    # print(type(co.co_name), type(fn_name))
    # print(len(co.co_name), len(fn_name))
    # if fn_name == co.co_name: 
    #     return co
    # Recursively fix all code objects
    # a= "assert 1==1"
    # c = compile(a, '<string>', 'exec')
    # dis.dis(c)
    temp_co_consts = []
    for const in co.co_consts:
        if isinstance(const, types.CodeType):
            temp_co = convert_3_9_all(const)
            temp_co_consts = temp_co_consts + [temp_co]
        else:
            temp_co_consts += [const]
    # Fix current code_object
    co = convert_3_9_co(co)
    return types.CodeType(
        co.co_argcount,
        co.co_posonlyargcount, #Add this in Python 3.8+
        co.co_kwonlyargcount,  #Add this in Python3
        co.co_nlocals,
        co.co_stacksize,
        co.co_flags,
        co.co_code,
        tuple(temp_co_consts),
        co.co_names,#tuple(list(co.co_names) + [get_local_var_name(list(co.co_names))]),
        co.co_varnames,
        co.co_filename,
        co.co_name,
        co.co_firstlineno,
        co.co_lnotab,   # In general, You should adjust this
        co.co_freevars,
        co.co_cellvars
    )
    # return None
## Python 3.9 cross compilation end

def flatten_co(co):
    # print(co.co_name, fn_name)
    # print(type(co.co_name), type(fn_name))
    # print(len(co.co_name), len(fn_name))
    # if fn_name == co.co_name: 
    #     return co
    # Recursively fix all code objects
    # a= "assert 1==1"
    # c = compile(a, '<string>', 'exec')
    # dis.dis(c)
    if co == None:
        return []
    temp_co_consts = []
    for const in co.co_consts:
        if isinstance(const, types.CodeType):
            temp_co = flatten_co(const)
            temp_co_consts = temp_co_consts + temp_co
    # Fix current code_object
    
    return  temp_co_consts + [co]
def toy_example(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    print("Found!")
    dis.dis(target_co)
    final = []  # Generate manipluated co and return in this
    code = target_co.co_code
    # Print code object
    # dis.dis(code)
    # Manipulate your code here
    temp_code = code[:32] + bytes([opcode.opmap['POP_JUMP_IF_FALSE']]) + code[33:]
    dummy_inst = bytes([opcode.opmap['UNARY_NOT']])+bytes([0]) #create_dummy_inst(len(target_co.co_names))
    temp_code = update_jump_offsets(temp_code, dummy_inst, 32)
    # Iterate through the instructions in the multiples of two
    # Find JUMP_ABSOLUTE and instrument after it
    # temp_code = code[:4] +  bytes([opcode.opmap['LOAD_GLOBAL']]) + code[5:]
    # dis.dis(temp_code)

    # for offset_1 in range(0, len(code), 2):
    #     # Get OP and ARG of the code at current offset
    #     curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
    #     # Skip extended args
    #     if curr_op_jmp in [opcode.EXTENDED_ARG]: continue
    #     # Check if current instruciton JUMP_ABSOLUTE and Prev too
    #     if not (code[offset_1] == opcode.opmap['LOAD_DEREF']): continue
    #     # instrument after JUMP_ABSOLUTE
    #     print("FOUND AT", offset_1)
    #     temp_code = update_jump_offsets_remove(code, offset_1)
    #     dis.dis(temp_code)
    #     # break
    #     # temp_code = update_jump_offsets(code, dummy_inst, offset_1 + 2)
    #     # Note that above is +2 so we instrument after JUMP_ABSOLUTE
    #     # Create full code object and append to final list
    
    if sys.version_info[1] > 7:
        final.append(types.CodeType(
            target_co.co_argcount,
            target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            # tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
            target_co.co_names,
            target_co.co_varnames,
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    else:
        final.append(types.CodeType(
            target_co.co_argcount,
            # target_co.co_posonlyargcount, #Add this in Python 3.8+
            target_co.co_kwonlyargcount,  #Add this in Python3
            target_co.co_nlocals + 1,
            target_co.co_stacksize,
            target_co.co_flags,
            temp_code,
            target_co.co_consts,
            #tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
            target_co.co_names,
            target_co.co_varnames,
            target_co.co_filename,
            target_co.co_name,
            target_co.co_firstlineno,
            target_co.co_lnotab,   # In general, You should adjust this
            target_co.co_freevars,
            target_co.co_cellvars
        ))
    # final processing
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    dis.dis(final[0])
    return final_co  
    

def convert_continue_general(co, fn_name):
    target_co = get_co_fn(co, fn_name)
    if target_co is None:
        print("Function '{}' not found.".format(fn_name))
        return []
    final = []
    # dis.dis(target_co)
    instr1 = create_dummy_inst(len(target_co.co_names)) # store
    
    code = target_co.co_code
    for offset_1 in range(0, len(code), 2):
        curr_op_jmp, curr_arg_jmp = get_op_arg_offset(code, offset_1)
        if not (curr_op_jmp in [opcode.opmap['JUMP_ABSOLUTE']] and curr_arg_jmp < offset_1): continue
        # Find JUMP_FORWARD and POP_TOP
        for offset_2 in range(offset_1 + 2, len(code), 2):
            curr_op_brk, curr_arg_brk = get_op_arg_offset(code, offset_2)
            # If another jump then give up
            if curr_op_brk in [opcode.EXTENDED_ARG]: continue
            # IF JUMP_ABSOLUTE followed by POP_TOP only
            if not(curr_op_brk in [opcode.opmap['JUMP_ABSOLUTE']] and curr_arg_brk == curr_arg_jmp): continue
            # Instrument our instruction
            temp_code = update_jump_offsets(code,instr1,offset_1)
            # Remove 7 instruction from WITH_CLEANUP_START to RETURN_VALUE
            for x in range(1):
                start_instru, end_instru = find_sub_list(instr1, temp_code)
                # +2 is POP +2 BEGIN_FINALLY +2 is to remove
                end_instru += 1
                while temp_code[end_instru] == opcode.EXTENDED_ARG: end_instru += 2
                temp_code = update_jump_offsets_remove(temp_code, end_instru)
            # Find jump absolute
            if sys.version_info[1] > 7:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            else:
                final.append(types.CodeType(
                    target_co.co_argcount,
                    # target_co.co_posonlyargcount, #Add this in Python 3.8+
                    target_co.co_kwonlyargcount,  #Add this in Python3
                    target_co.co_nlocals + 1,
                    target_co.co_stacksize,
                    target_co.co_flags,
                    temp_code,
                    target_co.co_consts,
                    tuple(list(target_co.co_names) + [get_local_var_name(list(target_co.co_names))]),
                    target_co.co_varnames,
                    target_co.co_filename,
                    target_co.co_name,
                    target_co.co_firstlineno,
                    target_co.co_lnotab,   # In general, You should adjust this
                    target_co.co_freevars,
                    target_co.co_cellvars
                ))
            break
    final_co = []
    for x in final:
        try:
            print("CO:", x)
            final_co.append(recursively_update_target_fn(co, fn_name, x))
        except Exception as a:
            print(a)
            continue
    return final_co 
def main():
    # create_dummy_inst()    
    raise Exception("Invoked")
    co = readpyc.read_file_get_object(input_f)
    # co = readpyc.read_file_get_object('test/solution.pyc') # Get manipulated code object here
    # print(co)
    # temp = analyse_co_fn(co, "is_at_turn")
    #temp = add_dummy_at_offset(co, 44, "is_at_turn")
    temp = add_dummy_at_offset(co, 32, "target_FUNC_ANNOTATED")
    #temp = add_dummy_at_offset(co, 34, "lstadd")
    if temp is not None:
        print("Updated!")
    readpyc.write_file(input_f, output_f, temp)
