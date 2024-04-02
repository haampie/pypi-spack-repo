# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreml(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="a1d7743a91160d096ccd3f5f5d824dafdd6b99d0c4342e8c18852333c9b3318e", url="https://pypi.org/packages/69/99/42c8a299a5b936eadac2c80429991194720514805950c8a13161d4d9df0b/pyobjc-framework-CoreML-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

