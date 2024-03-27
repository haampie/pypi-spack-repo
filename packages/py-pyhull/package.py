##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyhull(PythonPackage):
    version("2015.2.1", sha256="d2ff0aa3298b548287587609a24f4e2aae7f7b8b1df152a90cd313260abc3a24", url="https://pypi.org/packages/2d/5e/1dab36627c5855dacf206ccecc78c91ad7cfe614187c93643044fabdd934/pyhull-2015.2.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@2015.2.1:")

