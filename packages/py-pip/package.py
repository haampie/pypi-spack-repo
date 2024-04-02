# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPip(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("23.1.2", sha256="3ef6ac33239e4027d9a5598a381b9d30880a1477e50039db2eac6e8a8f6d1b18", url="https://pypi.org/packages/08/e3/57d4c24a050aa0bcca46b2920bff40847db79535dc78141eb83581a52eb8/pip-23.1.2-py3-none-any.whl")
    version("23.0", sha256="b5f88adff801f5ef052bcdef3daa31b55eb67b0fccd6d0106c206fa248e0463c", url="https://pypi.org/packages/ab/43/508c403c38eeaa5fc86516eb13bb470ce77601b6d2bbcdb16e26328d0a15/pip-23.0-py3-none-any.whl")
    version("22.2.2", sha256="b61a374b5bc40a6e982426aede40c9b5a08ff20e640f5b56977f4f91fed1e39a", url="https://pypi.org/packages/1f/2c/d9626f045e7b49a6225c6b09257861f24da78f4e5f23af2ddbdf852c99b8/pip-22.2.2-py3-none-any.whl")
    version("22.1.2", sha256="a3edacb89022ef5258bf61852728bf866632a394da837ca49eb4303635835f17", url="https://pypi.org/packages/96/2f/caec18213f6a67852f6997fb0673ae08d2e93d1b81573edb93ba4ef06970/pip-22.1.2-py3-none-any.whl")
    version("21.3.1", sha256="deaf32dcd9ab821e359cd8330786bcd077604b5c5730c0b096eda46f95c24a2d", url="https://pypi.org/packages/a4/6d/6463d49a933f547439d6b5b98b46af8742cc03ae83543e4d7688c2420f8b/pip-21.3.1-py3-none-any.whl")
    version("21.1.2", sha256="f8ea1baa693b61c8ad1c1d8715e59ab2b93cd3c4769bacab84afcc4279e7a70e", url="https://pypi.org/packages/cd/82/04e9aaf603fdbaecb4323b9e723f13c92c245f6ab2902195c53987848c78/pip-21.1.2-py3-none-any.whl")
    version("20.2", sha256="d75f1fc98262dabf74656245c509213a5d0f52137e40e8f8ed5cc256ddd02923", url="https://pypi.org/packages/36/74/38c2410d688ac7b48afa07d413674afc1f903c1c1f854de51dc8eb2367a5/pip-20.2-py2.py3-none-any.whl")
    version("19.3", sha256="e100a7eccf085f0720b4478d3bb838e1c179b1e128ec01c0403f84e86e0e2dfb", url="https://pypi.org/packages/4a/08/6ca123073af4ebc4c5488a5bc8a010ac57aa39ce4d3c8a931ad504de4185/pip-19.3-py2.py3-none-any.whl")
    version("19.1.1", sha256="993134f0475471b91452ca029d4390dc8f298ac63a712814f101cd1b6db46676", url="https://pypi.org/packages/5c/e0/be401c003291b56efc55aeba6a80ab790d3d4cece2778288d65323009420/pip-19.1.1-py2.py3-none-any.whl")
    version("19.0.3", sha256="bd812612bbd8ba84159d9ddc0266b7fbce712fc9bc98c82dee5750546ec8ec64", url="https://pypi.org/packages/d8/f3/413bab4ff08e1fc4828dfc59996d721917df8e8583ea85385d51125dceff/pip-19.0.3-py2.py3-none-any.whl")
    version("18.1", sha256="7909d0a0932e88ea53a7014dfd14522ffef91a464daaaf5c573343852ef98550", url="https://pypi.org/packages/c2/d7/90f34cb0d83a6c5631cf71dfe64cc1054598c843a92b400e55675cc2ac37/pip-18.1-py2.py3-none-any.whl")
    version("10.0.1", sha256="717cdffb2833be8409433a93746744b59505f42146e8d37de6c62b430e25d6d7", url="https://pypi.org/packages/0f/74/ecd13431bcc456ed390b44c8a6e917c1820365cbebcb6a8974d1cd045ab4/pip-10.0.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="690b762c0a8460c303c089d5d0be034fb15a5ea2b75bdf565f40421f542fefb0", url="https://pypi.org/packages/b6/ac/7015eb97dc749283ffdec1c3a88ddb8ae03b8fad0f0e611408f196358da3/pip-9.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@22:")
    # END DEPENDENCIES

