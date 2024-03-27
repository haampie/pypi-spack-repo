##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpglib(PythonPackage):
    version("2.3.1", sha256="736e25ec67c220cb20fab7017c4fe6382eedee223076d57f4047342b1bc68ce3", url="https://pypi.org/packages/bf/16/642c725894cef0d599f86e989c877a8f0bcbce4607d494ab653b2cbf3b5c/spglib-2.3.1.tar.gz")
    version("2.3.0", sha256="3dc375ed49107a2c22a91e47faa43a3a26b71debb42d7b3931def05418544e02", url="https://pypi.org/packages/23/c7/a333f2dbb9141a73c6a91065fdce163fbbd041f82314cd3476f9964be805/spglib-2.3.0.tar.gz")
    version("2.2.0", sha256="4a7c71f6adb860cbe14acdfd6ca43dcd29ecd9aed3f38c02cd76da80ffa5d01c", url="https://pypi.org/packages/54/13/04a95b4550bb698a4df25852b3a0b52379af2da23ec86c8c5079e843db20/spglib-2.2.0.tar.gz")
    version("2.1.0", sha256="8143545fdffc11fbcda4d705a6b6bcd4889de9bc3524b78df866a36dd0de0a4b", url="https://pypi.org/packages/5c/1b/d4d002ccc4c3d3c669a1c64d3cb865b81f95bc4e58e691ab37650d57f6e5/spglib-2.1.0.tar.gz")
    version("2.0.2", sha256="1d081ec22da4ab4fc3198e9445ddad6dec2261c43927831151d93e39422610aa", url="https://pypi.org/packages/9f/8d/fbf91ef1a55afebbfa0a0fca803c4601e2b63af110162aa30d0b14a959e2/spglib-2.0.2.tar.gz")
    version("2.0.1", sha256="f5f1cab835aec1b8d78cbf42989c54596a289a4a833fddc9f0c5f55cac1bc2c1", url="https://pypi.org/packages/41/5a/6fb3aea1c13da1edab9540d7fd1d9b4d626fd9ad57bf4a90662d1fd24361/spglib-2.0.1.tar.gz")
    version("2.0.0", sha256="cbbd5e1d6096577c58b2fa47a5ea4f433a1932e5bc1cd1b691ea387c1b2e9974", url="https://pypi.org/packages/0c/7e/baf267d39072b6394f90e33938c826df7704dc374480e88f3b9a1bcca256/spglib-2.0.0.tar.gz")
    version("1.16.5", sha256="2eacefd53cc644ba9a90c4681fd6c934b6bdd818c113d7f319904e078d5dab93", url="https://pypi.org/packages/f4/e9/97e16eb2012e25c35f5e4946736cf08b563d3d779daf41c40dabc202016a/spglib-1.16.5.tar.gz")
    version("1.16.4", sha256="a9583ced33857d5706fad0ff279340803a8f23b46ad1e923298eb84879f4c5ea", url="https://pypi.org/packages/a3/db/af8932fd05f3e7e9ae5e2d0927d6e5e5f2a41f76aacb4fe20c85d2ca4b95/spglib-1.16.4.tar.gz")
    version("1.16.3", sha256="ff1420967d64c2d4f0d747886116a6836d9b473454cdd73d560dbfe973a8a038", url="https://pypi.org/packages/f2/d1/87d8b5d08fb1256daa9be7a7980cdd99e850f66b9fa8a65a1f9b72816b22/spglib-1.16.3.tar.gz")
    version("1.16.1", sha256="9fd2fefbd83993b135877a69c498d8ddcf20a9980562b65b800cfb4cdadad003", url="https://pypi.org/packages/4e/9a/e3f7a39a110593e117f3a6d5047c0f85d48923aef78c952da3a718ccecd0/spglib-1.16.1.tar.gz")
    version("1.9.9.18", sha256="cbbb8383320b500dc6100b83d5e914a26a97ef8fc97c82d8921b10220e4126cd", url="https://pypi.org/packages/59/55/cd46678b8aa5bb2a126de0611c3d693b3696733baed5bbfe8405680f0a6e/spglib-1.9.9.18.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@1.9.9.121:1.9.10.0,1.10:1.10.0.0,1.10.2:1.10.3.5,1.10.3.20:1.10.3.65,1.10.4.11:1.12,1.13.0.post5:1.16.0,2.1:")

