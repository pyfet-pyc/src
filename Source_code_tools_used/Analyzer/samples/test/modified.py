# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.13 (default, Feb 20 2021, 21:42:50) 
# [GCC 5.4.0 20160609]
# Embedded file name: /home/rodream/project/pyc-cfg/pyccfg.py
# Compiled at: 2021-08-11 16:06:58
# Size of source mod 2**32: 11970 bytes
Instruction context:
   
 L.  69        20  LOAD_FAST                'hmap'
                  22  LOAD_FAST                'key'
                  24  BINARY_SUBSCR    
                  26  LOAD_ATTR                append
                  28  LOAD_FAST                'val'
                  30  CALL_FUNCTION_1       1  '1 positional argument'
                  32  POP_TOP          
                34_0  COME_FROM            18  '18'
->                34  LOAD_NAME                append
import sys, dis, pygraphviz, readpyc

class CFGNode:

    def __init__(self, i, bid, isTarget=False):
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
 'LOAD_CONST', 'LOAD_FAST', 'STORE_FAST', 'STORE_NAME', 'LOAD_NAME', 'STORE_ATTR', 'LOAD_ATTR', 'LOAD_GLOBAL', 'STORE_GLOBAL',
 'STORE_SUBSCR', 'STORE_DEREF', 'LOAD_CLOSURE', 'GET_AWAITABLE', 'LOAD_DEREF', 'STORE_ANNOTATION', 'FORMAT_VALUE',
 'COMPARE_OP',
 'INPLACE_ADD', 'INPLACE_SUBTRACT', 'UNPACK_SEQUENCE', 'DELETE_FAST', 'BINARY_ADD', 'BINARY_MODULO', 'BINARY_SUBSCR',
 'BINARY_MULTIPLY', 'BINARY_ADD', 'DELETE_SUBSCR', 'UNARY_NOT', 'LIST_APPEND', 'MAP_ADD', 'SET_ADD', 'BINARY_OR',
 'BINARY_FLOOR_DIVIDE', 'BINARY_SUBTRACT', 'ROT_TWO', 'ROT_THREE', 'DUP_TOP_TWO', 'UNARY_POSITIVE', 'UNARY_NEGATIVE',
 'BINARY_MATRIX_MULTIPLY', 'UNARY_INVERT', 'INPLACE_MATRIX_MULTIPLY', 'BINARY_POWER', 'INPLACE_FLOOR_DIVIDE',
 'MAKE_FUNCTION', 'CALL_FUNCTION', 'CALL_FUNCTION_KW', 'CALL_FUNCTION_EX', 'RETURN_VALUE', 'EXTENDED_ARG',
 'LOAD_BUILD_CLASS',
 'POP_BLOCK', 'POP_TOP', 'DUP_TOP',
 'BUILD_LIST', 'BUILD_MAP', 'BUILD_TUPLE', 'BUILD_CONST_KEY_MAP', 'BUILD_SLICE', 'BUILD_STRING', 'BUILD_SET',
 'FOR_ITER', 'BREAK_LOOP', 'GET_ITER', 'GET_AITER', 'GET_ANEXT', 'CONTINUE_LOOP', 'GET_YIELD_FROM_ITER',
 'END_FINALLY', 'RAISE_VARARGS', 'POP_EXCEPT',
 'IMPORT_FROM', 'IMPORT_NAME', 'IMPORT_STAR',
 'YIELD_FROM', 'YIELD_VALUE', 'SETUP_ANNOTATIONS', 'BEFORE_ASYNC_WITH', 'WITH_CLEANUP_START',
 'WITH_CLEANUP_FINISH',
 '<0>', '<6>', '<7>', '<8>', 'NOP', '<13>', '<18>', '<14>', '<21>', '<30>', '<32>', '<34>', '<36>', '<39>', '<41>',
 '<43>', '<33>']
