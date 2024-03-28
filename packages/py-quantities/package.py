# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQuantities(PythonPackage):
    # BEGIN VERSIONS
    version("0.14.1", sha256="b2edf67b8c2a28aa3bbe096f9fc3ec3ab83fc3192997373641cddab32bea2f72", url="https://pypi.org/packages/d8/87/d5042d2a7b689a1bd69d9d37ec19c60d97f29c9009fc47500e41ac27e20e/quantities-0.14.1-py3-none-any.whl")
    version("0.13.0", sha256="0fde20115410de21cefa786f3aeae69c1b51bb19ee492190324c1da705e61a81", url="https://pypi.org/packages/1b/f9/caf2a8fac182eb8cb9331abdd48658bcee9d326d1d36f27ba00fcc158a55/quantities-0.13.0.tar.gz")
    version("0.12.5", sha256="67546963cb2a519b1a4aa43d132ef754360268e5d551b43dd1716903d99812f0", url="https://pypi.org/packages/a6/e7/bc3fcbc6ad890a0ddbeddc776d7ffd0a112fc0ee9c56b269c955fca4ca3a/quantities-0.12.5.tar.gz")
    version("0.12.4", sha256="a33d636d1870c9e1127631185d89b0105a49f827d6aacd44ad9d8f151f331d8b", url="https://pypi.org/packages/2b/4f/2e8ce7d6c16fb07c43036f8539962322b2bf241e7397e87f318a1aa2f7c4/quantities-0.12.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.19.0:", when="@0.14")
    # END DEPENDENCIES

