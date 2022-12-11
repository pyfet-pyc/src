for f in test/*.pyc; do
    python run_uncompyle6_only.py $f >> u6_time.log # python 3+
done;