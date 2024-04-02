# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalfx(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d98a0fd1f0d2d3ea54efa768e6817a8773566c820ae7a3a23497e1c492e11da7", url="https://pypi.org/packages/69/96/dafa41327a9c0649c958829624690c9be055f156dc1623f956e6c31b6b7c/pyobjc-framework-MetalFX-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
    # END DEPENDENCIES

