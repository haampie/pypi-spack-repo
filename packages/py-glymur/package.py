# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGlymur(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.9", sha256="6a3df886b87c94c6f33b44c69b814afdfbc09fd849da5ba9dfd89e6b2f293de3", url="https://pypi.org/packages/b2/2c/dc5b32c9b25255a8f8524e3290f8c62e78249fbe3f293c027985b1b2d411/Glymur-0.9.9-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.9.7:0.12.0")
        depends_on("py-lxml", when="@0.9.2,0.9.7:")
        depends_on("py-numpy", when="@0.9.2,0.9.7:")
        depends_on("py-packaging", when="@0.9.8:")
        depends_on("py-setuptools", when="@0.9.2,0.9.7:0.11")
    # END DEPENDENCIES

