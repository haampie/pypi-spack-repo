# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNetworkextension(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="14f237bd96a822c55374584e99f2d79581b2d60570f34e4863800f934a44b82d", url="https://pypi.org/packages/0b/9c/69f2e265cb8560a0f1bc170831be1ecbcfef817e8e8d4a0bd330f185f1c0/pyobjc-framework-NetworkExtension-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

