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
        # OSX before 10.4.0, these don't support -arch and -isysroot at
        # all.
        stripArch = stripSysroot = True

    while True:
        try:
            index = compiler_so.index('-arch')
            # Strip this argument and the next one:
            del compiler_so[index:index+2]
        except ValueError:
            break
                
    return

def foo():
    sysroot = None
    argvar = cc_args