ops_jumps = [
 'POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'JUMP_IF_TRUE_OR_POP', 'JUMP_IF_FALSE_OR_POP', 'JUMP_ABSOLUTE']
ops_relative_jumps = ['JUMP_FORWARD']
ops_setups = [
 'SETUP_EXCEPT', 'SETUP_FINALLY', 'SETUP_ASYNC_WITH']

class CFG:

    def __init__(self, codeobject, target_offset=-1):

        def lstadd--- This code section failed: ---

 L.  66         0  LOAD_FAST                'key'
                2  LOAD_FAST                'hmap'
                4  COMPARE_OP               not-in
                6  POP_JUMP_IF_FALSE    20  'to 20'

 L.  67         8  LOAD_FAST                'val'
               10  BUILD_LIST_1          1 
               12  LOAD_FAST                'hmap'
               14  LOAD_FAST                'key'
               16  STORE_SUBSCR     
               18  JUMP_FORWARD         34  'to 34'
               20  ELSE                     '34'

 L.  69        20  LOAD_FAST                'hmap'
               22  LOAD_FAST                'key'
               24  BINARY_SUBSCR    
               26  LOAD_ATTR                append
               28  LOAD_FAST                'val'
               30  CALL_FUNCTION_1       1  '1 positional argument'
               32  POP_TOP          
             34_0  COME_FROM            18  '18'
               34  LOAD_NAME                append
               36  LOAD_CONST               None

Parse error at or near `LOAD_NAME' instruction at offset 34

        enter = CFGNode(dis.Instruction('NOP', opcode=(dis.opmap['NOP']), arg=0, argval=0, argrepr=0, offset=0, starts_line=0, is_jump_target=False), 0)
        last = enter
        self.target_offset = target_offset
        self.jump_to = {}
        self.opcodes = {}
        return_nodes = []
        for i, ins in enumerate(dis.get_instructions(codeobject)):
            byte = ins.offset
            node = CFGNode(ins, byte)
            node.nid = byte
            self.opcodes[byte] = node
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
                lstadd(self.jump_to, (i + 1) * 2 + ins.arg, node)
                last.add_child(node)
                last = node
            elif ins.opname == 'SETUP_LOOP':
                last.add_child(node)
                last = node
            elif ins.opname in ops_setups:
                lstadd(self.jump_to, (i + 1) * 2 + ins.arg, node)
                node.props['jmp'] = True
                last.add_child(node)
                last = node
            else:
                print(ins)
                print(ins.opname)
                assert False

        if target_offset == -1:
            self.target_offset = last.bid
            last.isTarget = True
        for byte in self.opcodes:
            if byte in self.jump_to:
                node = self.opcodes[byte]
                assert node.i.is_jump_target
                for b in self.jump_to[byte]:
                    b.add_child(node)

        for rnodes in return_nodes:
            rnodes.children.clear()

        block_nodes = []
        for nid, cnode in self.opcodes.items():
            if len(cnode.children) == 1 and len(cnode.children[0].parent) == 1:
                cnode.block = True
                block_nodes.append(cnode)

        for cnode in block_nodes:
            first_node = cnode
            last_node = cnode
            traversed_node = []
            if cnode.first_node_id == -1:
                while len(last_node.parent) > 0:
                    if first_node.parent[0].block == True:
                        first_node = first_node.parent[0]
                        traversed_node.append(first_node)
                    else:
                        break

                cnode.first_node_id = first_node.nid
            if cnode.last_node_id == -1:
                while len(last_node.children) > 0:
                    if last_node.children[0].block == True:
                        last_node = last_node.children[0]
                        traversed_node.append(last_node)
                    else:
                        break

                cnode.last_node_id = last_node.nid
            for node in traversed_node:
                node.first_node_id = first_node.nid
                node.last_node_id = last_node.nid

        node_to_del = []
        for cnode in block_nodes:
            if cnode.children[0].block == True:
                merging_to = self.opcodes[cnode.first_node_id]
                merged_children = self.opcodes[cnode.last_node_id].children
                node_to_del.append(cnode.children[0].nid)
                merging_to.ins.append(cnode.children[0])
                merging_to.children = merged_children

        for node in node_to_del:
            del self.opcodes[node]

        node_to_del.clear()
        for nid, cnode in self.opcodes.items():
            if len(cnode.children) == 1 and len(cnode.children[0].parent) == 1:
                merging_to = self.opcodes[nid]
                merged_children = self.opcodes[cnode.children[0].nid].children
                node_to_del.append(cnode.children[0].nid)
                merging_to.ins.append(cnode.children[0])
                for n in cnode.children[0].ins:
                    merging_to.ins.append(n)

                merging_to.children = merged_children

        for node in node_to_del:
            del self.opcodes[node]

    def to_graph(self, benign=False):
        G = pygraphviz.AGraph(directed=True)
        for nid, cnode in self.opcodes.items():
            G.add_node(cnode.bid)
            n = G.get_node(cnode.bid)
            s = ''
            if len(cnode.ins) > 0:
                for node in cnode.ins:
                    if not benign:
                        if cnode.isTarget:
                            if node.nid == self.target_offset:
                                t = '%d: %s <-- \n' % (node.nid, node.i.opname)
                    else:
                        t = '%d: %s\n' % (node.nid, node.i.opname)
                    s = s + t

                if not benign:
                    if cnode.isTarget:
                        if nid == self.target_offset:
                            n.attr['label'] = '%d: %s  <--\n%s' % (nid, cnode.i.opname, s)
                n.attr['label'] = '%d: %s \n%s' % (nid, cnode.i.opname, s)
            else:
                if not benign and cnode.isTarget:
                    if nid == self.target_offset:
                        n.attr['label'] = '%d: %s  <--' % (nid, cnode.i.opname)
                    else:
                        n.attr['label'] = '%d: %s' % (nid, cnode.i.opname)
                else:
                    n.attr['shape'] = 'box'
                    if not benign:
                        if cnode.isTarget:
                            n.attr['style'] = 'filled'
                            n.attr['color'] = 'lightcoral'
                for cn in cnode.children:
                    G.add_edge(cnode.bid, cn.bid)

        return G


def make_graph(filename, fn_names, offsets, types, file_solution=None):
    codeobjs = []
    fnnames = []
    fnnames, codeobjs = readpyc.read_file(filename)
    for i in range(len(fnnames)):
        fn = fnnames[i]
        fn = fn.replace('\n', '')
        fn = fn.replace('\r', '')
        fn = fn.replace(' ', '')
        fn = fn.replace('*', '_')
        if fn not in fn_names:
            pass
        else:
            if len(fn) > 20:
                fn = fn[0:19]
            print('Processing: ', fn)
            v = CFG(codeobjs[i], offsets[fn_names.index(fn)])
            g = v.to_graph()
            g.draw(('output_graph/' + fn + '.out.png'), prog='dot')
            print('CFG generated: ', fnnames[i] + '.out.png')

    if file_solution == None:
        return
    codeobjs = []
    fnnames = []
    fnnames, codeobjs = readpyc.read_file(file_solution)
    for i in range(len(fnnames)):
        fn = fnnames[i]
        fn = fn.replace('\n', '')
        fn = fn.replace('\r', '')
        fn = fn.replace(' ', '')
        fn = fn.replace('*', '_')
        if fn not in fn_names:
            pass
        else:
            if len(fn) > 20:
                fn = fn[0:19]
            print('Processing: ', fn)
            v = CFG(codeobjs[i], offsets[fn_names.index(fn)])
            g = v.to_graph(True)
            g.draw(('output_graph/' + fn + '.sol.out.png'), prog='dot')
            print('CFG generated: ', fnnames[i] + '.soln.out.png')


def main(argv):
    codeobjs = []
    fnnames = []
    fnnames, codeobjs = readpyc.read_file(argv[0])
    print('fnames:', fnnames)
    for i in range(len(fnnames)):
        fn = fnnames[i]
        fn = fn.replace('\n', '')
        fn = fn.replace('\r', '')
        fn = fn.replace(' ', '')
        fn = fn.replace('*', '_')
        if len(fn) > 20:
            fn = fn[0:19]
        print('Processing: ', fn)
        v = CFG(codeobjs[i])
        g = v.to_graph()
        g.draw((fn + '.out.png'), prog='dot')
        print('CFG generated: ', fnnames[i] + '.out.png')


if __name__ == '__main__':
    main(sys.argv[1:])
