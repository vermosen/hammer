# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

setup(
    name="hammer",
    version="0.0.1",
    description="a minimal example package (with pybind11)",
    author="Jean-Mathieu Vermosen",
    license="MIT",
    packages=["hammer"],
    package_dir={"": "src"},
    cmake_install_dir="src/hammer",
)