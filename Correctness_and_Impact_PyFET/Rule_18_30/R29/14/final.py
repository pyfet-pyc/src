# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:01:48
# Size of source mod 2**32: 638 bytes
"""
Convert the conda environment.yml to the pip requirements-dev.txt,
or check that they have the same packages (for the CI)

Usage:

    Generate `requirements-dev.txt`
    $ python scripts/generate_pip_deps_from_conda.py

    Compare and fail (exit status != 0) if `requirements-dev.txt` has not been
    generated with this script:
    $ python scripts/generate_pip_deps_from_conda.py --compare
"""
import argparse, pathlib, re, sys, toml, yaml
EXCLUDE = {
 'python', 'c-compiler', 'cxx-compiler'}
RENAME = {'pytables':'tables',  'geopandas-base':'geopandas',  'pytorch':'torch'}
# okay decompiling testbed_py/test.py
