# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkStorekit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="44cf0b5fe605b9e5dc6aed2ae9e09d807d04d5f2eaf78afb8c04e3f109a0d680", url="https://pypi.org/packages/57/b6/122f3990665aa63beeae13487d079362c1e35d7ad76c63f95f95bb050d72/pyobjc-framework-StoreKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

