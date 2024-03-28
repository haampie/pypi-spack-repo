# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMapclassify(PythonPackage):
    # BEGIN VERSIONS
    version("23.1", sha256="4f02efe049544f10ec1df84cb904f34a21796a5b0816093b329f6c99bbf417d7", url="https://pypi.org/packages/8b/8a/43b9291a4cddfea7776e8bfb139d358e63b2372d1359228037d39f3ef3a4/mapclassify-23.1-py3-none-any.whl")
    version("2.6.1", sha256="67a9a7f143e73eee053b2fc4c8d002bdc988a4d3b877c7d3d6993077359d0347", url="https://pypi.org/packages/3f/f1/8db36df379703311c16e5341b408dad04e34cfded66f38e351c380fbd5ae/mapclassify-2.6.1-py3-none-any.whl")
    version("2.6.0", sha256="3368ecd3ee197f1673979a2e19071a7dd7d88675cfa339c4fbb2432c118d9d47", url="https://pypi.org/packages/27/38/9ee51b78d134301c359b67ea6b493a9a60bca67ea044f8114387d0c4d7e7/mapclassify-2.6.0-py3-none-any.whl")
    version("2.4.3", sha256="dde0218d873b4778319387a10621cc97017a5c2533a48e68c39cb8d680c91846", url="https://pypi.org/packages/16/a8/7fc90e857d8f9db2498526500dc0e97e85c2519d4d74b1f45d24793b02c2/mapclassify-2.4.3-py3-none-any.whl")
    version("2.4.2", sha256="e2c9585bc0b17457d6b13bacaf1fc4222f7196408b6317e431b0397a03dad8c3", url="https://pypi.org/packages/22/8e/d968c0945d41bb02de0efaa92e31e43a817dc52d30e82b4dfdda407a1903/mapclassify-2.4.2-py3-none-any.whl")
    version("2.4.0", sha256="70f94a84220fb6d1bff69c6dcadbec75fc8ca8cac217acddda37e6268579dbff", url="https://pypi.org/packages/a4/24/fa7512ea4c4a07eb05f845023275edcbb73f08f9150662acbfd31bf5e047/mapclassify-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="29477d04de3bc290647571f7b79e890072b1bc989f0aaa8e95cad8cae16d5027", url="https://pypi.org/packages/11/80/cd58dc848a93bfb01c4b84f26e3d5d6c64266163ca1e2453c3f6fb291ef7/mapclassify-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="d8cce990f2df905ec7ba0d61a0de60a64635822684a2074cb412da9992dbf999", url="https://pypi.org/packages/91/b5/6b54f40901d89f2ce30cf2d8110dd57658db3e95db79baba6706d7588691/mapclassify-2.2.0.tar.gz")
    version("2.1.1", sha256="6994f398dae83cc0aafd844b78a7596ee9ddb0f8c0c73bb0b1af3550056c98a8", url="https://pypi.org/packages/9f/db/f35469e8acd792dad07e8908cd0df03615dad5e3bf4dac79d9e8512cef89/mapclassify-2.1.1.tar.gz")
    version("2.1.0", sha256="b59a603dc4b68ba1e6d5b296567b102e06a9df4c1e1dd4cfd6f7cfdc73fbdae0", url="https://pypi.org/packages/79/ef/13298309bab4e650c62764fe77e02b1bb5aab95c50677842467f07d6a628/mapclassify-2.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.6.1:2")
        depends_on("py-networkx@2.7:", when="@2.6.1:2")
        depends_on("py-networkx", when="@2.3:2.6.0,23:")
        depends_on("py-numpy@1.23.0:", when="@2.6.1:2")
        depends_on("py-numpy@1.3:", when="@2.3:2.6.0,23:")
        depends_on("py-pandas@1.4.0:1.5.0-rc0,1.5.1:", when="@2.6.1:2")
        depends_on("py-pandas@1.0.0:", when="@2.3:2.6.0,23:")
        depends_on("py-scikit-learn@1.0:", when="@2.6.1:2")
        depends_on("py-scikit-learn", when="@2.3:2.6.0,23:")
        depends_on("py-scipy@1.8.0:", when="@2.6.1:2")
        depends_on("py-scipy@1.0.0:", when="@2.3:2.6.0,23:")
    # END DEPENDENCIES

