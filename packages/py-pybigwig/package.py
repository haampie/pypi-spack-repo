# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybigwig(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.12", sha256="e01991790ece496bf6d3f00778dcfb136dd9ca0fd28acc1b3fb43051ad9b8403", url="https://pypi.org/packages/d5/0d/8e2a1edb9524790c6a4d0b70bc800a8e4afee1bc7bdd048c54b8d9cf1c32/pyBigWig-0.3.12.tar.gz")
    version("0.3.4", sha256="8c97a19218023190041c0e426f1544f7a4944a7bb4568faca1d85f1975af9ee2", url="https://pypi.org/packages/4d/7c/911e92392cf2d70d1a0da8fbb95be1e203f3cf9f858e030e98d4882c9ec7/pyBigWig-0.3.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numpy", default=False, description="numpy")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

