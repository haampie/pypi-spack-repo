# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetal(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="652050cf9f5627dba36b31ad134e56c49040d0dcfaf93a7026018ef17330a01e", url="https://pypi.org/packages/03/c5/2d4ac87f9ea2196f8ae1b0d31b7470db9c4fdb1c981dedf48818685e2684/pyobjc-framework-Metal-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

