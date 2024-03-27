##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySparse(PythonPackage):
    version("0.15.1", sha256="6d5a19350b0714a1425b653a67df44be330d24e86f21c09f5ad6bb4518c2a18c", url="https://pypi.org/packages/07/a3/22e031f6833d84edd54b0809087d910907358bddc1c92e56b7b2db30f5ed/sparse-0.15.1-py2.py3-none-any.whl")
    version("0.15.0", sha256="4f6a68990958a8fde68a922465ca7348ea38a1cb029da3648ec3c6f3708c1fe7", url="https://pypi.org/packages/20/1c/995784c2f089b5063770fef97cba7beaf3bfe75679e792ad11ee0810072f/sparse-0.15.0-py2.py3-none-any.whl")
    version("0.14.0", sha256="77e3c32ace6184de29074db94901c63e113c7729b28c8b3f1885aaf5e1934323", url="https://pypi.org/packages/f0/58/f6d081dd0aab1eb8ffd3f1820b72506043db55cde20cac32ae92bca7e77f/sparse-0.14.0-py2.py3-none-any.whl")
    version("0.13.0", sha256="95ed0b649a0663b1488756ad4cf242b0a9bb2c9a25bc752a7c6ca9fbe8258966", url="https://pypi.org/packages/26/21/c796aaef2e9c805ea2e608893a67ff88395ded66788122959ac710ad4d6e/sparse-0.13.0-py2.py3-none-any.whl")
    version("0.12.0", sha256="8ab311165004a0ec4e80bd216397c6b682974fd384f0897dc0e6af4179b671a4", url="https://pypi.org/packages/46/20/c409a0d0ea7623a936080e0038eb77a02e62629a07944706c26f24ebcbb8/sparse-0.12.0-py2.py3-none-any.whl")
    version("0.11.2", sha256="08b937109203a69d1937ad7ea47a3ca4a552a48f7b5c40ba485b37ae6653b204", url="https://pypi.org/packages/e3/82/d58361f8107e8686196b91319edf2c26490667b8340cc229b668ee7a1582/sparse-0.11.2-py2.py3-none-any.whl")
    version("0.11.1", sha256="a26b1addd3e91dbf5d30f5afe5f84e40f7d1d40cc7ad4a7491761780a466024c", url="https://pypi.org/packages/85/b7/4475d77aa3adde08073c8143c43bbeaf33209409ead12c920d9cb83928d7/sparse-0.11.1-py2.py3-none-any.whl")
    version("0.11.0", sha256="246e5b0424932c491d4a4cef64d226f1edbbd9e0c740821d188c4b5ee4517ff8", url="https://pypi.org/packages/43/24/1793d6faf50873f778b1bf5fbca0a0b2b45ffddfc8954ccb63d94aa66332/sparse-0.11.0-py2.py3-none-any.whl")
    version("0.10.0", sha256="7b838e2709765a2476f7cfbce1b0d00678061199e9b211a180ff3f7a2961a76b", url="https://pypi.org/packages/3a/25/562a0cebb6fc36f16989469350ac96e9dbe2cc11dba0c22c34d0eff2f5dd/sparse-0.10.0-py2.py3-none-any.whl")
    version("0.9.1", sha256="5d7e9bab68b20f63ba6e8c593e46864ebef3a0842fa26fb32b71e743e6c5c99e", url="https://pypi.org/packages/08/73/34946ead922c072d7981be5b917f5871961a1b3bab4bc43dcd861de9ac23/sparse-0.9.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numba@0.49:", when="@0.10:")
        depends_on("py-numba@0.45:", when="@0.8:0.9")
        depends_on("py-numpy@1.17.0:", when="@0.12:")
        depends_on("py-numpy", when="@:0.2,0.8:0.11")
        depends_on("py-scipy@0.19:", when="@0.2:")

