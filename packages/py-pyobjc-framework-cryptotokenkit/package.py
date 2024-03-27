##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCryptotokenkit(PythonPackage):
    version("10.2", sha256="c0adfde2d53da7df1f8827bdf0cbf4419590151dd1041711ab2f66a32bd986f5", url="https://pypi.org/packages/a1/76/61044c432e6935b51e83417f39d76a1dc4ac01b4ecda455da5dde73d7065/pyobjc-framework-CryptoTokenKit-10.2.tar.gz")
    version("10.1", sha256="ad8fb3c4f314cc5f35cd26a5e3fdd68dd71ea0f7b063f31cffb9d78050ce76f0", url="https://pypi.org/packages/fc/71/87a9330f515b19fd660ab62a320156da19c24a1482a1a44f88e56656679f/pyobjc-framework-CryptoTokenKit-10.1.tar.gz")
    version("10.0", sha256="314fe7067cecc0901602173a47bcdb3107ddbae6a22052b0e217f79b7d388153", url="https://pypi.org/packages/fd/a8/6d9c9c959a97b90a19f70dd153c098f5b3b2279272b04e116a599b6f24de/pyobjc-framework-CryptoTokenKit-10.0.tar.gz")
    version("9.2", sha256="a835f178f066a1d71ed287eb637f4f38021402eb0e7d043970cb50b44ad4e714", url="https://pypi.org/packages/90/cd/f41fd8eb91910e09164f9f53fcd546987808235e8052e86991f07c8a37ae/pyobjc-framework-CryptoTokenKit-9.2.tar.gz")
    version("9.1.1", sha256="ba77f9c7022153013108ec5c2b28afa4f2890cf65c96a25185dc20f98b7b13da", url="https://pypi.org/packages/3e/ee/03039672d14b99307e7aadade1740fe5822afa5481b372c01ab3d6232763/pyobjc-framework-CryptoTokenKit-9.1.1.tar.gz")
    version("9.1", sha256="32d17ae92151a0b4b9b3e94c04b1f5c71ca9b4c46bbdd6bb63e728ff3dcd6aa4", url="https://pypi.org/packages/8d/43/126e6744adeed2f8d20bf985826077dc07449a115345b98b579661adc969/pyobjc-framework-CryptoTokenKit-9.1.tar.gz")
    version("9.0.1", sha256="b2f88362a2a9cc4b2e1df3163a2ad931f8db02a617f8536a630cc5bf6a64774c", url="https://pypi.org/packages/e2/8c/88f13d031cc55ecbfeaf382f418d5e38e52c0e8d20eda8ebb48169939a05/pyobjc-framework-CryptoTokenKit-9.0.1.tar.gz")
    version("9.0", sha256="add0ecfdda3df2db969a17bc07b7f92f8540a823690c2a4208ce40584a98a618", url="https://pypi.org/packages/20/41/ea237a740435a5020ca977f78d2d3691894ef1c8479823e6338fa2ad28ca/pyobjc-framework-CryptoTokenKit-9.0.tar.gz")
    version("8.5.1", sha256="71193d5bb9c95bf24166fdc442b8c46b6e4d4557becbcb701963dd48c9a63cde", url="https://pypi.org/packages/43/38/a16f2c98501c24d3b5eee55926fd6973d3392e77316275cb0ecb0cc698f2/pyobjc-framework-CryptoTokenKit-8.5.1.tar.gz")
    version("8.5", sha256="9d25d49eb5b8fd6e1992a2323426fa8a8cd432c801f789e1f1dd53b3721cc1b8", url="https://pypi.org/packages/eb/40/8f0aa145ab98fca808fe4f0c1182a673da3737d628840608286168169c57/pyobjc-framework-CryptoTokenKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

