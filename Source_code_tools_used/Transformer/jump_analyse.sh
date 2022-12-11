 #!/bin/bash
 if [ "$#" -eq  "3" ]
   then
     python bin/convert_jumps.py "$1" "$2" "$3"
 else
     echo "jump_analyse.sh [input-pyc] [output-pyc directory] [function-name]"
     echo  "example: ./jump_analyse.sh samples/mwe/1.pyc output/test_output_pyc/ get_file_input"
 fi

