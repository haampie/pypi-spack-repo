# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPasskit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="0c879d632f0f0bf586161a7abbbba3dad9ba9894a3edbce06f4160491c2c134c", url="https://pypi.org/packages/49/2a/29810f864770d8e1430f5f982fa8094c31c45907249eef1a80b4244d39fa/pyobjc-framework-PassKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

