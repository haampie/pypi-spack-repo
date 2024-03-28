# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNpx(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.2", sha256="239a8502282cf382781c5fc15a9932a717fef5ca8b65ac8aee913b7cfacd347e", url="https://pypi.org/packages/7d/0f/f0e377caac1951ae5b1997b071a53c860df5e157212e63b838ff427d682d/npx-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="6ce3d860a5e2d7303b3ba58a55f1a8e68c3040c281de6a59fc560ab09702e0a7", url="https://pypi.org/packages/7f/61/a856139e5a91641a025fef883aae7d61acbe8970290a8c5722217ed12129/npx-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="5e07deadbf43096d8e1ec63dcd51b34e8d638e8e7e4a95d465e143e5701a0308", url="https://pypi.org/packages/4b/c8/4d8f80bf78c38268274b29c45a1a99ade4ade02b4d8c444ddbcc5fbaf1dd/npx-0.1.0-py3-none-any.whl")
    version("0.0.25", sha256="dc63b4377807ade5a110ae8745fc74bdeab48c4251483d020288ee50edbb3a9c", url="https://pypi.org/packages/ae/01/1d8c7f509eb4af5a3a91a94f0ebff38051b6056d106a3b7c7d4d134e12d3/npx-0.0.25-py3-none-any.whl")
    version("0.0.24", sha256="7dee676b6dc2b5d732f877b3f065919eaefc55cae74fb85303dd96d61b644d16", url="https://pypi.org/packages/0b/ad/eb3218ccdf86240e0f70e34a4c1b16dab34e68e5f1a5bc274f8fb19879d7/npx-0.0.24-py3-none-any.whl")
    version("0.0.23", sha256="b36805cef375c242eb11637853edb7e8acd4a347f45deec667d541090f5665fa", url="https://pypi.org/packages/b8/73/7955a6c65f65486ca55f09fc0a0d382f71a47f0987a0f358bf2650b405a6/npx-0.0.23-py3-none-any.whl")
    version("0.0.22", sha256="a23130c4b8edd2f9fd0a5973c2549e4e50201d8e668cdb8959711b22c9dd5a3b", url="https://pypi.org/packages/00/51/7190e1019eda207624e0bb657b1ed6ee6df6572c3ad69b613015037d59aa/npx-0.0.22-py3-none-any.whl")
    version("0.0.21", sha256="e10a27b3677e5ea0efd97b5d2b03e4ebc2864b3918a4f0e1b63d9314b5fb05a6", url="https://pypi.org/packages/8c/4a/104ecbc96b21e2be5f787ea689022cd6c431a3f867ae4fef2ae4fb1e40f4/npx-0.0.21-py3-none-any.whl")
    version("0.0.20", sha256="f570259128614efe836daa86b013f2313652e020ec2f2b73ef82cf5725fc57bf", url="https://pypi.org/packages/1a/f7/6190ddfd95db3762b67bee36cdf7e865da025388b1ea6aa4f3c0aaac4318/npx-0.0.20-py3-none-any.whl")
    version("0.0.19", sha256="6402b2b11801fd2f0fbfb663ec8cd451505251307ec7b052df23e6fc2da6fe4c", url="https://pypi.org/packages/c4/8b/14bfceb980eb9c444805069055082ec7f1635a16123f04dca47e6760b1d1/npx-0.0.19-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.20.0:", when="@0.0.17:")
    # END DEPENDENCIES

