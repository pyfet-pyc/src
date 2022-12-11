import sys
import dis
import pygraphviz
sys.path.insert(0, './lib')
import readpyc
import opcode

class Instruction_27:
    def __init__(self, opname, offset):
        self.opname = opname
        self.offset = offset

class CFGNode:
    def __init__(self, i, bid, isTarget= False):
        self.i = i
        self.first_node_id = -1
        self.last_node_id = -1
        self.nid = 0
        self.bid = bid
        self.block = False
        self.ins = []
        self.children = []
        self.parent = []
        self.props = {}
        self.isTarget = isTarget
    def add_inst(self, n):
        self.ins.append(n)        
    def add_child(self, n): 
        self.children.append(n)
        n.parent.append(self)

ops_list = [ 
# load/store
'LOAD_CONST', 'LOAD_FAST', 'STORE_FAST', 'STORE_NAME', 'LOAD_NAME', 'STORE_ATTR', 'LOAD_ATTR', 'LOAD_GLOBAL', 'STORE_GLOBAL',
'STORE_SUBSCR', 'STORE_DEREF', 'LOAD_CLOSURE', 'GET_AWAITABLE', 'LOAD_DEREF', 'STORE_ANNOTATION', 'FORMAT_VALUE',
# compare
'COMPARE_OP',
# arithmetic
'INPLACE_ADD', 'INPLACE_SUBTRACT', 'UNPACK_SEQUENCE', 'DELETE_FAST', 'BINARY_ADD', 'BINARY_MODULO', 'BINARY_SUBSCR',
'BINARY_MULTIPLY', 'BINARY_ADD', 'DELETE_SUBSCR', 'UNARY_NOT', 'LIST_APPEND', 'MAP_ADD', 'SET_ADD', 'BINARY_OR', 
'BINARY_FLOOR_DIVIDE', 'BINARY_SUBTRACT', 'ROT_TWO', 'ROT_THREE', 'DUP_TOP_TWO', 'UNARY_POSITIVE', 'UNARY_NEGATIVE',
'BINARY_MATRIX_MULTIPLY','UNARY_INVERT', 'INPLACE_MATRIX_MULTIPLY', 'BINARY_POWER', 'INPLACE_FLOOR_DIVIDE',
# functions
'MAKE_FUNCTION', 'CALL_FUNCTION', 'CALL_FUNCTION_KW', 'CALL_FUNCTION_EX', 'RETURN_VALUE', 'EXTENDED_ARG', 'LOAD_METHOD', 'CALL_METHOD',
# class
'LOAD_BUILD_CLASS',
# stack
'POP_BLOCK', 'POP_TOP', 'DUP_TOP', 
# data structure
'BUILD_LIST', 'BUILD_MAP',  'BUILD_TUPLE', 'BUILD_CONST_KEY_MAP', 'BUILD_SLICE', 'BUILD_STRING', 'BUILD_SET',
# for
'FOR_ITER', 'BREAK_LOOP', 'GET_ITER', 'GET_AITER', 'GET_ANEXT', 'CONTINUE_LOOP', 'GET_YIELD_FROM_ITER',
# try catch
'END_FINALLY', 'RAISE_VARARGS', 'POP_EXCEPT', 'BEGIN_FINALLY', 'POP_FINALLY',
# import
'IMPORT_FROM', 'IMPORT_NAME', 'IMPORT_STAR',
# etc
'YIELD_FROM', 'YIELD_VALUE', 'SETUP_ANNOTATIONS', 'BEFORE_ASYNC_WITH', 'WITH_CLEANUP_START',
'WITH_CLEANUP_FINISH',
# ???
'<0>', '<6>', '<7>', '<8>', 'NOP', '<13>', '<18>', '<14>', '<21>', '<30>', '<32>', '<34>', '<36>', '<39>', '<41>',
'<43>', '<33>', 'UNPACK_EX'
];

