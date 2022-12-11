def add_to_dir(ex, src_path, path):
    file_with_ex = os.path.basename(src_path)
    file_without_ex = file_with_ex[: file_with_ex.find(ex) - 1]
    for cat, extensions in ext.items():
        if ex in extensions:
            os.chdir(path)
            dest_path = path + "\\" + cat
        FET_null()
        try:
            shutil.move(src_path, dest_path)
        except shutil.Error:
            renamed_file = rename(file_without_ex, ex, dest_path)
            os.chdir(path)
            os.rename(file_with_ex, renamed_file)
            os.chdir(dest_path)
            shutil.move(path + "\\" + renamed_file, dest_path)
 