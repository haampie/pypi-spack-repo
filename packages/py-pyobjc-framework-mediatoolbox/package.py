# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMediatoolbox(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="614ec0a28c810395274aa1d5348a447f67bae4629a3a8372d14162f38e2fc597", url="https://pypi.org/packages/c8/c9/7f17e8424a36c82b7a320ad9ac8699c8956c5d0c8fbb40b557d6506d62d9/pyobjc-framework-MediaToolbox-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

