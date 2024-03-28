# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClustershell(PythonPackage):
    # BEGIN VERSIONS
    version("1.8.4", sha256="ff6fba688a06e5e577315d899f0dab3f4fe479cef99d444a4e651af577b7d081", url="https://pypi.org/packages/08/5a/ba0bfdcef8b129ac0fefa575b8e209d1f1370cead55657472b1f15d3d497/ClusterShell-1.8.4.tar.gz")
    version("1.8.3", sha256="cde552475e29a9b5ee80c0fb84e7491cae466c27f3d1d12882c0e3c315a52ba8", url="https://pypi.org/packages/f0/05/a1c7ff511d2830d232c34590a28aa81f9c8b246c6dc8787b451ed5e250f7/ClusterShell-1.8.3-py3-none-any.whl")
    version("1.8.1", sha256="e913efb4fe017eed9731d5ad8be397509e7f1966e6cb6441ee2bce074b16b310", url="https://pypi.org/packages/7f/63/d8c86ebdfd64195e2de73447a8729e7735d7654db14c9da0c52cda6b3ebc/ClusterShell-1.8.1.tar.gz")
    version("1.8", sha256="95dc937356a9c00a5a58f30d3826fb666d9c8b411a2e11134e1467c111bea0ae", url="https://pypi.org/packages/d5/8d/d3fa9b759566c9dfebe5e1f43bc69addd2fc5b9a6bbf87de2c8aeed94799/ClusterShell-1.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyyaml", when="@1.8.3")
    # END DEPENDENCIES

