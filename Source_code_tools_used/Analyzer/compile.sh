python -m compileall -b samples/target_py/main.py # python 3+
# python -m compileall main.py # python 2
python bin/dis_code_s.py samples/target_py/main.py > output/dis_output/main.dis
mv samples/target_py/main.pyc samples/test/
# python -m compileall solution.py # python 2
# python -m compileall -b samples/target_py/solution.py # python 3+
# python bin/dis_code_s.py samples/target_py/solution.py > output/dis_output/solution.dis
# mv samples/target_py/solution.pyc samples/test/

source create-cfg.sh samples/test/main.pyc