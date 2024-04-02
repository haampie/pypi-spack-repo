# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSafetykit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="b5822cda3b1dc0209fa58027551fa17457763275902c7d42fc23d5b13de9ee67", url="https://pypi.org/packages/cb/01/3f54482dd8e4660fd64e11fd1d807639f60b1493b4b79651d27464fed65d/pyobjc-framework-SafetyKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

