# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMacholib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.16.3", sha256="0e315d7583d38b8c77e815b1ecbdbf504a8258d8b3e17b61165c6feb60d18f2c", url="https://pypi.org/packages/d1/5d/c059c180c84f7962db0aeae7c3b9303ed1d73d76f2bfbc32bc231c8be314/macholib-1.16.3-py2.py3-none-any.whl")
    version("1.16.2", sha256="44c40f2cd7d6726af8fa6fe22549178d3a4dfecc35a9cd15ea916d9c83a688e0", url="https://pypi.org/packages/5f/8c/8d7c7437f2799f570f9f4cb1fc974f671eff6fecd659f5e4097858a014ef/macholib-1.16.2-py2.py3-none-any.whl")
    version("1.16", sha256="5a0742b587e6e57bfade1ab90651d4877185bf66fd4a176a488116de36878229", url="https://pypi.org/packages/dc/02/0d0f2010c17918055a253ba00653b88b4c3af2ec960004fe35c2aaf36f8e/macholib-1.16-py2.py3-none-any.whl")
    version("1.15.2", sha256="885613dd02d3e26dbd2b541eb4cc4ce611b841f827c0958ab98656e478b9e6f6", url="https://pypi.org/packages/59/87/d92bad3903ad3b6e10e949ac1bfbfc660433c2a8ae26849947f23299cb41/macholib-1.15.2-py2.py3-none-any.whl")
    version("1.15.1", sha256="3781768cdbc8c7996cbf0c61844e80e715f870385358b17602b1c9c1eba9f48e", url="https://pypi.org/packages/98/d1/072caf59a77f3e177d914b09f7313f7ae423dc2685f3f3e8891240cbdb3d/macholib-1.15.1-py2.py3-none-any.whl")
    version("1.15", sha256="a86f0fa3ff8899d8cd7d4ed357d6da87448bb34199697f31275b9fc12478d6a8", url="https://pypi.org/packages/24/29/3fb277d4c289ce7557568a0a0ca06671a3e67b21627150c4881fd764899e/macholib-1.15-py2.py3-none-any.whl")
    version("1.14", sha256="c500f02867515e6c60a27875b408920d18332ddf96b4035ef03beddd782d4281", url="https://pypi.org/packages/3c/e1/c12f8d6af5d745ce88f270aeb243cb2bd6d8186320e5122df87fded29e4e/macholib-1.14-py2.py3-none-any.whl")
    version("1.13", sha256="c72bda118afe7799570fcb4114315d5c9c5416e48eacf1198da39b4d77201559", url="https://pypi.org/packages/93/be/cc6ac3fb59e38f2033c9006be147c198d77c28c2f2180e66743d4881571c/macholib-1.13-py2.py3-none-any.whl")
    version("1.11", sha256="ac02d29898cf66f27510d8f39e9112ae00590adb4a48ec57b25028d6962b1ae1", url="https://pypi.org/packages/41/f1/6d23e1c79d68e41eb592338d90a33af813f98f2b04458aaf0b86908da2d8/macholib-1.11-py2.py3-none-any.whl")
    version("1.10", sha256="a8941ff2cf2519859ed64d1248782442c98f5e1e28a1c331911d5501f74b7b37", url="https://pypi.org/packages/a1/01/845b2df65117dbdabf00c6df879625f4968ede6f512956710f05f4c7663a/macholib-1.10-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-altgraph@0.17:", when="@1.16.2:")
        depends_on("py-altgraph@0.15:", when="@1.9:1.16.0")
    # END DEPENDENCIES

