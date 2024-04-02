# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorespotlight(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="bc4ac490953db29f6a58bc6fca6f819f8a810d0bb15d5f067451b3a8cad1cb50", url="https://pypi.org/packages/8d/94/867b96e673a466f43ad4d9e9ec3b10f904e5d5689e59b0c9b5ee3c45f609/pyobjc-framework-CoreSpotlight-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

