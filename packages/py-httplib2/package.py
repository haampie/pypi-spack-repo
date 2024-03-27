##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHttplib2(PythonPackage):
    version("0.22.0", sha256="14ae0a53c1ba8f3d37e9e27cf37eabb0fb9980f435ba405d546948b009dd64dc", url="https://pypi.org/packages/a8/6c/d2fbdaaa5959339d53ba38e94c123e4e84b8fbc4b84beb0e70d7c1608486/httplib2-0.22.0-py3-none-any.whl")
    version("0.21.0", sha256="987c8bb3eb82d3fa60c68699510a692aa2ad9c4bd4f123e51dfb1488c14cdd01", url="https://pypi.org/packages/31/c9/4720a06cc961415e49735e672071b1da1621a347e14a9b1f3728a59a2cbd/httplib2-0.21.0-py3-none-any.whl")
    version("0.20.4", sha256="8b6a905cb1c79eefd03f8669fd993c36dc341f7c558f056cb5a33b5c2f458543", url="https://pypi.org/packages/59/0f/29725a9caf4b2618f524e0f28e2bda91aca8f880123ec77426ede6ea1ea4/httplib2-0.20.4-py3-none-any.whl")
    version("0.20.2", sha256="6b937120e7d786482881b44b8eec230c1ee1c5c1d06bce8cc865f25abbbf713b", url="https://pypi.org/packages/b3/20/511741a05f8a59dc98f5ad9962efdc4f7bc1126329234e18b13f0cb3ddc4/httplib2-0.20.2-py3-none-any.whl")
    version("0.20.1", sha256="8fa4dbf2fbf839b71f8c7837a831e00fcdc860feca99b8bda58ceae4bc53d185", url="https://pypi.org/packages/1d/7c/9f5bfd49876524885c73d58c0335b4dfd81588dc9958120e99a1fcebcc7c/httplib2-0.20.1-py3-none-any.whl")
    version("0.20.0", sha256="ae39aed994e43f1001326b31eb904c2dca5b42c56c1569729041608ccc738a94", url="https://pypi.org/packages/b0/8e/6195be65d697988921ddbe6b42344aeec3a757ff318d7f1f279478e40222/httplib2-0.20.0.tar.gz")
    version("0.19.1", sha256="2ad195faf9faf079723f6714926e9a9061f694d07724b846658ce08d40f522b4", url="https://pypi.org/packages/15/dc/d14bce03f4bfd0214b90a3f556d7c96f75bb94ad597c816a641b962f22e9/httplib2-0.19.1-py3-none-any.whl")
    version("0.19.0", sha256="749c32603f9bf16c1277f59531d502e8f1c2ca19901ae653b49c4ed698f0820e", url="https://pypi.org/packages/15/7e/51e5bd333c0afa1c7bdbf98eb3b0ccf5167e2b1ecc8b4d13e9cc29291f81/httplib2-0.19.0-py3-none-any.whl")
    version("0.18.1", sha256="ca2914b015b6247791c4866782fa6042f495b94401a0f0bd3e1d6e0ba2236782", url="https://pypi.org/packages/b3/ad/d9d9331850ea5bd4f5cb8c650c0bfa119a4abd6b0ad7c45b6506bc979fc0/httplib2-0.18.1-py3-none-any.whl")
    version("0.18.0", sha256="4f6988e6399a2546b525a037d56da34aed4d149bbdc0e78523018d5606c26e74", url="https://pypi.org/packages/cc/f9/2a2c5be40e3d664cc3de70f72a9299fbe4fda5011e6ef1c008cfaef2d302/httplib2-0.18.0-py3-none-any.whl")
    version("0.13.1", sha256="cf6f9d5876d796539ec922a2c9b9a7cad9bfd90f04badcdc3bcfa537168052c3", url="https://pypi.org/packages/60/55/3902b9f33ad9c15abf447ad91b86ef2d0835a1ae78530f1410c115cf8fe3/httplib2-0.13.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyparsing@2.4.2:3.0.0-rc2,3.0.4:", when="@0.20.2:")
        depends_on("py-pyparsing@2.4.2:2", when="@0.19,0.20.1")

