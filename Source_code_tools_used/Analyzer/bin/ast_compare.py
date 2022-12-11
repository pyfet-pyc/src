import ast, types
from itertools import count
import astunparse

cfg_nodes = [ast.If, ast.For,  ast.While, ast.Break, ast.Continue, ast.Try, ast.ExceptHandler, ast.With]
def get_ast(f):
    return ast.parse(open(f).read())

def get_functions_from_ast(i_ast):
    func_nodes =[]
    for node in i_ast.body:
        if isinstance(node, ast.FunctionDef):
            func_nodes.append(node)
            # print(node.name)
    # print(len(func_nodes))
    return func_nodes

def get_control_flow_counts(tree):
    counter = {}
    print([x for x in ast.walk(tree) if isinstance(x, ast.If)])
    try:
        counter['if'] = len([x for x in ast.walk(tree) if isinstance(x, ast.If)])
    except:
        pass#counter['if'] = 0
    try:
        counter['else'] = len([x for x in ast.walk(tree) if isinstance(x, ast.If) and len(x.orelse)>0])
    except:
        pass#counter['else'] = 0
    try:
        counter['for'] = len([x for x in ast.walk(tree) if isinstance(x, ast.For)])
    except:
        pass#counter['for'] = 0
    try:
        counter['while'] = len([x for x in ast.walk(tree) if isinstance(x, ast.While)])
    except:
        pass#counter['while'] = 0
    try:
        counter['break'] = len([x for x in ast.walk(tree) if isinstance(x, ast.Break)])
    except:
        pass#counter['break'] = 0
    try:
        counter['Continue'] = len([x for x in ast.walk(tree) if isinstance(x, ast.Continue)])
    except:
        pass#counter['Continue'] = 0
    try:
        counter['Try'] = len([x for x in ast.walk(tree) if isinstance(x, ast.Try)])
    except:
        pass#counter['Try'] = 0
    try:
        counter['ExceptHandler'] = len([x for x in ast.walk(tree) if isinstance(x, ast.ExceptHandler)])
    except:
        pass#counter['ExceptHandler'] = 0
    try:
        counter['With'] = len([x for x in ast.walk(tree) if isinstance(x, ast.With)])
    except:
        pass#counter['With'] = 0
    print('ast if',counter)

def compare_two_ast(ast_1, ast_2):
    func_nodes_1 = get_functions_from_ast(ast_1)
    func_nodes_2 = get_functions_from_ast(ast_2)
    for node_1 in func_nodes_1:
        for node_2 in func_nodes_2:
            if node_1.name != node_2.name: continue
            # Got same node
            # ast.dump(node_1)
            # ast.dump(node_2)
            # get_control_flow_counts(node_1)
            # get_control_flow_counts(node_2)
            print(ast.iter_child_nodes(node_1))
            print(ast.iter_child_nodes(node_2))
            tree2 = ast.iter_child_nodes(node_2.body)
            for c1 in ast.iter_child_nodes(node_1.body):
                print(c1)

            # code1 = astunparse.unparse(node_1)
            # code2 = astunparse.unparse(node_2)
            break
        break
        

print(ast.dump(ast.parse("""
if a:
    return
elif b:
    return
else:
    return

if c:
    return
else:
    if d:
            return
""")))        
    

# test_files = ['test.py', 'test.d.py']

# ast1 = get_ast(test_files[0])
# ast2 = get_ast(test_files[1])

# print(type(ast1))

# print(get_functions_from_ast(ast1))
# print(get_functions_from_ast(ast2))

# compare_two_ast(ast1, ast2)
# print(ast.dump(ast1))