# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoretext(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="59ef8ca8d88bb53ce9980dda0b8094daa3e2dabe355847365ba965ff0b49f961", url="https://pypi.org/packages/51/51/17409f0a85753e780893515d9a525eb291852428cac18839601161535553/pyobjc-framework-CoreText-10.2.tar.gz")
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

