# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJacobi(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.2", sha256="7e57b2d9c62d47bce688ef4b3564adeb1def611cf5ed232ec39a6aa6083f7a8c", url="https://pypi.org/packages/b0/5c/2d6a44da539db44820b1c053958bfc4ee011e33f4f110175bfc712520440/jacobi-0.9.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@0.9.2:")
    # END DEPENDENCIES

