# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 23:36:21
# Size of source mod 2**32: 2153 bytes
"""distutils._msvccompiler

Contains MSVCCompiler, an implementation of the abstract CCompiler class
for Microsoft Visual Studio 2015.

The module is compatible with VS 2015 and later. You can find legacy support
for older versions in distutils.msvc9compiler and distutils.msvccompiler.
"""
import os, subprocess, winreg
import distutils.errors as distee
import distutils.errors as distpe
import distutils.errors as compe
import distutils.errors as libe
import distutils.errors as lnke
from distutils.ccompiler import CCompiler, gen_lib_options
from distutils import log
from distutils.util import get_platform
from itertools import count

def _find_vc2017():
    """Returns "15, path" based on the result of invoking vswhere.exe
    If no install is found, returns "None, None"

    The version is returned to avoid unnecessarily changing the function
    result. It may be ignored when the path is not None.

    If vswhere.exe is not available, by definition, VS 2017 is not
    installed.
    """
    root = os.environ.get('ProgramFiles(x86)') or os.environ.get('ProgramFiles')
    if not root:
        return (None, None)
    try:
        path = subprocess.check_output([
         os.path.join(root, 'Microsoft Visual Studio', 'Installer', 'vswhere.exe'),
         '-latest',
         '-prerelease',
         '-requires', 'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
         '-property', 'installationPath',
         '-products', '*'],
          encoding='mbcs',
          errors='strict').strip()
    except (subprocess.CalledProcessError, OSError, UnicodeDecodeError):
        return (None, None)
    else:
        path = os.path.join(path, 'VC', 'Auxiliary', 'Build')
        if os.path.isdir(path):
            return (15, path)
        else:
            return (None, None)
# okay decompiling test.pyc
