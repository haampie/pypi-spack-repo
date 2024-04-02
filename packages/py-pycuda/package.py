# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPycuda(PythonPackage):
    # BEGIN VERSIONS
    version("2021.1", sha256="ab87312d0fc349d9c17294a087bb9615cffcf966ad7b115f5b051008a48dd6ed", url="https://pypi.org/packages/5a/56/4682a5118a234d15aa1c8768a528aac4858c7b04d2674e18d586d3dfda04/pycuda-2021.1.tar.gz")
    version("2020.1", sha256="effa3b99b55af67f3afba9b0d1b64b4a0add4dd6a33bdd6786df1aa4cc8761a5", url="https://pypi.org/packages/46/61/47d3235a4c13eec5a5f03594ddb268f4858734e02980afbcd806e6242fa5/pycuda-2020.1.tar.gz")
    version("2019.1.2", sha256="ada56ce98a41f9f95fe18809f38afbae473a5c62d346cfa126a2d5477f24cc8a", url="https://pypi.org/packages/5e/3f/5658c38579b41866ba21ee1b5020b8225cec86fe717e4b1c5c972de0a33c/pycuda-2019.1.2.tar.gz")
    version("2016.1.2", sha256="a7dbdac7e2f0c0d2ad98f5f281d5a9d29d6673b3c20210e261b96e9a2d0b6e37", url="https://pypi.org/packages/e8/3d/4b6b622d8a22cace237abad661a85b289c6f0803ccfa3d2386103307713c/pycuda-2016.1.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3", when="@2020:2022.1")
    # END DEPENDENCIES

