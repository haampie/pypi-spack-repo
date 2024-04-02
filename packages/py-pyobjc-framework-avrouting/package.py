# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAvrouting(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="133d646cf36cfa329c2b3a060c7b81368a95bfbb24f30e2bae2804be65b93ec9", url="https://pypi.org/packages/d9/0b/9c2686f2ea430a555d6f92d00be491e0eb630e2f4c0d7acfc0ff4dfa6db4/pyobjc-framework-AVRouting-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

