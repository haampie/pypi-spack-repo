##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBlis(PythonPackage):
    version("0.9.1", sha256="7ceac466801f9d97ecb34e10dded8c24cf5e0927ea7e834da1cc9d2ed3fc366f", url="https://pypi.org/packages/74/1e/18f5068e5c4f2e10248f65bc0f799e9017f70749fa3f5c9fdd30be179784/blis-0.9.1.tar.gz")
    version("0.7.11", sha256="cec6d48f75f7ac328ae1b6fbb372dde8c8a57c89559172277f66e01ff08d4d42", url="https://pypi.org/packages/51/8c/60c85350f2e1c9647df580083a0f6acc686ef32d1a91f4ab0c624b3ff867/blis-0.7.11.tar.gz")
    version("0.7.10", sha256="343e8b125784d70ff6e1f17a95ea71538705bf0bd3cc236a176d153590842647", url="https://pypi.org/packages/6c/7b/4dc6e5079f85d3cb512897b60502d7d6789b9fdee554fe1909d3d5ff13cd/blis-0.7.10.tar.gz")
    version("0.7.9", sha256="29ef4c25007785a90ffc2f0ab3d3bd3b75cd2d7856a9a482b7d0dac8d511a09d", url="https://pypi.org/packages/ff/a1/0ece7b0cceda6ca764ecba21e32f099cebff3448d88aa33ff0fce708d34b/blis-0.7.9.tar.gz")
    version("0.7.8", sha256="f7d541bb06323aa350163ba4a3ad00e8effb3b53d4c58ee6228224f3928b6c57", url="https://pypi.org/packages/55/b2/9d1ea86b861c42b3a1cca6e1c01b744dbf69b8cf5731dd68f66431a3fb09/blis-0.7.8.tar.gz")
    version("0.4.1", sha256="d69257d317e86f34a7f230a2fd1f021fd2a1b944137f40d8cdbb23bd334cd0c4", url="https://pypi.org/packages/98/5a/f9b8a78e3d1fdde1b0215413d88ab55d907ab81f95b62418a6e9cda30dec/blis-0.4.1.tar.gz")
    version("0.4.0", sha256="d5dfb6adc2ec93b8f32006f8eb1f85e569ace0ef998b4e7bb6d9676ebe0010ce", url="https://pypi.org/packages/47/53/13af70296735ff51ec130ae980612299ad2392ccbcd550ce71b644e5bbe5/blis-0.4.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.15.0:", when="@0.7.11:0.7 ^python@:3.8")
        depends_on("py-numpy@1.19.0:", when="@0.7.11:0.7 ^python@3.9:")
        depends_on("py-numpy@1.15.0:", when="@0.2.4:0.4.0.0")

