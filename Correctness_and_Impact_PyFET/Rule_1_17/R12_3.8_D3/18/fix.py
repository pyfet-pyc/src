"""distutils._msvccompiler

Contains MSVCCompiler, an implementation of the abstract CCompiler class
for Microsoft Visual Studio 2015.

The module is compatible with VS 2015 and later. You can find legacy support
for older versions in distutils.msvc9compiler and distutils.msvccompiler.
"""

# Written by Perry Stoll
# hacked by Robin Becker and Thomas Heller to do a better job of
#   finding DevStudio (through the registry)
# ported to VS 2005 and VS 2008 by Christian Heimes
# ported to VS 2015 by Steve Dower

import os
import subprocess
import winreg

from distutils.errors import (
    DistutilsExecError as distee
    )
from distutils.errors import (
    DistutilsPlatformError as distpe
    )
from distutils.errors import (
    CompileError as compe
    )
from distutils.errors import (
    LibError as libe
    )
from distutils.errors import (
    LinkError as lnke
    )    
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
    root = os.environ.get("ProgramFiles(x86)") or os.environ.get("ProgramFiles")
    if not root:
        return None, None

    try:
        path = subprocess.check_output([
            os.path.join(root, "Microsoft Visual Studio", "Installer", "vswhere.exe"),
            "-latest",
            "-prerelease",
            "-requires", "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
            "-property", "installationPath",
            "-products", "*",
        ], encoding="mbcs", errors="strict").strip()
    except (subprocess.CalledProcessError, OSError, UnicodeDecodeError):
        return None, None

    path = os.path.join(path, "VC", "Auxiliary", "Build")
    if os.path.isdir(path):
        return 15, path

    return None, None