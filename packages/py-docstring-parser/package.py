# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDocstringParser(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.15", sha256="d1679b86250d269d06a99670924d6bce45adc00b08069dae8c47d98e89b667a9", url="https://pypi.org/packages/89/e3/32e272db7adcf90e93f73e9a98fd763049ed7c641fb57ab26cb8f3e7e79c/docstring_parser-0.15-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3", when="@0.14:")
    # END DEPENDENCIES

