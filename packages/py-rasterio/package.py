# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRasterio(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.9", sha256="fc6d0d290492fa1a5068711cfebb21cc936968891b7ed9da0690c8a7388885c5", url="https://pypi.org/packages/bd/b8/84f5e6ee1d7915d20ceaa7dbbf2589787c5819907b75c4f2b95386f88961/rasterio-1.3.9.tar.gz")
    version("1.3.8.post2", sha256="e45c6c46f07902cb87f25ed2f394ce0fddf19ff2396c8071f8afd22263c54258", url="https://pypi.org/packages/44/1b/879365a41fecfd806940b183777d738651dc6d8e98b242e0f7af9d44f83f/rasterio-1.3.8.post2.tar.gz")
    version("1.3.8.post1", sha256="98d5efd2dca85eb9d36af3928cc2dc430a2d29a7b24ee38b5004122860d75f77", url="https://pypi.org/packages/6d/36/bbcd4d1ca8010da5b7df0a907e8da2f89a5e3e045b7632dea30be19fa64b/rasterio-1.3.8.post1.tar.gz")
    version("1.3.8", sha256="ffdd18e78efdf8ad5861065fd812a66dd34264293317ff6540a078ea891cdef8", url="https://pypi.org/packages/2e/2e/65affa3bd9c6c8f4a3b4f7cbf7947d0a3b3a65675af58162f80201c01510/rasterio-1.3.8.tar.gz")
    version("1.3.7", sha256="abfdcb8f10210b8fad939f40d545d6c47e9e3b5cf4a43773ca8dd11c58204304", url="https://pypi.org/packages/7b/d8/7590109d7a62af60754c406ebf67c55f9646919a40096c5373d0f67bb525/rasterio-1.3.7.tar.gz")
    version("1.3.6", sha256="c8b90eb10e16102d1ab0334a7436185f295de1c07f0d197e206d1c005fc33905", url="https://pypi.org/packages/f2/d2/1772051f222ee507d893d4f3ab49d1e27b52f9c7eca9ffb4f75ad842e2f4/rasterio-1.3.6.tar.gz")
    version("1.3.5.post1", sha256="78efee9b975c0601c67817abb501333c722125e38d10f90addf1bcb7a49008b3", url="https://pypi.org/packages/ce/93/7249e6874bfdf58b09922c2c372d33366e8c7e3a73a9a2447f61c462557e/rasterio-1.3.5.post1.tar.gz")
    version("1.3.5", sha256="92358c3d4d5d6f3c7cd2812c8832d5175abce02b11bc101ac9548ff07163e8e2", url="https://pypi.org/packages/ca/4a/2a34788caa5d04f805f3619f9198736ce57ab59741133790c5d9cc7bc684/rasterio-1.3.5.tar.gz")
    version("1.3.4", sha256="5a8771405276ecf00b8ee927bd0a81ec21778dcfc97e4a37d0b388f10c9a41a8", url="https://pypi.org/packages/3b/5a/c4111c37c4a45fc41adc91e7fc45cff6da6213e977920e43b9274e1dd7e0/rasterio-1.3.4.tar.gz")
    version("1.3.3", sha256="b6fb1f12489f3a678c05ddcb78a74f0b6f63836219f51c0541e505f5e5208e7d", url="https://pypi.org/packages/51/07/811aa39f0430f51598489fe1fa2cc12bb23d285bd9743d847905c713e6c6/rasterio-1.3.3.tar.gz")
    version("1.3.2", sha256="a91b32f649bc5aa3259909349258eb7999b7e830375f63cd37ade2082066ec1c", url="https://pypi.org/packages/91/84/cbe179360554bc9d4673e4986c520899135cab180ec9818bad19d0a31f14/rasterio-1.3.2.tar.gz")
    version("1.3.1", sha256="91a22c512862e6411def675cd864eb63000ec2e0922c8bf25834c631ba80bdc1", url="https://pypi.org/packages/91/5c/8ad8a5bb99a313ad00723e92704bcc890e29f6361e89f9a84e45c48af989/rasterio-1.3.1.tar.gz")
    version("1.3.0", sha256="90171035e5b201cdb85a9abd60181426366040d4ca44706958db982a030f8dc4", url="https://pypi.org/packages/20/95/e1681dbd71d13a3858eadb5ae29c5366f57d955b3135812cee2168eb5402/rasterio-1.3.0.tar.gz")
    version("1.2.10", sha256="6062456047ba6494fe18bd0da98a383b6fad5306b16cd52a22e76c59172a2b5f", url="https://pypi.org/packages/44/5e/9f19e1e6fe980b59d8da8809f2e8f81eb7f0322c71914f077edcbcd9a110/rasterio-1.2.10.tar.gz")
    version("1.2.3", sha256="d8c345e01052b70ac3bbbe100c83def813c0ab19f7412c2c98e553d03720c1c5", url="https://pypi.org/packages/97/85/3591f1b04fc9e9038aff7d6c5ddc816e8a7c0c8362f69b70ed6455ebcebd/rasterio-1.2.3.tar.gz")
    version("1.1.8", sha256="f7cac7e2ecf65b4b1eb78c994c63bd429b67dc679b0bc0ecfe487d3d5bf88fd5", url="https://pypi.org/packages/73/2d/3e1bc56d75bf7c4cd5df51536992b3420197f2aa5ddd4d93e12100715dff/rasterio-1.1.8.tar.gz")
    version("1.1.5", sha256="ebe75c71f9257c780615caaec8ef81fa4602702cf9290a65c213e1639284acc9", url="https://pypi.org/packages/86/43/aae52a19a69ee30d28d0374c5f22d473ba3ba98ace4a5a5330a26590df95/rasterio-1.1.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.4-alpha1:")
        depends_on("py-affine", when="@0.29:1.0.3,1.0.5:1.0.18,1.0.21:1.1.5")
        depends_on("py-attrs", when="@1.0-alpha10:1.0.3,1.0.5:1.0.18,1.0.21:1.1.5")
        depends_on("py-click@4:7", when="@1.0.8:1.0.18,1.0.21:1.1.5")
        depends_on("py-click-plugins", when="@0.26:1.0.3,1.0.5:1.0.18,1.0.21:1.1.5")
        depends_on("py-cligj@0.5:", when="@1.0.7:1.0.18,1.0.21:1.1.5")
        depends_on("py-numpy", when="@0.29:1.0.3,1.0.5:1.0.18,1.0.21:1.1.5")
        depends_on("py-snuggs@1.4.1:", when="@1.0-alpha6:1.0.3,1.0.5:1.0.18,1.0.21:1.1.5")
    # END DEPENDENCIES

