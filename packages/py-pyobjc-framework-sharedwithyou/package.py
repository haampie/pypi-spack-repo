##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSharedwithyou(PythonPackage):
    version("10.2", sha256="bc13756ef20af488cd3022c036a11a0f7572e1b286e9eb7d31c61a8cb7655c70", url="https://pypi.org/packages/66/95/d31fba1615926f36c7bcf3014fbc343a87ce7679bffa9758bc3b65e3e7f4/pyobjc-framework-SharedWithYou-10.2.tar.gz")
    version("10.1", sha256="bcac8ffa2642589a416c62ff436148586db9c41f92419a0164b1e9d6f6c73e38", url="https://pypi.org/packages/f2/4d/59ac45850a9f26587e0734f132115895cb6f37afdb4255a5d539d99ce432/pyobjc-framework-SharedWithYou-10.1.tar.gz")
    version("10.0", sha256="2d19cd38d54c3c5e85488e6f6264f83638984810d9d1601916abddd0984e6b8d", url="https://pypi.org/packages/fd/3a/ad3241b1d367ac01897776750e7cc49f6c44308f5f9324946dd8cf3dfe7b/pyobjc-framework-SharedWithYou-10.0.tar.gz")
    version("9.2", sha256="38edbaa24d05083ca736f2c2c718a897db803a4c34dd12e789999525c01d0104", url="https://pypi.org/packages/69/f7/8e55cecd1a0d99a60f7dcf6a25067d211f5e3d03dd68eac37e0d587c4e29/pyobjc-framework-SharedWithYou-9.2.tar.gz")
    version("9.1.1", sha256="c8e1ba484baf1468e82be9c626444575753a7c69d5c0cec0484d4781eff3da0f", url="https://pypi.org/packages/96/3a/7dd9675fd03bd051672bea8e86ddac2cde98fdee1ff7d240b8869da61f02/pyobjc-framework-SharedWithYou-9.1.1.tar.gz")
    version("9.1", sha256="97b9c6eafc6e77702ad06add1c10a77290adcd66153eb798803aaa9b20a60ad9", url="https://pypi.org/packages/b7/c1/a2118de9f9e2d7708d5315b39aa7179fdc9bcec9cc862f689b7f81439a43/pyobjc-framework-SharedWithYou-9.1.tar.gz")
    version("9.0.1", sha256="78637b858aeb99ec0830813f945e15db259c9cee0b916df371910b28af275008", url="https://pypi.org/packages/ea/d0/f65d705d89c78894c3725acac53bdbb254f3ec6331b654acb0418ff8d66f/pyobjc-framework-SharedWithYou-9.0.1.tar.gz")
    version("9.0", sha256="c656a61cd61d495460666e70f803362abb8b10959758ffaa05ad0dab6b98e34e", url="https://pypi.org/packages/2b/a7/a44b6e97a923ff6f45149e89c67744210d67de3ba22842a132c72caf7d41/pyobjc-framework-SharedWithYou-9.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-sharedwithyoucore@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-sharedwithyoucore@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-sharedwithyoucore@10:", when="@10:10.0")

