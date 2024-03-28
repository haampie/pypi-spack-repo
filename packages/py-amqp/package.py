# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAmqp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.2.0", sha256="827cb12fb0baa892aad844fd95258143bce4027fdac4fccddbc43330fd281637", url="https://pypi.org/packages/b3/f0/8e5be5d5e0653d9e1d02b1144efa33ff7d2963dfad07049e02c0fa9b2e8d/amqp-5.2.0-py3-none-any.whl")
    version("5.1.1", sha256="6f0956d2c23d8fa6e7691934d8c3930eadb44972cbbd1a7ae3a520f735d43359", url="https://pypi.org/packages/de/a3/e7b3b9d34239bae066df135060e225929d639731050c920fdc740d6b7897/amqp-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="a575f4fa659a2290dc369b000cff5fea5c6be05fe3f2d5e511bcf56c7881c3ef", url="https://pypi.org/packages/bd/66/1b1031d30607fdd2a24a7b6106676ecc4e3ea8cbfeaf63a9d111b475459c/amqp-5.1.0-py3-none-any.whl")
    version("5.0.9", sha256="9cd81f7b023fc04bbb108718fbac674f06901b77bfcdce85b10e2a5d0ee91be5", url="https://pypi.org/packages/b9/80/76cc2ce4789c91394f43e0e78d86be5738b5223d106c11d78bacc260a559/amqp-5.0.9-py3-none-any.whl")
    version("5.0.8", sha256="61adb0c6f85518002023e2b0e1d7d9822f7456a409bbf86702fd264acc9ca5ce", url="https://pypi.org/packages/03/18/635ed71018cfaaae0c5e4915fbc065ac538b3fd7d69c263f89b683652f10/amqp-5.0.8-py3-none-any.whl")
    version("5.0.7", sha256="4d9cb6b5d69183ba279e97382ff68a071864c25b561d206dab73499d3ed26d1c", url="https://pypi.org/packages/5f/5e/3499863649093f0ca0a4641e3d62af803ac8205050ed333ecff53bf7f8f3/amqp-5.0.7-py3-none-any.whl")
    version("5.0.6", sha256="493a2ac6788ce270a2f6a765b017299f60c1998f5a8617908ee9be082f7300fb", url="https://pypi.org/packages/80/f1/cd7626c763e58f967317023c3dd01a2fab5d6f00f8e1c672ccceb3aae5cb/amqp-5.0.6-py3-none-any.whl")
    version("5.0.5", sha256="1e759a7f202d910939de6eca45c23a107f6b71111f41d1282c648e9ac3d21901", url="https://pypi.org/packages/89/52/452f0f12126bdf381176d65aab12320155d238c865f88c5b56901457d594/amqp-5.0.5-py3-none-any.whl")
    version("5.0.4", sha256="4d07bcfbebb470dc39fc0e711aabc0dd5b11d99db072b2f49b45b7d21a6183a0", url="https://pypi.org/packages/c7/49/0234fefc5c5f10fd36162a2b26f6ec6a67b626d29a38c2fc2cf8a3a7e5bd/amqp-5.0.4-py3-none-any.whl")
    version("5.0.3", sha256="2c58528a05dcbf2ae080f3141b6a5bf467949fad9234edd8b9085b8db2e325fe", url="https://pypi.org/packages/ab/aa/219def9160cd6714cda4ce95e4706eccd8a3d2b857e4f30ebd19dfd44aed/amqp-5.0.3-py3-none-any.whl")
    version("5.0.1", sha256="a8fb8151eb9d12204c9f1784c0da920476077609fa0a70f2468001e3a4258484", url="https://pypi.org/packages/6a/10/2d781823dd1366d7609148714e1a81af402c3c4d0ef52c1a1ac0716da9d0/amqp-5.0.1-py2.py3-none-any.whl")
    version("2.6.1", sha256="aa7f313fb887c91f15474c1229907a04dac0b8135822d6603437803424c0aa59", url="https://pypi.org/packages/bc/90/bb5ce93521772f083cb2d7a413bb82eda5afc62b4192adb7ea4c7b4858b9/amqp-2.6.1-py2.py3-none-any.whl")
    version("2.6.0", sha256="bb68f8d2bced8f93ccfd07d96c689b716b3227720add971be980accfc2952139", url="https://pypi.org/packages/4b/ab/650793fadefb63d6b730fbe7e64a38cbfaba1471d78dd2ebb8a5ee0f6c4a/amqp-2.6.0-py2.py3-none-any.whl")
    version("2.5.2", sha256="6e649ca13a7df3faacdc8bbb280aa9a6602d22fd9d545336077e573a1f4ff3b8", url="https://pypi.org/packages/fc/a0/6aa2a7923d4e82dda23db27711d565f0c4abf1570859f168e3d0975f1eb6/amqp-2.5.2-py2.py3-none-any.whl")
    version("2.5.1", sha256="19d851b879a471fcfdcf01df9936cff924f422baa77653289f7095dedd5fb26a", url="https://pypi.org/packages/a1/ef/a62ff9dde89e6b75976a746aa5b828ccb3c839ac6fcdc283edd88d7cf90b/amqp-2.5.1-py2.py3-none-any.whl")
    version("2.5.0", sha256="aa4409446139676943a2eaa27d5f58caf750f4ca5a89f888c452afd86be6a67d", url="https://pypi.org/packages/45/91/877ea2d1c3234dbb32e818d281615232468ff8a4a783a8fc264862b9f77b/amqp-2.5.0-py2.py3-none-any.whl")
    version("2.4.2", sha256="35a3b5006ca00b21aaeec8ceea07130f07b902dd61bfe42815039835f962f5f1", url="https://pypi.org/packages/42/ec/cbbaa8f75be8cbd019afb9d63258e2bdc95242f8c46a54bb90db5fef03bd/amqp-2.4.2-py2.py3-none-any.whl")
    version("2.4.1", sha256="16056c952e8029ce8db097edf0d7c2fe2ba9de15d30ba08aee2c5221273d8e23", url="https://pypi.org/packages/27/32/5c8a0d355b247446eb73f89c0fa4a22c1832764c0cc9d2bc43b9256d9366/amqp-2.4.1-py2.py3-none-any.whl")
    version("2.4.0", sha256="c3d7126bfbc640d076a01f1f4f6e609c0e4348508150c1f61336b0d83c738d2b", url="https://pypi.org/packages/e3/c3/a3b303cab73a9c3ee699f7229b33e262536204cfa9fe5df5274b1cf3dd4e/amqp-2.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-vine@5.0.0:", when="@5.1:")
        depends_on("py-vine@5.0.0:5.0", when="@5.0.1:5.0")
        depends_on("py-vine@1.1.3:1", when="@2.5:2")
        depends_on("py-vine@1.1.3:", when="@2.2:2.4")
    # END DEPENDENCIES

