find . -maxdepth 1 -type d \( ! -name . \) -exec bash -c "cd '{}' && pwd | cut -d '-' -f 2 | xargs -I {} docker buildx  build --platform linux/amd64 --tag {} ." \;