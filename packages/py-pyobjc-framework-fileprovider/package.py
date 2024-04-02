# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkFileprovider(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1accc2965c59395152d04b2f4a096cb4a5364bca8094695ce2b60d2f794bff74", url="https://pypi.org/packages/b0/e5/15fc9fafa5686ff08c53e3b36f9c3445de76dca8695b6efc7c28b22f1028/pyobjc-framework-FileProvider-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

