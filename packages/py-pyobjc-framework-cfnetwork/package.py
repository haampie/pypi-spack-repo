# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCfnetwork(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="18ebd22c645b5b77c1df6d973a91cc035ddd4666346912b2a0c847803c23f4d4", url="https://pypi.org/packages/8c/cf/f7f8e8e91f6fa62b9bd774f9f64e3efa32b075423ad3c9ca37f55558a36c/pyobjc-framework-CFNetwork-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

