# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStarsessions(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.3", sha256="5c2aa725ab7466e0b27c827a95c0a436179f0f12f8d826ef2c554e7f50a9a79f", url="https://pypi.org/packages/aa/26/f0cac14f6cdcf70654550b2c6d6e7e5976a83053dcf25322ddadd2c2563d/starsessions-2.1.3-py3-none-any.whl")
    version("2.1.2", sha256="290494d61c8b54bb343016b2a12a2899653981d01730c925b9394a2603f7f98c", url="https://pypi.org/packages/58/b3/e2b5ba4363d735b80cef1f5ee67d3dd37b9292c1b4c2abe99909afd63897/starsessions-2.1.2-py3-none-any.whl")
    version("2.1.1", sha256="e3573ce6f3531b201021443fa5c7ec72d360835dcb102d384c4f87ac942005a6", url="https://pypi.org/packages/d0/97/8b0aaa98329252cf85bdc79b794ae7ac965a96842abde41ab724c298c957/starsessions-2.1.1-py3-none-any.whl")
    version("2.1.0", sha256="ece20a6f33df9384d844365816ce64af747988de65d5d4f3335dfc86ff0389e0", url="https://pypi.org/packages/c8/63/e573977f653cf4f2e7661bf58bf6b3d0208acf6fdaa408efc1f103d98203/starsessions-2.1.0-py3-none-any.whl")
    version("2.0.1", sha256="1ef2cc35bb0af385a0079adf3222575eea8df11a50b85ab4e8982ade54c84dce", url="https://pypi.org/packages/c9/4c/6111a9077d9f55a6d45da16af165684185acf5f889c967cda22119a94ce9/starsessions-2.0.1-py3-none-any.whl")
    version("1.3.0", sha256="c0758f2a1a2438ec7ba88b232e82008f2261a75584f01179c787b3636fae6040", url="https://pypi.org/packages/18/fa/6d33ea610c65f9ed27223860e1f4e25b2ac17c8780a69b6cf65ece037428/starsessions-1.3.0-py3-none-any.whl")
    version("1.2.3", sha256="084ad30407521c349f0e5b3bd8de12ae3ecefce0dec6dfcc6c2c60e2ae8047d0", url="https://pypi.org/packages/7e/17/44f79dab9ddbccd59624495cee13d80ad0d9a7106b9f271ec1244f8951a8/starsessions-1.2.3-py3-none-any.whl")
    version("1.2.1", sha256="2cbe154d74a9f09b64d2373b8c5f75b40caa3b2bc9a902207f1e5548c1ad31d7", url="https://pypi.org/packages/ee/4b/f47f28cba0f72167ee8b2fd9b7b5e9aa1e302992a3b2cffaedc8e69cec07/starsessions-1.2.1-py3-none-any.whl")
    version("1.1.5", sha256="5c775c05b30e9440fe4be625c61f404b53cdd987fa0c55793470e41242d79d2a", url="https://pypi.org/packages/73/f6/4d6cfb71ba0c971d96748946796e79d63873fbd0a1664529d0928c725b11/starsessions-1.1.5-py3-none-any.whl")
    version("1.1.4", sha256="2498ec1573a2013ce99a25d1bff46a31f469c1aaa59dcf40f0d868bc4efc9f02", url="https://pypi.org/packages/c9/72/74cde681e1a8b7665cca5704faaff75c23fbc1bb32d2db2c65849f42dfd5/starsessions-1.1.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-itsdangerous@2.0.1:")
        depends_on("py-redis@4.2:", when="@2.1:2.1.0")
        depends_on("py-starlette", when="@1.1.4:")
    # END DEPENDENCIES

