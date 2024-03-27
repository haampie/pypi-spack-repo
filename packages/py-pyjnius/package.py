##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyjnius(PythonPackage):
    version("1.3.0", sha256="d20845e75a2d18224e661d0e2bc2ce9141f17472e685cd6579847b0a7b5da6ad", url="https://pypi.org/packages/69/62/a81f0bdd7a96831b920efeaec80d80b66991cb582a65f6e4ae8c9a10cffd/pyjnius-1.3.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-cython", when="@1.2.1:1.3")
        depends_on("py-six@1.7:", when="@1.2.1:1.3")

