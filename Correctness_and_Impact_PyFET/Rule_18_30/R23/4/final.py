# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/buildserver.py
# Compiled at: 2022-08-12 04:23:33
# Size of source mod 2**32: 1687 bytes
Instruction context:
   
 L.  34       240  LOAD_FAST                'srv'
                 242  LOAD_CLOSURE             'thr'
                 244  BUILD_TUPLE_1         1 
->               246  LOAD_DICTCOMP            '<code_object <dictcomp>>'
                 248  LOAD_STR                 'main.<locals>.<dictcomp>'
                 250  MAKE_FUNCTION_8          'closure'
                 252  LOAD_GLOBAL              action
                 254  GET_ITER         
                 256  CALL_FUNCTION_1       1  ''
                 258  BUILD_MAP_UNPACK_2     2 
                 260  STORE_FAST               'compat_input'


def main--- This code section failed: ---

 L.   2         0  LOAD_GLOBAL              argparse
                2  LOAD_METHOD              ArgumentParser
                4  CALL_METHOD_0         0  ''
                6  STORE_FAST               'parser'

 L.   3         8  LOAD_FAST                'parser'
               10  LOAD_ATTR                add_argument
               12  LOAD_STR                 '-i'
               14  LOAD_STR                 '--install'

 L.   4        16  LOAD_STR                 'store_const'

 L.   4        18  LOAD_STR                 'action'

 L.   4        20  LOAD_STR                 'install'

 L.   5        22  LOAD_STR                 'Launch at Windows startup'

 L.   3        24  LOAD_CONST               ('action', 'dest', 'const', 'help')
               26  CALL_FUNCTION_KW_6     6  '6 total positional and keyword args'
               28  POP_TOP          

 L.   6        30  LOAD_FAST                'parser'
               32  LOAD_ATTR                add_argument
               34  LOAD_STR                 '-u'
               36  LOAD_STR                 '--uninstall'

 L.   7        38  LOAD_STR                 'store_const'

 L.   7        40  LOAD_STR                 'action'

 L.   7        42  LOAD_STR                 'uninstall'

 L.   8        44  LOAD_STR                 'Remove Windows service'

 L.   6        46  LOAD_CONST               ('action', 'dest', 'const', 'help')
               48  CALL_FUNCTION_KW_6     6  '6 total positional and keyword args'
               50  POP_TOP          

 L.   9        52  LOAD_FAST                'parser'
               54  LOAD_ATTR                add_argument
               56  LOAD_STR                 '-s'
               58  LOAD_STR                 '--service'

 L.  10        60  LOAD_STR                 'store_const'

 L.  10        62  LOAD_STR                 'action'

 L.  10        64  LOAD_STR                 'service'

 L.  11        66  LOAD_STR                 'Run as a Windows service'

 L.   9        68  LOAD_CONST               ('action', 'dest', 'const', 'help')
               70  CALL_FUNCTION_KW_6     6  '6 total positional and keyword args'
               72  POP_TOP          

 L.  12        74  LOAD_FAST                'parser'
               76  LOAD_ATTR                add_argument
               78  LOAD_STR                 '-b'
               80  LOAD_STR                 '--bind'
               82  LOAD_STR                 '<host:port>'

 L.  13        84  LOAD_STR                 'store'

 L.  13        86  LOAD_STR                 '0.0.0.0:8142'

 L.  14        88  LOAD_STR                 'Bind to host:port (default %default)'

 L.  12        90  LOAD_CONST               ('metavar', 'action', 'default', 'help')
               92  CALL_FUNCTION_KW_6     6  '6 total positional and keyword args'
               94  POP_TOP          

 L.  15        96  LOAD_FAST                'parser'
               98  LOAD_ATTR                parse_args
              100  LOAD_FAST                'args'
              102  LOAD_CONST               ('args',)
              104  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              106  STORE_FAST               'options'

 L.  17       108  LOAD_FAST                'options'
              110  LOAD_ATTR                action
              112  LOAD_STR                 'install'
              114  COMPARE_OP               ==
              116  POP_JUMP_IF_FALSE   170  'to 170'

 L.  18       118  LOAD_GLOBAL              os
              120  LOAD_ATTR                path
              122  LOAD_METHOD              abspath
              124  LOAD_GLOBAL              __file__
              126  CALL_METHOD_1         1  ''
              128  LOAD_METHOD              replace
              130  LOAD_STR                 'v:'
              132  LOAD_STR                 '\\\\vboxsrv\\vbox'
              134  CALL_METHOD_2         2  ''
              136  STORE_FAST               'fn'

 L.  19       138  LOAD_STR                 '%s %s -s -b %s'
              140  LOAD_GLOBAL              sys
              142  LOAD_ATTR                executable
              144  LOAD_FAST                'fn'
              146  LOAD_FAST                'options'
              148  LOAD_ATTR                bind
              150  BUILD_TUPLE_3         3 
              152  BINARY_MODULO    
              154  STORE_FAST               'cmdline'

 L.  20       156  LOAD_GLOBAL              win_install_service
              158  LOAD_GLOBAL              SVCNAME
              160  LOAD_FAST                'cmdline'
              162  CALL_FUNCTION_2       2  ''
              164  POP_TOP          

 L.  21       166  LOAD_CONST               None
              168  RETURN_VALUE     
            170_0  COME_FROM           116  '116'

 L.  23       170  LOAD_FAST                'options'
              172  LOAD_ATTR                action
              174  LOAD_STR                 'uninstall'
              176  COMPARE_OP               ==
              178  POP_JUMP_IF_FALSE   192  'to 192'

 L.  24       180  LOAD_GLOBAL              win_uninstall_service
              182  LOAD_GLOBAL              SVCNAME
              184  CALL_FUNCTION_1       1  ''
              186  POP_TOP          

 L.  25       188  LOAD_CONST               None
              190  RETURN_VALUE     
            192_0  COME_FROM           178  '178'

 L.  27       192  LOAD_FAST                'options'
              194  LOAD_ATTR                action
              196  LOAD_STR                 'service'
              198  COMPARE_OP               ==
              200  POP_JUMP_IF_FALSE   216  'to 216'

 L.  28       202  LOAD_GLOBAL              win_service_start
              204  LOAD_GLOBAL              SVCNAME
              206  LOAD_GLOBAL              main
              208  CALL_FUNCTION_2       2  ''
              210  POP_TOP          

 L.  29       212  LOAD_CONST               None
              214  RETURN_VALUE     
            216_0  COME_FROM           200  '200'

 L.  31       216  LOAD_FAST                'options'
              218  LOAD_ATTR                bind
              220  LOAD_METHOD              split
              222  LOAD_STR                 ':'
              224  CALL_METHOD_1         1  ''
              226  UNPACK_SEQUENCE_2     2 
              228  STORE_FAST               'host'
              230  STORE_FAST               'port_str'

 L.  32       232  LOAD_GLOBAL              int
              234  LOAD_FAST                'port_str'
              236  CALL_FUNCTION_1       1  ''
              238  STORE_FAST               'port'

 L.  34       240  LOAD_FAST                'srv'
              242  LOAD_CLOSURE             'thr'
              244  BUILD_TUPLE_1         1 
              246  LOAD_DICTCOMP            '<code_object <dictcomp>>'
              248  LOAD_STR                 'main.<locals>.<dictcomp>'
              250  MAKE_FUNCTION_8          'closure'
              252  LOAD_GLOBAL              action
              254  GET_ITER         
              256  CALL_FUNCTION_1       1  ''
              258  BUILD_MAP_UNPACK_2     2 
              260  STORE_FAST               'compat_input'

 L.  36       262  LOAD_GLOBAL              print
              264  LOAD_STR                 'Listening on %s:%d'
              266  LOAD_FAST                'host'
              268  LOAD_FAST                'port'
              270  BUILD_TUPLE_2         2 
              272  BINARY_MODULO    
              274  CALL_FUNCTION_1       1  ''
              276  POP_TOP          

 L.  37       278  LOAD_GLOBAL              BuildHTTPServer
              280  LOAD_FAST                'host'
              282  LOAD_FAST                'port'
              284  BUILD_TUPLE_2         2 
              286  LOAD_GLOBAL              BuildHTTPRequestHandler
              288  CALL_FUNCTION_2       2  ''
              290  STORE_FAST               'srv'

 L.  38       292  LOAD_GLOBAL              threading
              294  LOAD_ATTR                Thread
              296  LOAD_FAST                'srv'
              298  LOAD_ATTR                serve_forever
              300  LOAD_CONST               ('target',)
              302  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              304  STORE_DEREF              'thr'

 L.  39       306  LOAD_DEREF               'thr'
              308  LOAD_METHOD              start
              310  CALL_METHOD_0         0  ''
              312  POP_TOP          

 L.  40       314  LOAD_FAST                'compat_input'
              316  LOAD_STR                 'Press ENTER to shut down'
              318  CALL_FUNCTION_1       1  ''
              320  POP_TOP          

 L.  41       322  LOAD_FAST                'srv'
              324  LOAD_METHOD              shutdown
              326  CALL_METHOD_0         0  ''
              328  POP_TOP          

 L.  42       330  LOAD_DEREF               'thr'
              332  LOAD_METHOD              join
              334  CALL_METHOD_0         0  ''
              336  POP_TOP          

Parse error at or near `LOAD_DICTCOMP' instruction at offset 246
