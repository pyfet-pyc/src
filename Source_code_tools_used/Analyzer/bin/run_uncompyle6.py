import uncompyle6
import sys
sys.path.insert(0, './lib')
sys.path.insert(0, './bin')
import pyccfg
from pyccfg import *
f = open('temp.txt', 'w+')
should_process = True
new_stdout = f

try:
    filename = sys.argv[1]
except:
    print("Please pass file as an argument")
    exit()
try:
    file_solution = sys.argv[2]
except:
    file_solution = None

if file_solution == 'False':
    should_process = False # Change this to make cfg


def parse_errors():
    f.flush()
    with open('temp.txt', 'r') as file:
        text = file.read()
    # f = open('temp.txt', 'r').seek(0)
    # text = f.read()
    print(text)
    err = [
        x for x in text.split('\n') 
        if "Parse error at or near" in x or "--- This code section failed: ---" in x
    ]
    funcs = [x for idx, x in enumerate(err) if idx % 2 == 0]
    funcs = [x.split(' ')[1][:-3] for x in funcs]
    
    offsets = [int(x.split(' ')[-1]) for idx, x in enumerate(err) if idx % 2 == 1]
    types = [x.split('`')[-1].split("'")[0] for idx, x in enumerate(err) if idx % 2 == 1]
    
    return funcs, offsets, types

try:
    uncompyle6.decompile_file(filename, f)
    # f.close()
    if not should_process:
        print(filename, "Passed")
        exit()
    print("Uncompyle Successful.")
    exit()
except uncompyle6.semantics.pysource.SourceWalkerError as e:
    # print("Parse error:", e)
    if not should_process:
        print(filename, "Failed")
    f, offsets, types =parse_errors()
    print(f, offsets, types)
    make_graph(filename, f, offsets, types, file_solution)
    # print ("functions:", f)
    # print ("offset:", offsets)
    # print ("instruction:", types)
    
    # Extract offset from here
except Exception as e:
    print("New error:")
    print("exception:", e)
    print("exception type:", type(e))
    print("exception args:", e.args)
    # print("exception cause:", e.__cause__)
    # print("exception class:", e.__class__)
    exit()
    
    
