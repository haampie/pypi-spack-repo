# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBottleneck(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.8", sha256="6780d896969ba7f53c8995ba90c87c548beb3db435dc90c60b9a10ed1ab4d868", url="https://pypi.org/packages/f0/56/732cc7285ad7767ab248631b823fff2e6b9175a5bff86637627fa3fc6315/Bottleneck-1.3.8.tar.gz")
    version("1.3.8-rc5", sha256="410b7edb88e0714a89c545c1ea1a1f738f6960380fda3751df2de6f023fcea9d", url="https://pypi.org/packages/0c/dc/04b5f9c419825c9501de33a532f10763c3144d0ac2ee1af74666abf4816a/Bottleneck-1.3.8rc5.tar.gz")
    version("1.3.8-rc3", sha256="94ea5f12496c5127b382cdbc7a2873961c38e362d342480a4d64c726d313f2b6", url="https://pypi.org/packages/97/2c/11498e142e1392833fb4c4e6e147134e02fc7ac0b1c90f80c07382ee58d1/Bottleneck-1.3.8rc3.tar.gz")
    version("1.3.7", sha256="e1467e373ad469da340ed0ff283214d6531cc08bfdca2083361a3aa6470681f8", url="https://pypi.org/packages/98/1f/e5c91a94a9e695fe12442aa3a1c0c8fa7b09b1091ab885e288a45733c089/Bottleneck-1.3.7.tar.gz")
    version("1.3.7-rc1", sha256="b48dd84dedc987da66f6425192bdf4b0a22c78be4488fed9e5674b9374680f08", url="https://pypi.org/packages/ad/65/b71dbac889f748ddf7fee50d7d84ca5caad0e205257a1aa9aad5b4903a03/Bottleneck-1.3.7rc1.tar.gz")
    version("1.3.6", sha256="bc15e2545d4282d6f2529597df1bd6e4c5f0c44296b3f8425bc835305bd943c9", url="https://pypi.org/packages/4a/4f/2ee4ee0494384891fa7784d774affbcf2ad6c9ddb33b1fd211da86739513/Bottleneck-1.3.6.tar.gz")
    version("1.3.6-rc1", sha256="7cf01599879861362ea94bc1a64798ae0114e6e3af3723e37367520089d177ee", url="https://pypi.org/packages/a7/83/97c1946c5531b73c4601a9a6680fa30254525e1d6fa632946975451ed59a/Bottleneck-1.3.6rc1.tar.gz")
    version("1.3.5", sha256="2c0d27afe45351f6f421893362621804fa7dea14fe29a78eaa52d4323f646de7", url="https://pypi.org/packages/43/b1/1b3087073dbfaab4654720d78d3d14119f89f4397360b0f5f836bb9c228e/Bottleneck-1.3.5.tar.gz")
    version("1.3.5-rc2", sha256="cae3389b4306e8aaebc3e7a839d0f682c9ca85fef50be7db3e889b52800b70ba", url="https://pypi.org/packages/54/ab/81cd8d30ca56a4bf4888863524b8df899066c98728fb20403be0e9b87609/Bottleneck-1.3.5rc2.tar.gz")
    version("1.3.4", sha256="1764a7f4ad58c558723c542847eb367ab0bbb6d880a4e5d5eef30a0ece5cecea", url="https://pypi.org/packages/17/f0/5b06746ae8889b9fc47ccace8b98f81d8da0a22733744d88598e281b0069/Bottleneck-1.3.4.tar.gz")
    version("1.3.3", sha256="ede12eb8af5048f2f128a33424b9144111804dabedb9d48b411b9e5f2dc0ac20", url="https://pypi.org/packages/4e/66/5a91ce040af578a25b647507a5900a566bbcf3aeb93512bf6317a3dc41a5/Bottleneck-1.3.3.tar.gz")
    version("1.3.2", sha256="20179f0b66359792ea283b69aa16366419132f3b6cf3adadc0c48e2e8118e573", url="https://pypi.org/packages/5b/08/278c6ee569458e168096f6b51019cc1c81c288da3d1026a22ee2ccead102/Bottleneck-1.3.2.tar.gz")
    version("1.3.1", sha256="451586370462cb623d6ad604a545d1e97fb51d2ab5252b1ac57350a83e494a28", url="https://pypi.org/packages/62/d0/55bbb49f4fade3497de2399af70ec0a06e432c786b8623c878b11e90d456/Bottleneck-1.3.1.tar.gz")
    version("1.3.0", sha256="9d7814c61c31f42cfb4f26e050c2659c88a198f1398a9714174ae78347aad737", url="https://pypi.org/packages/b8/d9/2b0beb43e0f8b25624699f918d6b00e53c46812da911eb15ec9ffebf1917/Bottleneck-1.3.0.tar.gz")
    version("1.2.1", sha256="6efcde5f830aed64feafca0359b51db0e184c72af8ba6675b4a99f263922eb36", url="https://pypi.org/packages/05/ae/cedf5323f398ab4e4ff92d6c431a3e1c6a186f9b41ab3e8258dff786a290/Bottleneck-1.2.1.tar.gz")
    version("1.0.0", sha256="8d9b7ad4fadf9648acc924a6ee522c7cb5b474e75faaad9d90dfd55e2805b495", url="https://pypi.org/packages/12/5c/567d4b3b764013cd22451d0aeba4a9fc7dbde08f16752b808adae1aba776/Bottleneck-1.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.3.8-rc3:")
    # END DEPENDENCIES

