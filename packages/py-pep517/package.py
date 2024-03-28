# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPep517(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.12.0", sha256="dd884c326898e2c6e11f9e0b64940606a93eb10ea022a2e067959f3a110cf161", url="https://pypi.org/packages/f4/67/846c08e18fefb265a66e6fd5a34269d649b779718d9bf59622085dabd370/pep517-0.12.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-tomli@1.1:", when="@0.13: ^python@:3.10")
        depends_on("py-tomli@1.1:", when="@0.11.1:0.12")
    # END DEPENDENCIES

