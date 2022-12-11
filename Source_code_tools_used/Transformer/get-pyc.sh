
python -m compileall $1 

for f in $(dirname $1)/__pycache__/*; do
  s=$1
  mv "$(dirname $1)/__pycache__/$(basename $f)" "$(dirname $1)/$(basename ${s%.*}).pyc"
done;

rmdir "$(dirname $1)/__pycache__"

echo "Created: $(dirname $1)/$(basename ${s%.*}).pyc"
# https://stackoverflow.com/questions/2664740/extract-file-basename-without-path-and-extension-in-bash

