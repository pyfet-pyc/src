# Batch compilation
# for f in test_py_3.7/*.py; do
#     python -m compileall -b $f # python 3+
# done;

# Check decompilation in batch:
# for f in test_py_3.7/*.pyc; do
#     python run_uncompyle6.py $f False # python 3+
# done;

# Check if target function detected
# for f in test_py_3.7/*.pyc; do
#     python check_target_func_in_pyc.py $f target_FUNC_ANNOTATED # python 3+
# done;

# Append
# for f in test_py_3.7/*.pyc; do
#     filename="$(basename $f)"
#     python instrument_pyc_at_offset.py $f pre-pend_3.7/$filename target_FUNC_ANNOTATED 0 # python 3+
# done;

# Check decompilation in batch:
# for f in pre-pend_3.7/*.pyc; do
#     python run_uncompyle6.py $f False # python 3+
# done;

# for f in pre-pend_3.7/*.pyc; do
#     filename="$(basename $f)"
#     name="${filename%.*}"
#     cp ../decompiler-experiment/Error_1/$name/$filename test_err_pyc_3.7/ # python 3+
# done;
echo "====U6======" >> all_blocks.log
for f in samples/u6_pyinstaller_3.9_modified/*.pyc; do
    filename="$(basename $f)"
    name="${filename%.*}"
    echo "$name"
    python bin/convert_into_3_8.py $f some_outputs/
done;
echo "====D3======" >> all_blocks.log
for f in samples/d3_pyinstaller_3.9_modified/*.pyc; do
    filename="$(basename $f)"
    name="${filename%.*}"
    echo "$name"
    python bin/convert_into_3_8.py $f some_outputs_d3/
done;

# # python -m compileall main.py # python 2
# python scripts/dis_code.py target_py/main.py > dis_output/main.dis
# mv target_py/main.pyc test/
# python -m compileall -b target_py/solution.py # python 3+
# # python -m compileall solution.py # python 2
# python scripts/dis_code.py target_py/solution.py > dis_output/solution.dis
# mv target_py/solution.pyc test/