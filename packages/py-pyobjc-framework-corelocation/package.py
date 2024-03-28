# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorelocation(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="59497cc210023479e03191495c880e61fb6f44ad6c435ed1c8dd8def39f3aada", url="https://pypi.org/packages/e5/f3/3a7008caff53b84df92fface16f9bb66a2d4bcddb79261b57bd374479ad3/pyobjc-framework-CoreLocation-10.2.tar.gz")
    version("10.1", sha256="f43637443c4386233c52b0af3131a545968229543f7b0050764298cac1604fd8", url="https://pypi.org/packages/38/55/3420dd3cc3678d1625fae730a3eae69270e917dd6b45c69476bf92e79cc0/pyobjc-framework-CoreLocation-10.1.tar.gz")
    version("10.0", sha256="d84001ab5ef58441514bd92ed9b2fd4225faf0241d2a09ab503592fbc6a6066d", url="https://pypi.org/packages/a8/d0/4ee78cfbca3e3df0c6dc81e028bad6a23d0f2f08ebd81b933160798dc0fa/pyobjc-framework-CoreLocation-10.0.tar.gz")
    version("9.2", sha256="a6a59e6d1297f84c99dfa9f4ac3927af2fc851b6a1999617f5c159571f885c43", url="https://pypi.org/packages/ce/f4/e2a190a76bca21a435b59d467f9d1b53e5f6225a2a773accba3d2bb46077/pyobjc-framework-CoreLocation-9.2.tar.gz")
    version("9.1.1", sha256="e7fb6612535f9772cc698020303fc35ac72227958c17a1437aef6c04821d0e31", url="https://pypi.org/packages/c0/ef/6afda435ce7f196d29247217f82b54102ce6793ed61dc86b9406f2aff04f/pyobjc-framework-CoreLocation-9.1.1.tar.gz")
    version("9.1", sha256="e3e3601053893234143c454cf34aa15db98addde152c49a1e9a77d6c2d14321c", url="https://pypi.org/packages/29/1c/53ab1554b8cdf456435a5ad049112abf90d1b88b19e0468aacb29fc52882/pyobjc-framework-CoreLocation-9.1.tar.gz")
    version("9.1-beta1", sha256="319d1c3d75d4ef6fc2476ac8138217123cee48d143adfa8d2bca06aa772bbe8d", url="https://pypi.org/packages/79/81/418b6592d8f1786f6fbc0f02d531e34ea46dbe7d771c6b538663be933ba7/pyobjc-framework-CoreLocation-9.1b1.tar.gz")
    version("9.0.1", sha256="a1454ed210ffb3eb46df3876741fabe8ebe7b877074868df9ee550345a6ee6d5", url="https://pypi.org/packages/55/f2/4b25f2b0362a7d7c88dee615fc01cb42d46da54dbe8d0d3120f47e65cff9/pyobjc-framework-CoreLocation-9.0.1.tar.gz")
    version("9.0", sha256="8baf43809be6e51a0b390054729f15588ec8900a806e081de10c8e759ee67c5d", url="https://pypi.org/packages/8a/d9/6245937f52724a51f2bd0db145e0448e6f614382bbe7af1849359bf8a134/pyobjc-framework-CoreLocation-9.0.tar.gz")
    version("8.5.1", sha256="86f6ea60e8459a63dde380cc2086ff1faddc54d9c776246a65cae5f7c34492d9", url="https://pypi.org/packages/d8/42/b5ee4d3fa824c589b5f4e2e4fc9004979674b636b39780653ab232559750/pyobjc-framework-CoreLocation-8.5.1.tar.gz")
    version("8.5", sha256="f748573675afddf43440f3768d890d691efbd3e76d04596f412dbe2bc9a40267", url="https://pypi.org/packages/63/71/187e0812fec3a3d06be5e20a005390e416441fee3838356bf1469c9389aa/pyobjc-framework-CoreLocation-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

