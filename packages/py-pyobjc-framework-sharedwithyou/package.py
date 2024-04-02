# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSharedwithyou(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="bc13756ef20af488cd3022c036a11a0f7572e1b286e9eb7d31c61a8cb7655c70", url="https://pypi.org/packages/66/95/d31fba1615926f36c7bcf3014fbc343a87ce7679bffa9758bc3b65e3e7f4/pyobjc-framework-SharedWithYou-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-sharedwithyoucore@10.2:", when="@10.2:")
    # END DEPENDENCIES

