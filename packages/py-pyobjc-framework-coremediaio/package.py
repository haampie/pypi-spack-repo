# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremediaio(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="12f9fd93e610e61258f1acb023b868ed196e9444c69e38dfd314f8c256d07c9e", url="https://pypi.org/packages/9c/0d/c6641bd2bb653911612fc2580dbce1cc71d1a354c02051afb2603c068ebb/pyobjc-framework-CoreMediaIO-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

