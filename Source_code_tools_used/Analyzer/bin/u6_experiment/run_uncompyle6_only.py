import uncompyle6, decompyle3
import sys, os, time
from io import StringIO

sys.stdout = open(os.devnull, 'w')
try:
    filename = sys.argv[1]
except:
    print("Please pass file as an argument")
    exit()

start_time = time.time()
try:
    f = StringIO()
    uncompyle6.decompile_file(filename, f)
    # f.close()
except:
    pass
f.flush()
sys.stdout = sys.__stdout__
print("{}:{}:{}".format(filename, os.path.getsize(filename),time.time() - start_time))