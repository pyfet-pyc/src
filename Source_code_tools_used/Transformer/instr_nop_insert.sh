 #!/bin/bash
 if [ "$#" -eq  "3" ]
   then
     python bin/instr_at_offset.py "$1" "$1.instr.pyc" "$2" "$3"
 else
     echo "instr_nop_test.sh [input-pyc] [function-name] [offset]"
     echo  "example: ./instr_nop_insert.sh samples/mwe/1.pyc get_file_input 12"
 fi

