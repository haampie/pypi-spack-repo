# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGamecontroller(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="81ad502346904995ec04b0580bab94ab32ca847fad06bca88cdf2ec6222b80ae", url="https://pypi.org/packages/7c/3c/a5b8df9c0c11ba380a2aa73e9e64e74254a5d07426507dd6a900d8197799/pyobjc-framework-GameController-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

