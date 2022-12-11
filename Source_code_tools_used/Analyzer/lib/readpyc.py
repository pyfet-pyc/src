# ================================================================
# ================================================================
# ================================================================
import binascii
import dis
import marshal
import sys, os
import time
import types
import uncompyle6

class CodeObjNames:
    def __init__(self):
        self.funcname = []
        self.codeobj = []
    


def get_long(s):
    return s[0] + (s[1] << 8) + (s[2] << 16) + (s[3] << 24)


def show_hex(label, h, indent):
    h = binascii.hexlify(h).decode('ascii')
    if len(h) < 60:
        print('%s%s %s' % (indent, label, h))
    else:
        print('%s%s' % (indent, label))
        for i in range(0, len(h), 60):
            print('%s   %s' % (indent, h[i:i+60]))

def read_code(code, coret, fnname=''):
    # print("name:", code.co_name, code)
    #print('%scode' % indent)
    #indent += '   '
    #print('%sargcount %d' % (indent, code.co_argcount))
    #print('%snlocals %d' % (indent, code.co_nlocals))
    #print('%sstacksize %d' % (indent, code.co_stacksize))
    #print('%sflags %04x' % (indent, code.co_flags))
    #show_hex('code', code.co_code, indent=indent)
    #dis.disassemble(code)

    if( fnname == None ):
        fnname = "None"

    coret.funcname.append( code.co_name );
    coret.codeobj.append( code );
    #v = CFG(code);    
    #g = v.to_graph()   
    #g.draw(fnname + '.out.png', prog='dot')
    
    #dis.disassemble(code)
    func_name = ""
    #print('%sconsts' % indent)
    # print("co_consts", code.co_consts)
    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            # print("codetype:",const)
            read_code(const, coret, func_name)
        else:
            # print("funcname:", const)
            func_name = "{0}".format(const)
            #print('-   %s%r' % (indent, const))
    #print('%snames %r' % (indent, code.co_names))
    #print('%svarnames %r' % (indent, code.co_varnames))
    #print('%sfreevars %r' % (indent, code.co_freevars))
    #print('%scellvars %r' % (indent, code.co_cellvars))
    #print('%sfilename %r' % (indent, code.co_filename))
    #print('%sname %r' % (indent, code.co_name))
    #print('%sfirstlineno %d' % (indent, code.co_firstlineno))
    #show_hex('lnotab', code.co_lnotab, indent=indent)


def read_file(fname):
    with open(fname, 'rb') as f:
        # magic_str = f.read(4)
        # mtime_str = f.read(4)
        # mtime = get_long(mtime_str)
        # modtime = time.asctime(time.localtime(mtime))
        # # print('magic %s' % binascii.hexlify(magic_str))
        # # print('moddate %s (%s)' % (binascii.hexlify(mtime_str), modtime))
        # if sys.version_info < (3, 3):
        #     print('source_size: (unknown)')
        #     pass
        # else:
        #     source_size = f.read(4)
        #     # print('source_size: %s' % binascii.hexlify(source_size))
        # if sys.version_info > (3, 6):
        #     f.read(4)    
        ret = CodeObjNames()
        f.seek(8) 
        try: 
            read_code(marshal.load(f), ret)          # rest is a marshalled code object
        except: 
            try:
                f.seek(12)
                read_code(marshal.load(f), ret)
            except:
                f.seek(16)
                read_code(marshal.load(f), ret)
        return ret.funcname, ret.codeobj

def read_file_get_object(fname):
    with open(fname, 'rb') as f:
        ret = CodeObjNames()
        f.seek(8) 
        try: 
            co = marshal.load(f)   # rest is a marshalled code object
            if isinstance(co, types.CodeType):
                return co
            raise "Code Object not found" 
        except: 
            try:
                f.seek(12)
                co = marshal.load(f)
                if isinstance(co, types.CodeType):
                    return co
                raise "Code Object not found"
            except:
                f.seek(16)
                co = marshal.load(f)
                if isinstance(co, types.CodeType):
                    return co
                raise "Code Object not found"


def write_file(original_file, target_file, co):
    header = 0
    header_data = None  
    if co == None: return
    with open(original_file, 'rb') as f:   
        f.seek(8) 
        try: 
            header = 8
            co_temp = marshal.load(f)          # rest is a marshalled code object
            if not isinstance(co_temp, types.CodeType):
                raise "Code Object not found"
        except: 
            try:
                header = 12
                f.seek(12)
                co_temp = marshal.load(f)
                if not isinstance(co_temp, types.CodeType):
                    raise "Code Object not found"
            except:
                header = 16
                f.seek(16)
                co_temp = marshal.load(f)
                if not isinstance(co_temp, types.CodeType):
                    raise "Code Object not found"
        f.seek(0)
        header_data = f.read(header)
    if header_data is None:
        raise "Failed reading header"
    with open(target_file, 'wb') as fp:
        # Copy header data
        fp.write(header_data)
        # Dump co
        # print("---------------")
        # dis.dis(co_temp)
        # print("---------------")
        # dis.dis(co)
        
        fp.write(marshal.dumps(co))
    return

def check_uncompyle6_on_co(original_file, co):
    f = open("tmp/read_pyc.log", 'w')
    stdout = sys.stdout
    sys.stdout = f # Silence output
    write_file(original_file, "tmp/temp.pyc", co)
    sys.stdout = stdout
    try:
        uncompyle6.decompile_file("tmp/temp.pyc", f)
        return True
    except Exception as x:
        print(x)
        return False

# ================================================================
# ================================================================
# ================================================================
