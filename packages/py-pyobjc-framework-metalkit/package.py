# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="42fc61371d49c2b86828d2a668b7badb2418c0ecce7595fce790830607bd8040", url="https://pypi.org/packages/08/d9/0c495e6c02c89b248cb0b762985a049d98c8d99cdd63742f67a66a665104/pyobjc-framework-MetalKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
    # END DEPENDENCIES

