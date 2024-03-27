##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnyio(PythonPackage):
    version("4.3.0", sha256="048e05d0f6caeed70d731f3db756d35dcc1f35747c8c403364a8332c630441b8", url="https://pypi.org/packages/14/fd/2f20c40b45e4fb4324834aea24bd4afdf1143390242c0b33774da0e2e34f/anyio-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="745843b39e829e108e518c489b31dc757de7d2131d53fac32bd8df268227bfee", url="https://pypi.org/packages/bf/cd/d6d9bb1dadf73e7af02d18225cbd2c93f8552e13130484f1c8dcfece292b/anyio-4.2.0-py3-none-any.whl")
    version("4.1.0", sha256="56a415fbc462291813a94528a779597226619c8e78af7de0507333f700011e5f", url="https://pypi.org/packages/85/4f/d010eca6914703d8e6be222165d02c3e708ed909cdb2b7af3743667f302e/anyio-4.1.0-py3-none-any.whl")
    version("4.0.0", sha256="cfdb2b588b9fc25ede96d8db56ed50848b0b649dca3dd1df0b11f683bb9e0b5f", url="https://pypi.org/packages/36/55/ad4de788d84a630656ece71059665e01ca793c04294c463fd84132f40fe6/anyio-4.0.0-py3-none-any.whl")
    version("3.7.1", sha256="91dee416e570e92c64041bd18b900d1d6fa78dff7048769ce5ac5ddad004fbb5", url="https://pypi.org/packages/19/24/44299477fe7dcc9cb58d0a57d5a7588d6af2ff403fdd2d47a246c91a3246/anyio-3.7.1-py3-none-any.whl")
    version("3.7.0", sha256="eddca883c4175f14df8aedce21054bfca3adb70ffe76a9f607aef9d7fa2ea7f0", url="https://pypi.org/packages/68/fe/7ce1926952c8a403b35029e194555558514b365ad77d75125f521a2bec62/anyio-3.7.0-py3-none-any.whl")
    version("3.6.2", sha256="fbbe32bd270d2a2ef3ed1c5d45041250284e31fc0a4df4a5a6071842051a51e3", url="https://pypi.org/packages/77/2b/b4c0b7a3f3d61adb1a1e0b78f90a94e2b6162a043880704b7437ef297cad/anyio-3.6.2-py3-none-any.whl")
    version("3.6.1", sha256="cb29b9c70620506a9a8f87a309591713446953302d7d995344d0d7c6c0c9a7be", url="https://pypi.org/packages/c3/22/4cba7e1b4f45ffbefd2ca817a6800ba1c671c26f288d7705f20289872012/anyio-3.6.1-py3-none-any.whl")
    version("3.6.0", sha256="5bd42d66c9c382e657c9acba60f9459d747c192513e76dcae8b1c611e55174ef", url="https://pypi.org/packages/f4/17/86c924b1371353f785e1515b830e118fcd46880ae8d7a7b11116e5f81d6f/anyio-3.6.0-py3-none-any.whl")
    version("3.5.0", sha256="b5fa16c5ff93fa1046f2eeb5bbff2dad4d3514d6cda61d02816dba34fa8c3c2e", url="https://pypi.org/packages/b1/ae/9a8af72d6f0c551943903eefcf93c3a29898fb7b594603c0d70679c199b1/anyio-3.5.0-py3-none-any.whl")
    version("3.4.0", sha256="2855a9423524abcdd652d942f8932fda1735210f77a6b392eafd9ff34d3fe020", url="https://pypi.org/packages/ad/0a/919c040f061bc31f604ee8275ada8fa9f6f237425010afa523e429a04a45/anyio-3.4.0-py3-none-any.whl")
    version("3.3.4", sha256="4fd09a25ab7fa01d34512b7249e366cd10358cdafc95022c7ff8c8f8a5026d66", url="https://pypi.org/packages/e6/bc/832d33ddcf7bcfdfa73cd1780847726dee4581adac9d4ca975feb8e7662c/anyio-3.3.4-py3-none-any.whl")
    version("3.3.3", sha256="56ceaeed2877723578b1341f4f68c29081db189cfb40a97d1922b9513f6d7db6", url="https://pypi.org/packages/a9/9a/36fca955726d572827b0f8b039a544311c362b55868fbc265bac7455e166/anyio-3.3.3-py3-none-any.whl")
    version("3.3.2", sha256="c32da314c510b34a862f5afeaf8a446ffed2c2fde21583e654bd71ecfb5b744b", url="https://pypi.org/packages/89/c7/76b61d971bd463ed32d093c61a70d757a8edd7f7baaec0bdabc64ed9f376/anyio-3.3.2-py3-none-any.whl")
    version("3.2.1", sha256="442678a3c7e1cdcdbc37dcfe4527aa851b1b0c9162653b516e9f509821691d50", url="https://pypi.org/packages/5a/8c/6712b0aebe9b250736ec5dde99883b143290b49ecc2310eb583577e316aa/anyio-3.2.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-exceptiongroup@1.0.2:", when="@4: ^python@:3.10")
        depends_on("py-exceptiongroup", when="@3.7:3 ^python@:3.10")
        depends_on("py-idna@2.8:", when="@1.4:")
        depends_on("py-sniffio@1.1:", when="@1.0.0-rc2:")
        depends_on("py-typing-extensions@4.1:", when="@4.2: ^python@:3.10")

