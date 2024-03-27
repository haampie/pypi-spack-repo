##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLdsc(PythonPackage):
    version("2.0.1", sha256="6780af857d866a7c3fc987aef346887a719ba8564cc33ec6e626ffc6940bac43", url="https://pypi.org/packages/e5/28/0039f95b8c7d9db1f5623eeb9ff3260bb436c9f63a99e7feb429dfefeaad/ldsc-2.0.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-bitarray@2.6:", when="@2.0.1:")
        depends_on("py-nose@1.3.7:", when="@2.0.1:")
        depends_on("py-numpy@1.23.3:", when="@2.0.1:")
        depends_on("py-pandas@1.5.0:", when="@2.0.1:")
        depends_on("py-pybedtools@0.9:", when="@2.0.1:")
        depends_on("py-scipy@1.9.2:", when="@2.0.1:")

