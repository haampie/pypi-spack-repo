##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPipreqs(PythonPackage):
    version("0.5.0", sha256="0809f6217028e35785f80e90217e18043e58c99ba28175e28320f9074dd03874", url="https://pypi.org/packages/36/38/cc1343c3a63655e18328e51e00c6e6851be648f1b8babffc5131f1b9f226/pipreqs-0.5.0-py3-none-any.whl")
    version("0.4.13", sha256="e522b9ed54aa3e8b7978ff251ab7a9af2f75d2cd8de4c102e881b666a79a308e", url="https://pypi.org/packages/d9/ea/74c89d786cf3403bfbf8fb70142fdf501af9517d0bb8c1acce3ee5ab613e/pipreqs-0.4.13-py2.py3-none-any.whl")
    version("0.4.12", sha256="f8ca40a95c6547f35760716ae9be4544627cd34e67e6f32446044ed851203a1b", url="https://pypi.org/packages/26/cd/88d111d38cc1366f277a7fc448282360eaa502df392cfd1db510e3b1dcff/pipreqs-0.4.12-py2.py3-none-any.whl")
    version("0.4.11", sha256="1510a91ae73ef6a8e2f24ffc8751132251cd61a01296d61538f37d1491841640", url="https://pypi.org/packages/1a/cd/74bbb901d65c375e2e8ab5601a4071d4ef38c745f6d4da74add61f964b9a/pipreqs-0.4.11-py2.py3-none-any.whl")
    version("0.4.10", sha256="cafe42ab70628d408c147fb8944bc303355ea8f91fddca4a98d273e572e39905", url="https://pypi.org/packages/9b/83/b1560948400a07ec094a15c2f64587b70e1a5ab5f7b375ba902fcab5b6c3/pipreqs-0.4.10-py2.py3-none-any.whl")
    version("0.4.9", sha256="cec6eecc4685967b27eb386037565a737d036045f525b9eb314631a68d60e4bc", url="https://pypi.org/packages/67/63/84409df1acd879d239e53599de2b3df45013e6cf46406fd94e86822635f3/pipreqs-0.4.9.tar.gz")
    version("0.4.8", sha256="eb82383bc903c03c17486fa128f963ccb606f15b67fb720041165bc8950a4538", url="https://pypi.org/packages/cb/d2/773745cb0fafb969efce863a88bfe76e36c0147acc548d7ffac27fca6734/pipreqs-0.4.8.tar.gz")
    version("0.4.7", sha256="baf5a6a1d3b6384e4ee0c2040a868f752fad4977340d76d1137e0a0f23241074", url="https://pypi.org/packages/fe/79/76711a075ee1c419c2f89576ce7ea2513bc562a346d74b2ab274dd812bf1/pipreqs-0.4.7.tar.gz")
    version("0.4.6", sha256="439543d659e426537ed6793c42142e3f4a95e0846dfac94fce7b186ba64f66ea", url="https://pypi.org/packages/a1/a5/d08430006ac08d5cdb7ecd2c345b45d1f21623b940ba801eb173ca71674c/pipreqs-0.4.6.tar.gz")
    version("0.4.5", sha256="8f375ef3fdbe13d2bbbb7f4e3023a4e7dd1ed4b80db1e6c4035dd0b09fc23832", url="https://pypi.org/packages/41/00/6cd70b6e3cde506fd350d07bcb50ba7861371521c54538322ec79660f0eb/pipreqs-0.4.5.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.8.1:3.12", when="@0.5:")
        depends_on("py-docopt@0.6.2:", when="@0.5:")
        depends_on("py-docopt", when="@0.4.10:0.4")
        depends_on("py-ipython@8.12.3:8.12", when="@0.5:")
        depends_on("py-nbconvert@7.11:", when="@0.5:")
        depends_on("py-yarg@0.1.9:", when="@0.5:")
        depends_on("py-yarg", when="@0.4.10:0.4")

