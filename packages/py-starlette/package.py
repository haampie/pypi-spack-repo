# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStarlette(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.37.2", sha256="6fe59f29268538e5d0d182f2791a479a0c64638e6935d1c6989e63fb2699c6ee", url="https://pypi.org/packages/fd/18/31fa32ed6c68ba66220204ef0be798c349d0a20c1901f9d4a794e08c76d8/starlette-0.37.2-py3-none-any.whl")
    version("0.37.1", sha256="92a816002d4e8c552477b089520e3085bb632e854eb32cef99acb6f6f7830b69", url="https://pypi.org/packages/5b/d2/0faf92a81a25e08930feee166488873f8b8ceab1f6f9df8697cb29965347/starlette-0.37.1-py3-none-any.whl")
    version("0.37.0", sha256="53a95037cf6a563fca942ea16ba0260edce10258c213cbd554adc263fad22dfc", url="https://pypi.org/packages/4b/ec/7adae4eef578e3792fb01e4d4fd0b7f5f6956cb8aa5c9441eb4962155d06/starlette-0.37.0-py3-none-any.whl")
    version("0.36.3", sha256="13d429aa93a61dc40bf503e8c801db1f1bca3dc706b10ef2434a36123568f044", url="https://pypi.org/packages/eb/f7/372e3953b6e6fbfe0b70a1bb52612eae16e943f4288516480860fcd4ac41/starlette-0.36.3-py3-none-any.whl")
    version("0.36.2", sha256="e53e086e620ba715f0c187daca92927b722484d148e70921f0de075936119536", url="https://pypi.org/packages/69/bf/b8f2c0e1dd2a314712994e25405e6b03ed0d27795305aa68a22da08ffb01/starlette-0.36.2-py3-none-any.whl")
    version("0.36.1", sha256="d5b43a72f475fd1b9707f661aa66da42d59ae16c9b2a5845b4edee4309c425ee", url="https://pypi.org/packages/84/35/8a4e4564194fc929e700cf8a982dab356b49b6b40028ce8e9734785eab63/starlette-0.36.1-py3-none-any.whl")
    version("0.36.0", sha256="84edbd1d9e7a315390acd5789f1e4f93e834eb90f6a7d98450ef35e001ac3877", url="https://pypi.org/packages/a3/f7/c44db7e55691ed899bd2730df606b452413b7f8010929551f9eda6cc4a92/starlette-0.36.0-py3-none-any.whl")
    version("0.35.1", sha256="50bbbda9baa098e361f398fda0928062abbaf1f54f4fadcbe17c092a01eb9a25", url="https://pypi.org/packages/03/13/c60c738da2fb69d60ee1dc5631e8d152352003cc0bc4ce39582bdd90e293/starlette-0.35.1-py3-none-any.whl")
    version("0.35.0", sha256="521234a99a5b5a11de1d0e2e8cea775cf2eeb081ad9dec3d9cecc8aed5ea11a7", url="https://pypi.org/packages/5f/8d/254e9a509fe03647b8e91619bf064832e3f9c3e8edb00f44366d2993351f/starlette-0.35.0-py3-none-any.whl")
    version("0.34.0", sha256="2e14ee943f2df59eb8c141326240ce601643f1a97b577db44634f6d05d368c37", url="https://pypi.org/packages/fd/ec/e33d2726b2215af061cc8911f1420aedbb02ea5e8097d761f09a0512635c/starlette-0.34.0-py3-none-any.whl")
    version("0.32.0.post1", sha256="cd0cb10ddb49313f609cedfac62c8c12e56c7314b66d89bb077ba228bada1b09", url="https://pypi.org/packages/40/9e/6bfa6be40034fa04cc50e2a81d24a4e5b89279c688b51380d70ac31c0556/starlette-0.32.0.post1-py3-none-any.whl")
    version("0.32.0", sha256="bbc0973cfeba8cc767ee9b53f28d0b85fa77ab5045083e13fb99e6e7bcf0b748", url="https://pypi.org/packages/5b/98/a00e6c051944aecc358d64c9843eb48503044bb5d584545cedbebe8007c7/starlette-0.32.0-py3-none-any.whl")
    version("0.31.1", sha256="009fb98ecd551a55017d204f033c58b13abcd4719cb5c41503abbf6d260fde11", url="https://pypi.org/packages/c5/8c/38a89e8f477a57a506a5727fe5134b6043a9bc487835a5d52a56c457a1cf/starlette-0.31.1-py3-none-any.whl")
    version("0.31.0", sha256="1aab7e04bcbafbb1867c1ce62f6b21c60a6e3cecb5a08dcee8abac7457fbcfbf", url="https://pypi.org/packages/b0/a3/56d2ad63dd940fd9ccc3487ff26daffbb3a406116d91cfbc3d0c619852a9/starlette-0.31.0-py3-none-any.whl")
    version("0.30.0", sha256="cb15a5dfbd8de70c999bd1ae4b7e1ba625d74520bc57b28cc4086c7969431f2d", url="https://pypi.org/packages/48/ac/a61494868aa18d606cd4b0e4619c112a2e55f6638ced63ccb22817d66135/starlette-0.30.0-py3-none-any.whl")
    version("0.29.0", sha256="8814471c91ad98da5bec5792db16520a2a6d54b83e049dbc06a64c2019565081", url="https://pypi.org/packages/2d/7d/2a5b87a7e26d081f8b19f8edb77cd857fd94c33785e79287045dc1c5b00f/starlette-0.29.0-py3-none-any.whl")
    version("0.28.0", sha256="e58b9fc402c579950260fbb6d57173395c4e62804c40d3ede7e9ef1074f0c579", url="https://pypi.org/packages/ba/f3/3cca6acd03eb7e2da1dcf35148815d94e588bf7c1e555a002c888d8a23ee/starlette-0.28.0-py3-none-any.whl")
    version("0.27.0", sha256="918416370e846586541235ccd38a474c08b80443ed31c578a418e2209b3eef91", url="https://pypi.org/packages/58/f8/e2cca22387965584a409795913b774235752be4176d276714e15e1a58884/starlette-0.27.0-py3-none-any.whl")
    version("0.23.1", sha256="ec69736c90be8dbfc6ec6800ba6feb79c8c44f9b1706c0b2bb27f936bcf362cc", url="https://pypi.org/packages/a3/1d/b23984c05e39ddab35bbba33a3828dc4f896250220dcbd946c0fcad1e934/starlette-0.23.1-py3-none-any.whl")
    version("0.22.0", sha256="b5eda991ad5f0ee5d8ce4c4540202a573bb6691ecd0c712262d0bc85cf8f2c50", url="https://pypi.org/packages/1d/4e/30eda84159d5b3ad7fe663c40c49b16dd17436abe838f10a56c34bee44e8/starlette-0.22.0-py3-none-any.whl")
    version("0.21.0", sha256="0efc058261bbcddeca93cad577efd36d0c8a317e44376bcfc0e097a2b3dc24a7", url="https://pypi.org/packages/94/a3/777d1749aa0db3f9da12a8cc5f89fe01c95548909d012f0e419299c6d8a3/starlette-0.21.0-py3-none-any.whl")
    version("0.20.4", sha256="c0414d5a56297d37f3db96a84034d61ce29889b9eaccf65eb98a0b39441fcaa3", url="https://pypi.org/packages/51/37/8ac52116984d6a0d8502ec2c7e4a4a78f862b76410cdb1a4bcb384c91cb3/starlette-0.20.4-py3-none-any.whl")
    version("0.19.1", sha256="5a60c5c2d051f3a8eb546136aa0c9399773a689595e099e0877704d5888279bf", url="https://pypi.org/packages/f1/9d/1fa96008b302dd3e398f89f3fc5afb19fb0b0f341fefa05c65b3a38d64cf/starlette-0.19.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-anyio@3.4:", when="@0.19:")
        depends_on("py-typing-extensions@3.10:", when="@0.19: ^python@:3.9")
    # END DEPENDENCIES

