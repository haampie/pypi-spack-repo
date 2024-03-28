# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPipreqs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.0", sha256="0809f6217028e35785f80e90217e18043e58c99ba28175e28320f9074dd03874", url="https://pypi.org/packages/36/38/cc1343c3a63655e18328e51e00c6e6851be648f1b8babffc5131f1b9f226/pipreqs-0.5.0-py3-none-any.whl")
    version("0.4.13", sha256="e522b9ed54aa3e8b7978ff251ab7a9af2f75d2cd8de4c102e881b666a79a308e", url="https://pypi.org/packages/d9/ea/74c89d786cf3403bfbf8fb70142fdf501af9517d0bb8c1acce3ee5ab613e/pipreqs-0.4.13-py2.py3-none-any.whl")
    version("0.4.12", sha256="f8ca40a95c6547f35760716ae9be4544627cd34e67e6f32446044ed851203a1b", url="https://pypi.org/packages/26/cd/88d111d38cc1366f277a7fc448282360eaa502df392cfd1db510e3b1dcff/pipreqs-0.4.12-py2.py3-none-any.whl")
    version("0.4.11", sha256="1510a91ae73ef6a8e2f24ffc8751132251cd61a01296d61538f37d1491841640", url="https://pypi.org/packages/1a/cd/74bbb901d65c375e2e8ab5601a4071d4ef38c745f6d4da74add61f964b9a/pipreqs-0.4.11-py2.py3-none-any.whl")
    version("0.4.10", sha256="cafe42ab70628d408c147fb8944bc303355ea8f91fddca4a98d273e572e39905", url="https://pypi.org/packages/9b/83/b1560948400a07ec094a15c2f64587b70e1a5ab5f7b375ba902fcab5b6c3/pipreqs-0.4.10-py2.py3-none-any.whl")
    version("0.4.9", sha256="2dfa21631cb68a97515e222d6f0033b5bfb75823567ca2195d528efb18c97990", url="https://pypi.org/packages/f8/8d/2e7c15bc5fcab54f9c5b404b5668fdac65f5e3224b2116097fae1299fc98/pipreqs-0.4.9-py2.py3-none-any.whl")
    version("0.4.8", sha256="2c88c53f8e76c86729aadd5faa23dce876ae5e40341fa6946b32110391964933", url="https://pypi.org/packages/fa/9e/c7470533ff80ac446ca1f21a6e2a482dbbe1e37f66e8d8a91746b2e18d6e/pipreqs-0.4.8-py2.py3-none-any.whl")
    version("0.4.7", sha256="e6a9e296ec5fd4cc239ac607d54a558bb6057be133796de723abd86f3023d1a5", url="https://pypi.org/packages/c7/0b/aa318b7d225dcc3a15f4e4961c4d9b34e9651a2935a82df85c180fc956b5/pipreqs-0.4.7-py2.py3-none-any.whl")
    version("0.4.6", sha256="54fb938b318f093c5226d0f99a92994bc83a209d2bca8801283f0b09f31ec634", url="https://pypi.org/packages/ae/ce/039773366e50247c58f216357829b0b24ba15c2d47531cdf54d6d4fedc83/pipreqs-0.4.6-py2.py3-none-any.whl")
    version("0.4.5", sha256="544f046e0b9822188305ec1e654abc6f820b0018627a3402ffe413d3d06f340b", url="https://pypi.org/packages/cc/f6/235b9d3904769ad255c4a0460ab74fd4eb6bb52774ff64bb762d44207dc7/pipreqs-0.4.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8.1:3.12", when="@0.5:")
        depends_on("py-docopt@0.6.2:", when="@0.5:")
        depends_on("py-docopt", when="@0.4.10:0.4")
        depends_on("py-ipython@8.12.3:8.12", when="@0.5:")
        depends_on("py-nbconvert@7.11:", when="@0.5:")
        depends_on("py-yarg@0.1.9:", when="@0.5:")
        depends_on("py-yarg", when="@0.4.10:0.4")
    # END DEPENDENCIES

