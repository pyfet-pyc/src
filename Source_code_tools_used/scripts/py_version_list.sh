for f in ../to_check/pyinstaller/malware6/*.pyc; do
    python3 header_recover.py $f
done;
