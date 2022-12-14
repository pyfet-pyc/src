import struct
import os
import sys
# These constants are from Python-3.x.x/Lib/importlib/_bootstrap_external.py
PYTHON_MAGIC = {
    # Python 1
    20121: (1, 5),
    50428: (1, 6),

    # Python 2
    50823: (2, 0),
    60202: (2, 1),
    60717: (2, 2),
    62011: (2, 3),  # a0
    62021: (2, 3),  # a0
    62041: (2, 4),  # a0
    62051: (2, 4),  # a3
    62061: (2, 4),  # b1
    62071: (2, 5),  # a0
    62081: (2, 5),  # a0
    62091: (2, 5),  # a0
    62092: (2, 5),  # a0
    62101: (2, 5),  # b3
    62111: (2, 5),  # b3
    62121: (2, 5),  # c1
    62131: (2, 5),  # c2
    62151: (2, 6),  # a0
    62161: (2, 6),  # a1
    62171: (2, 7),  # a0
    62181: (2, 7),  # a0
    62191: (2, 7),  # a0
    62201: (2, 7),  # a0
    62211: (2, 7),  # a0

    # Python 3
    3000: (3, 0),
    3010: (3, 0),
    3020: (3, 0),
    3030: (3, 0),
    3040: (3, 0),
    3050: (3, 0),
    3060: (3, 0),
    3061: (3, 0),
    3071: (3, 0),
    3081: (3, 0),
    3091: (3, 0),
    3101: (3, 0),
    3103: (3, 0),
    3111: (3, 0),  # a4
    3131: (3, 0),  # a5

    # Python 3.1
    3141: (3, 1),  # a0
    3151: (3, 1),  # a0

    # Python 3.2
    3160: (3, 2),  # a0
    3170: (3, 2),  # a1
    3180: (3, 2),  # a2

    # Python 3.3
    3190: (3, 3),  # a0
    3200: (3, 3),  # a0
    3220: (3, 3),  # a1
    3230: (3, 3),  # a4

    # Python 3.4
    3250: (3, 4),  # a1
    3260: (3, 4),  # a1
    3270: (3, 4),  # a1
    3280: (3, 4),  # a1
    3290: (3, 4),  # a4
    3300: (3, 4),  # a4
    3310: (3, 4),  # rc2

    # Python 3.5
    3320: (3, 5),  # a0
    3330: (3, 5),  # b1
    3340: (3, 5),  # b2
    3350: (3, 5),  # b2
    3351: (3, 5),  # 3.5.2

    # Python 3.6
    3360: (3, 6),  # a0
    3361: (3, 6),  # a0
    3370: (3, 6),  # a1
    3371: (3, 6),  # a1
    3372: (3, 6),  # a1
    3373: (3, 6),  # b1
    3375: (3, 6),  # b1
    3376: (3, 6),  # b1
    3377: (3, 6),  # b1
    3378: (3, 6),  # b2
    3379: (3, 6),  # rc1

    # Python 3.7
    3390: (3, 7),  # a1
    3391: (3, 7),  # a2
    3392: (3, 7),  # a4
    3393: (3, 7),  # b1
    3394: (3, 7),  # b5

    # Python 3.8
    3400: (3, 8),  # a1
    3401: (3, 8),  # a1
    3410: (3, 8),  # a1
    3411: (3, 8),  # b2
    3412: (3, 8),  # b2
    3413: (3, 8),  # b4

    # Python 3.9
    3420: (3, 9),  # a0
    3421: (3, 9),  # a0
    3422: (3, 9),  # a0
    3423: (3, 9),  # a2
    3424: (3, 9),  # a2
    3425: (3, 9),  # a2
}

# Python 2.7: [magic_num][source_modified_time]
# Python >= 3.2 (PEP-3147): [magic_num][source_modified_time][source_size]
# Python >= 3.8 (PEP-0552): [magic_num][bit-field][source_modified_time][source_size]

invalid_files = []
file_to_analysis = []
def magic_word_to_version(magic_word):
  """Return the Python version belonging to the magic number in the pyc head.
  The magic number is encoded in the first two bytes of a .pyc file.
  It translates to a (major, minor) version. It never has a "micro" version,
  because Python bytecode encoding doesn't change between micro version.
  Arguments:
    magic_word: A 16 bit number, either as an integer or little-endian encoded
      as a string.
  Returns:
    A tuple (major, minor), e.g. (2, 7).
  """
  if not isinstance(magic_word, int):
    magic_word = struct.unpack("<H", magic_word)[0]
    print(magic_word, end=":")
    try:
        version = PYTHON_MAGIC[magic_word]
        return version
    except:
        return 0


def get_magic_code(filename):
    hash = os.path.basename(filename).split('.')[0]
    print(hash,end=":")
    with open(filename, 'rb') as f:
        magic_word = f.read(2)
    version = magic_word_to_version(magic_word)
    print(version)
    if(version == 0):
        invalid_files.append(filename)



def main(folder_root):
    for current_dir_path, current_subdirs, current_files in os.walk(folder_root):
        for aFile in current_files:
            if aFile.endswith(".pyc") :
                # print(aFile.split('.')[0], end=":")
                pyc_file_path = str(os.path.join(current_dir_path, aFile))
                file_to_analysis.append(pyc_file_path)

    for pyc_file in file_to_analysis:
        get_magic_code(pyc_file)



if __name__ == "__main__":
    # main(sys.argv[1])
    get_magic_code(sys.argv[1])
    # print(invalid_files)