ops_jumps = ['POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'JUMP_IF_TRUE_OR_POP', 'JUMP_IF_FALSE_OR_POP', 'JUMP_ABSOLUTE'] + [ opcode.opname[i] for i in opcode.hasjabs] ;
ops_relative_jumps = ['JUMP_FORWARD'] + [ opcode.opname[i] for i in opcode.hasjrel];

ops_setups = ['SETUP_EXCEPT', 'SETUP_FINALLY', 'SETUP_ASYNC_WITH', 'SETUP_WITH'];
class CFG:
    def __init__(self, codeobject, target_offset=-1):
        def lstadd(hmap, key, val):
            if key not in hmap:
                hmap[key] = [val]
            else:
                hmap[key].append(val)
        enter = CFGNode(Instruction_27('NOP', 0), 0)
        last = enter
        self.target_offset = target_offset
        self.jump_to = {}
        self.opcodes = {}
        return_nodes = []
        #for i,ins in enumerate(dis.get_instructions(myfn)):
        for i,ins in enumerate(dis.get_instructions(codeobject)):
            byte = ins.offset #i * 2
            node = CFGNode(ins, byte)
            node.nid = byte
            self.opcodes[byte] = node
            #print(i,ins)
            # print(ins, ins.offset, type(ins.offset))
            if ins.offset == target_offset:
                node.isTarget = True
            if ins.opname in ops_list:
                last.add_child(node)
                last = node
                if ins.opname == 'RETURN_VALUE':
                    return_nodes.append(node)
            elif ins.opname in ops_jumps:
                lstadd(self.jump_to, ins.arg, node)
                node.props['jmp'] = True
                last.add_child(node)
                last = node
            elif ins.opname in ops_relative_jumps:
                node.props['jmp'] = True
                lstadd(self.jump_to, (i+1)*2 + ins.arg, node)
                last.add_child(node)
                last = node
            elif ins.opname == 'SETUP_LOOP':
                last.add_child(node)
                last = node
            elif ins.opname in ops_setups:
                lstadd(self.jump_to, (i+1)*2 + ins.arg, node)
                node.props['jmp'] = True
                last.add_child(node)
                last = node
            else:
                print( ins )
                print( ins.opname )
                assert False
        # print ("last inst:", byte)
        if target_offset == -1: 
            self.target_offset = last.bid
            last.isTarget = True
        for byte in self.opcodes:
            if  byte in self.jump_to:
                node = self.opcodes[byte]
                assert node.i.is_jump_target
                for b in self.jump_to[byte]:
                    b.add_child(node)
                    
                    
        for rnodes in return_nodes:
            rnodes.children.clear()
        
        block_nodes = []
        for nid, cnode in self.opcodes.items():
            #if len(cnode.children) == 1 and len(cnode.parent) == 1:
            if len(cnode.children) == 1:
                if len(cnode.children[0].parent) == 1:
                    cnode.block = True            
                    block_nodes.append(cnode)
                    #print (nid)
        
        for cnode in block_nodes:
            first_node = cnode
            last_node = cnode
            
            traversed_node = []
            
            if cnode.first_node_id == -1:
                while True:
                    if len(last_node.parent) > 0 and first_node.parent[0].block == True:
                        first_node = first_node.parent[0]
                        traversed_node.append(first_node)
                    else:
                        break
                cnode.first_node_id = first_node.nid;
            if cnode.last_node_id == -1:
                while True:
                    if len(last_node.children) > 0 and last_node.children[0].block == True:
                        last_node = last_node.children[0]
                        traversed_node.append(last_node)
                    else:
                        break
                cnode.last_node_id = last_node.nid;
            for node in traversed_node:
                node.first_node_id = first_node.nid;
                node.last_node_id = last_node.nid;
            
            
        node_to_del = []
        for cnode in block_nodes:
            if cnode.children[0].block == True:
                # merge                
                merging_to = self.opcodes[cnode.first_node_id];
                merged_children = self.opcodes[cnode.last_node_id].children;
                node_to_del.append(cnode.children[0].nid);
                merging_to.ins.append(cnode.children[0])
                merging_to.children = merged_children
                
        for node in node_to_del:
            del self.opcodes[node];
        
        
        node_to_del.clear()
        for nid, cnode in self.opcodes.items():
            if len(cnode.children) == 1:
                if len(cnode.children[0].parent) == 1:
                    merging_to = self.opcodes[nid];
                    merged_children = self.opcodes[cnode.children[0].nid].children;
                    node_to_del.append(cnode.children[0].nid);
                    merging_to.ins.append(cnode.children[0])
                    for n in cnode.children[0].ins:
                        merging_to.ins.append( n )
                    merging_to.children = merged_children

        
        for node in node_to_del:
            del self.opcodes[node];
    
    def to_graph(self, benign = False):
        G = pygraphviz.AGraph(directed=True)
        for nid, cnode in self.opcodes.items():
            G.add_node(cnode.bid)
            n = G.get_node(cnode.bid)
            s = ""
            if len(cnode.ins) > 0:
                for node in cnode.ins:
                    ## Mark NODE that is troublesome
                    if not benign and cnode.isTarget and node.nid == self.target_offset:
                        t = "%d: %s <-- \n" % (node.nid, node.i.opname)
                    else:
                        t = "%d: %s\n" % (node.nid, node.i.opname)
                    s = s + t
                ## Mark node if starting node
                if not benign and cnode.isTarget and nid == self.target_offset:
                    n.attr['label'] = "%d: %s  <--\n%s" % (nid, cnode.i.opname, s)
                else:
                    n.attr['label'] = "%d: %s \n%s" % (nid, cnode.i.opname, s)
            else:
                ## Mark node if only starting node
                if not benign and cnode.isTarget and nid == self.target_offset:
                    n.attr['label'] = "%d: %s  <--" % (nid, cnode.i.opname)
                else:
                    n.attr['label'] = "%d: %s" % (nid, cnode.i.opname)        
                # n.attr['label'] = "%d: %s" % (nid, cnode.i.opname)
            n.attr["shape"] = "box"
            if not benign and cnode.isTarget:
                n.attr['style'] = "filled"
                n.attr['color'] = "lightcoral"
            for cn in cnode.children:
                G.add_edge(cnode.bid, cn.bid)
        return G


def make_graph(filename, fn_names, offsets, types, file_solution = None):
    # print(filename, fn_names, offsets, types )
    codeobjs = []
    fnnames = [] 
    #fnnames, codeobjs = readpyc.read_file( "pyc-cfg.cpython-36.pyc");
    fnnames, codeobjs = readpyc.read_file( filename ) #"TOP_40/1.pyc");
    for i in range(len(fnnames)):
        fn = fnnames[i];
        fn = fn.replace("\n", "")
        fn = fn.replace("\r", "")
        fn = fn.replace(" ", "")
        fn = fn.replace("*", "_")
        if fn not in fn_names: # Ignore any not causing error
            continue
        if len(fn) > 20:
            fn = fn[0:19]            
        print ('Processing: ', fn)
        
        
        #if fnnames[i] == "gcd":
        v = CFG(codeobjs[i], offsets[fn_names.index(fn)]);    
        g = v.to_graph()   
        g.draw('output/cfg/'+fn + '.out.png', prog='dot')

        print ('2CFG generated: ', fnnames[i] + '.out.png')
    if file_solution == None: return
    codeobjs = []
    fnnames = [] 
    #fnnames, codeobjs = readpyc.read_file( "pyc-cfg.cpython-36.pyc");
    fnnames, codeobjs = readpyc.read_file( file_solution ) #"TOP_40/1.pyc");
    for i in range(len(fnnames)):
        fn = fnnames[i];
        fn = fn.replace("\n", "")
        fn = fn.replace("\r", "")
        fn = fn.replace(" ", "")
        fn = fn.replace("*", "_")
        if fn not in fn_names: # Ignore any not causing error
            continue
        if len(fn) > 20:
            fn = fn[0:19]            
        print ('Processing: ', fn)
        
        
        #if fnnames[i] == "gcd":
        v = CFG(codeobjs[i], offsets[fn_names.index(fn)]);    
        g = v.to_graph(True)   
        g.draw('output/cfg/'+fn + '.sol.out.png', prog='dot')

        print ('1CFG generated: ', fnnames[i] + '.soln.out.png')

    

def main(argv):
    #print (argv[0])
    codeobjs = []
    fnnames = [] 
    #fnnames, codeobjs = readpyc.read_file( "pyc-cfg.cpython-36.pyc");
    fnnames, codeobjs = readpyc.read_file( argv[0] ) #"TOP_40/1.pyc");
    print("fnames:", fnnames)
    for i in range(len(fnnames)):
        fn = fnnames[i];
        fn = fn.replace("\n", "")
        fn = fn.replace("\r", "")
        fn = fn.replace(" ", "")
        fn = fn.replace("*", "_")
        if len(fn) > 20:
            fn = fn[0:19]            
        print ('Processing: ', fn)
        
        
        #if fnnames[i] == "gcd":
        v = CFG(codeobjs[i], -1);    
        g = v.to_graph()   
        g.draw('output/cfg/'+ fn + '.out.png', prog='dot')
        print ('CFG generated: ', fn + '.out.png')
        
        #dis.disassemble(codeobjs[i])
    

if __name__ == '__main__':
    main(sys.argv[1:])
    