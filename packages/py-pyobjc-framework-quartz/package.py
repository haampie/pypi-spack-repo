# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkQuartz(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="9b947e081f5bd6cd01c99ab5d62c36500d2d6e8d3b87421c1cbb7f9c885555eb", url="https://pypi.org/packages/9d/be/1895258fdac58acfdddb3af29cf80619778689c9254133e82d1a345d42a1/pyobjc-framework-Quartz-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

