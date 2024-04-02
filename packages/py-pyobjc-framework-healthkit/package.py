# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkHealthkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="abcc4e6bd0e11eace7257887958b6cc5332f8aad4efa6b94e930425016540789", url="https://pypi.org/packages/03/46/b3e68efd4912aca0b99944c0f75d1c6f0d2b2ef6573d84cd165dd3a54007/pyobjc-framework-HealthKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

