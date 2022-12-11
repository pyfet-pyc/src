for f in test/*.pyc; do
    python run_decompyle3_only.py $f >> d3_time.log # python 3+
done;