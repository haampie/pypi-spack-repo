##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySeaborn(PythonPackage):
    version("0.13.2", sha256="636f8336facf092165e27924f223d3c62ca560b1f2bb5dff7ab7fad265361987", url="https://pypi.org/packages/83/11/00d3c3dfc25ad54e731d91449895a79e4bf2384dc3ac01809010ba88f6d5/seaborn-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="6baa69b6d1169ae59037971491c450c0b73332b42bd4b23570b62a546bc61cb8", url="https://pypi.org/packages/2d/46/cf3fce41ffc543b6e94dadbe6b647559d591df446ec716e72c3b4ce71b34/seaborn-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="70d740828c48de0f402bb17234e475eda687e3c65f4383ea25d0cc4728f7772e", url="https://pypi.org/packages/7b/e5/83fcd7e9db036c179e0352bfcd20f81d728197a16f883e7b90307a88e65e/seaborn-0.13.0-py3-none-any.whl")
    version("0.13.0-rc0", sha256="0208ce74c5e53957cffa46c33af380782dc68fbcb83d0377836a214c6baa1536", url="https://pypi.org/packages/4c/28/b5cb23050168179953362a1253384756ab20dd2733e9d3df3144d22b2002/seaborn-0.13.0rc0-py3-none-any.whl")
    version("0.12.2", sha256="ebf15355a4dba46037dfd65b7350f014ceb1f13c05e814eda2c9f5fd731afc08", url="https://pypi.org/packages/8f/2e/17bbb83fbf102687bb2aa3d808add39da820a7698159302a1a69bb82e01c/seaborn-0.12.2-py3-none-any.whl")
    version("0.12.1", sha256="a9eb39cba095fcb1e4c89a7fab1c57137d70a715a7f2eefcd41c9913c4d4ed65", url="https://pypi.org/packages/77/18/7354cb68dd7906d5a3118e0ed3e30c37502f9e6253139ecfcf4fa33af210/seaborn-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="cbeff3deef7c2515aa0af99b2c7e02dc5bf8b42c936a74d8e4b416905b549db0", url="https://pypi.org/packages/c2/03/14991c1f18422eb640f6fe6eadf9a675bb21d9339236d64c3d12bd0eb1a4/seaborn-0.12.0-py3-none-any.whl")
    version("0.11.2", sha256="85a6baa9b55f81a0623abddc4a26b334653ff4c6b18c418361de19dbba0ef283", url="https://pypi.org/packages/10/5b/0479d7d845b5ba410ca702ffcd7f2cd95a14a4dfff1fde2637802b258b9b/seaborn-0.11.2-py3-none-any.whl")
    version("0.11.1", sha256="4e1cce9489449a1c6ff3c567f2113cdb41122f727e27a984950d004a88ef3c5c", url="https://pypi.org/packages/68/ad/6c2406ae175f59ec616714e408979b674fe27b9587f79d59a528ddfbcd5b/seaborn-0.11.1-py3-none-any.whl")
    version("0.11.0", sha256="62439a38482decdb263a8339f54ecb9823995ad8716abc830e91ca0753201e70", url="https://pypi.org/packages/bc/45/5118a05b0d61173e6eb12bc5804f0fbb6f196adb0a20e0b16efc2b8e98be/seaborn-0.11.0-py3-none-any.whl")
    version("0.10.1", sha256="c901ce494541fb4714cfa7db79d0232dc3f4c4dfd3f273bacf17816084df5b53", url="https://pypi.org/packages/c7/e6/54aaaafd0b87f51dfba92ba73da94151aa3bc179e5fe88fc5dfb3038e860/seaborn-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="bdf7714ef7d4603e6325d3902e80a46d6149561e1cc237ac08a1c05c3f55a996", url="https://pypi.org/packages/70/bd/5e6bf595fe6ee0f257ae49336dd180768c1ed3d7c7155b2fdf894c1c808a/seaborn-0.10.0-py3-none-any.whl")
    version("0.9.1", sha256="2b285662f727c3a94f01c71a96a9c84f3552fa12a57c36ea971e3be3a3e2d5bb", url="https://pypi.org/packages/b2/86/43b8c9138ef4c2a1c492fee92792c83c13799d0e2061ff810d3826d06cd1/seaborn-0.9.1-py2.py3-none-any.whl")
    version("0.9.0", sha256="42e627b24e849c2d3bbfd059e00005f6afbc4a76e4895baf44ae23fe8a4b09a5", url="https://pypi.org/packages/a8/76/220ba4420459d9c4c9c9587c6ce607bf56c25b3d3d2de62056efe482dadc/seaborn-0.9.0-py3-none-any.whl")
    version("0.8.1", sha256="6702978b903d0284446e935916b980dfebae4063c18ad8eb6e8f9e76d0257eae", url="https://pypi.org/packages/10/01/dd1c7838cde3b69b247aaeb61016e238cafd8188a276e366d36aa6bcdab4/seaborn-0.8.1.tar.gz")
    version("0.8", sha256="732d08306449e3f041ed9f0c3cfadaf5480c8d352c2321b58f71e26607e34dfc", url="https://pypi.org/packages/d6/13/dd3da2cd6e03e522bbd389735d3adcb47d7a4470a968ebc3348fbac8eddd/seaborn-0.8.tar.gz")
    version("0.7.1", sha256="fa274344b1ee72f723bab751c40a5c671801d47a29ee9b5e69fcf63a18ce5c5d", url="https://pypi.org/packages/ed/dc/f168ff9db34f8c03c568987b4f81603cd3df40dd8043722d526026381a91/seaborn-0.7.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-matplotlib@3.4.0:3.6.0,3.6.2:", when="@0.13.1:")
        depends_on("py-matplotlib@3.3.0:3.6.0,3.6.2:", when="@0.13:0.13.0")
        depends_on("py-matplotlib@3.1.0:3.6.0,3.6.2:", when="@0.12.1:0.12")
        depends_on("py-matplotlib@3.1.0:", when="@0.12:0.12.0")
        depends_on("py-matplotlib@2.2.0:", when="@0.11")
        depends_on("py-matplotlib@2.1.2:", when="@0.10")
        depends_on("py-matplotlib@1.5.3:", when="@0.9.1-rc0:0.9")
        depends_on("py-matplotlib@1.4.3:", when="@0.9:0.9.0")
        depends_on("py-numpy@1.20.0:1.24.0-rc2,1.24.1:", when="@0.13:")
        depends_on("py-numpy@1.17.0:1.24.0-rc2,1.24.1:", when="@0.12.2:0.12")
        depends_on("py-numpy@1.17.0:", when="@0.12:0.12.1")
        depends_on("py-numpy@1.15.0:", when="@0.11")
        depends_on("py-numpy@1.13.3:", when="@0.10")
        depends_on("py-numpy@1.10.4:", when="@0.9.1-rc0:0.9")
        depends_on("py-numpy@1.9.3:", when="@0.9:0.9.0")
        depends_on("py-pandas@1.2.0:", when="@0.13:")
        depends_on("py-pandas@0.25.0:", when="@0.12")
        depends_on("py-pandas@0.23.0:", when="@0.11")
        depends_on("py-pandas@0.22:", when="@0.10")
        depends_on("py-pandas@0.17.1:", when="@0.9.1-rc0:0.9")
        depends_on("py-pandas@0.15.2:", when="@0.9:0.9.0")
        depends_on("py-scipy@1.0.0:", when="@0.11")
        depends_on("py-scipy@1.0.1:", when="@0.10")
        depends_on("py-scipy@0.17.1:", when="@0.9.1-rc0:0.9")
        depends_on("py-scipy@0.14:", when="@0.9:0.9.0")

