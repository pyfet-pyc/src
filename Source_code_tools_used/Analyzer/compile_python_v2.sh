# python -m compileall -b main.py # python 3+
python -m compileall samples/target_py/main.py # python 2
python bin/dis_code_s.py > output/dis_output/main.dis
mv samples/target_py/main.pyc samples/test/

python -m compileall samples/target_py/solution.py # python 2
python bin/dis_code_s.py > output/dis_output/solution.dis
mv samples/target_py/solution.pyc samples/test/
# source reverse.sh