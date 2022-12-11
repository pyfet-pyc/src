#!/usr/bin/env python3
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
import argparse
import pathlib
import re
import sys

import toml
import yaml

EXCLUDE = {"python", "c-compiler", "cxx-compiler"}
RENAME = {"pytables": "tables", "geopandas-base": "geopandas", "pytorch": "torch"}
