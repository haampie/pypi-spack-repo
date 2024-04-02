# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonDotenv(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.1", sha256="f7b63ef50f1b690dddf550d03497b66d609393b40b564ed0d674909a68ebf16a", url="https://pypi.org/packages/6a/3e/b68c118422ec867fa7ab88444e1274aa40681c606d59ac27de5a5588f082/python_dotenv-1.0.1-py3-none-any.whl")
    version("0.19.2", sha256="32b2bdc1873fd3a3c346da1c6db83d0053c3c62f28f1f38516070c4c8971b1d3", url="https://pypi.org/packages/0e/f1/0317f4b2c5284075a2154fe95539b43c0acecbcb86fe80fcb2645803edd9/python_dotenv-0.19.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cli", default=False, description="cli")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@1:")
        depends_on("py-click@5:", when="+cli")
    # END DEPENDENCIES

