# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGameplaykit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="068ee6f3586f4033d25ed3b0451eab8f388b2970be1dfbe39be01accca7a9b2e", url="https://pypi.org/packages/ae/5b/ec8707e9a84d85cd219da45fa098890cf69e13be4dd447e8fc37d0352ca6/pyobjc-framework-GameplayKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-spritekit@10.2:", when="@10.2:")
    # END DEPENDENCIES

