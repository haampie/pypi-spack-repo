# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAutomator(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="fb753e5bd40bfe720fa9e60e2ea5a1777b4c92082ffeba42b4055cdd56cb022d", url="https://pypi.org/packages/b0/c7/6f7231c6a560e95b6d32ad16712382229c7356497250f5f4dcd25079cbcf/pyobjc-framework-Automator-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

