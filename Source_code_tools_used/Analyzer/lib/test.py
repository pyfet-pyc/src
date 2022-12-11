import readpyc

# This file is for testing lib functions

co = readpyc.read_file_get_object("samples/mwe/0.pyc")
print(readpyc.check_uncompyle6_on_co("samples/mwe/0.pyc", co))