# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorewlan(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="f47dcf735145eb2f817db5c2134321a7cfb9274a634161ff3069617fd2afff42", url="https://pypi.org/packages/38/b4/c3c3fe7624d7b9840e38769dcdf8fc25d6eab3498418303e23c5e6578019/pyobjc-framework-CoreWLAN-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

