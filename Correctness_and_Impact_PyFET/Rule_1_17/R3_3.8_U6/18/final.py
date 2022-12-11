# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/17/test_fix.py
# Compiled at: 2022-08-17 08:21:24
# Size of source mod 2**32: 949 bytes


def compiler_fixup(compiler_so, cc_args):
    """
    This function will strip '-isysroot PATH' and '-arch ARCH' from the
    compile flags if the user has specified one them in extra_compile_flags.

    This is needed because '-arch ARCH' adds another architecture to the
    build, without a way to remove an architecture. Furthermore GCC will
    barf if multiple '-isysroot' arguments are present.
    """
    stripArch = stripSysroot = False
    compiler_so = list(compiler_so)
    if not _supports_universal_builds():
        stripArch = stripSysroot = True
    while True:
        try:
            index = compiler_so.index('-arch')
            del compiler_so[index:index + 2]
        except ValueError:
            break


def foo():
    sysroot = None
    argvar = cc_args
# okay decompiling R3_3.8_U6/17/test_fix.py
