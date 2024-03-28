# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScreentime(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="43afabfd0fd61eed91f11aba3de95091a4f05d7c7e63341f493026e5ff7b90e4", url="https://pypi.org/packages/51/ce/8dad8672e32c75c68e5a0226332845a7a1829ed21885c87d1414c4372f99/pyobjc_framework_ScreenTime-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="734e090debb954a890a564869f2af20b55b9f7b7875d360795c9875279d09bd9", url="https://pypi.org/packages/20/ca/7590842e2571b49ca1ed9ec187e969631e47aec96d56506d02054df2b088/pyobjc_framework_ScreenTime-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="800cbb0f5e1bc2ef04e1328e6263b5ec7585538e16989265a3fa8c33957744ed", url="https://pypi.org/packages/f2/f9/53bf01ec46816c86b20f502462dfe14eb9c8b65c557a874c8906d92117f7/pyobjc_framework_ScreenTime-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="420dd744a2f69fc38db25a3210049d983a91941ab1072a209ef83e7c6fed53c5", url="https://pypi.org/packages/e7/6b/457d7a23047e4a3a8c405a4963438bed66f2f554f7adaa92bb472cd0504b/pyobjc_framework_ScreenTime-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="ed45e0a7b7d4cf345c7c48dd7d37b1e429d35c30f2d4776433e0957e1b1de9a6", url="https://pypi.org/packages/dc/54/f36a33592f8c0add4b7b94a69707edd3a83c5db493740db8371633eb1fd1/pyobjc_framework_ScreenTime-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="fc7a0a904ac3b2ae3d9694c7767d596aa9761bed7c9a83e2c5d384f3d2dfb217", url="https://pypi.org/packages/b8/96/6ba34559c4798921484ba0571f31795f0761b329a60991cbdbfef3e7d29b/pyobjc_framework_ScreenTime-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="39d52381a07fd1933c4a38fe9497a19e83c0b4d5384601427c4c8dd49643bdb3", url="https://pypi.org/packages/98/64/b530ce3fb5be2d7dafd275324d593f51a6ee7781e0221ef489695c634154/pyobjc_framework_ScreenTime-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="abf9079a0bd253a3230c4df71252804324e4ded8649eff03a253b63fc1af046c", url="https://pypi.org/packages/84/e5/5b1991c62384f30534f8aa75ed61a76ea1a2678e0f5ce69ce5f888b8a824/pyobjc_framework_ScreenTime-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="759adf3a28589c8823a0f15c222fb4a821a3441ba2f868204c5298c11b6b6e47", url="https://pypi.org/packages/19/e0/e4b8bcbdb76a403ba2fcab5eff5aa474f81edb30e399165cedd8e46c2493/pyobjc_framework_ScreenTime-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="45d15baad0ca3888ce208f73da5a1e3c4cf472b177c795037ee83a85d2a0e48f", url="https://pypi.org/packages/df/01/24ededb34415066a39f2b88ed3c29e9cbef13f60e4f15df4edb4ab7b0dce/pyobjc_framework_ScreenTime-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

