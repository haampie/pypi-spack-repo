# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyParsimonious(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.0", sha256="982ab435fabe86519b57f6b35610aa4e4e977e9f02a14353edf4bbc75369fc0f", url="https://pypi.org/packages/aa/0f/c8b64d9b54ea631fcad4e9e3c8dbe8c11bb32a623be94f22974c88e71eaf/parsimonious-0.10.0-py3-none-any.whl")
    version("0.8.1", sha256="3add338892d580e0cb3b1a39e4a1b427ff9f687858fdd61097053742391a9f6b", url="https://pypi.org/packages/02/fc/067a3f89869a41009e1a7cdfb14725f8ddd246f30f63c645e8ef8a1c56f4/parsimonious-0.8.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-regex@2022.3.15:", when="@0.10:")
    # END DEPENDENCIES

