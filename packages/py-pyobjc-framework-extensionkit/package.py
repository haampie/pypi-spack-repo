# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkExtensionkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="343c17ec1696947cde6764b32f741d00d7424a620cdbaa91d9bcf47025b77718", url="https://pypi.org/packages/98/50/cf74917661bf524e9fcc2c8ce5925c08e3b8b8d022ef80b9e488723b8d81/pyobjc-framework-ExtensionKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

