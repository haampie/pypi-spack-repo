# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUpdateChecker(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.18.0", sha256="cbba64760a36fe2640d80d85306e8fe82b6816659190993b7bdabadee4d4bbfd", url="https://pypi.org/packages/0c/ba/8dd7fa5f0b1c6a8ac62f8f57f7e794160c1f86f31c6d0fb00f582372a3e4/update_checker-0.18.0-py3-none-any.whl")
    version("0.17", sha256="1ff5dc7aab340b4f7710bd6c69d08ff5a5351617cd4ba0eb8886ddb285e2104f", url="https://pypi.org/packages/d6/c3/aaf8a162df8e8f9d321237c7c0e63aff95b42d19f1758f96606e3cabb245/update_checker-0.17-py2.py3-none-any.whl")
    version("0.16", sha256="59cfad7f9a0ee99f95f1dfc60f55bf184937bcab46a7270341c2c33695572453", url="https://pypi.org/packages/17/c9/ab11855af164d03be0ff4fddd4c46a5bd44799a9ecc1770e01a669c21168/update_checker-0.16-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests@2.3:", when="@0.17:")
    # END DEPENDENCIES

