# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLlvmlite(PythonPackage):
    # BEGIN VERSIONS
    version("0.42.0", sha256="f92b09243c0cc3f457da8b983f67bd8e1295d0f5b3746c7a1861d7a99403854a", url="https://pypi.org/packages/3b/ff/ad02ffee7d519615726fc46c99a37e697f2b4b1fb7e5d3cd6fb465d4f49f/llvmlite-0.42.0.tar.gz")
    version("0.42.0-rc1", sha256="01a057fc242bbd875cb44b373538c50172e09bf6cf559da12eb48197a7f4b116", url="https://pypi.org/packages/fa/82/52d7d0ed04bf20736e475a88b40f89037c911aa9b61082007976b8dd7739/llvmlite-0.42.0rc1.tar.gz")
    version("0.41.1", sha256="f19f767a018e6ec89608e1f6b13348fa2fcde657151137cb64e56d48598a92db", url="https://pypi.org/packages/01/c6/bc6634da9f58edf91a1a002280c6380f404715245a49a46234b1d9d9585a/llvmlite-0.41.1.tar.gz")
    version("0.41.0", sha256="7d41db345d76d2dfa31871178ce0d8e9fd8aa015aa1b7d4dab84b5cb393901e0", url="https://pypi.org/packages/99/46/cd194dacca2704fb13f6d156727ca233c911a6229c0bf1cd4f3af4f56c04/llvmlite-0.41.0.tar.gz")
    version("0.40.1", sha256="5cdb0d45df602099d833d50bd9e81353a5e036242d3c003c5b294fc61d1986b4", url="https://pypi.org/packages/95/e0/369f1c0613c9532319ed3307f4289afc8338d3bf71c1875fdf43603a2d19/llvmlite-0.40.1.tar.gz")
    version("0.40.0", sha256="c910b8fbfd67b8e9d0b10ebc012b23cd67cbecef1b96f00d391ddd298d71671c", url="https://pypi.org/packages/30/2c/9ab0b7d5825a2ea1b6a941158a19de176938510c1cbba08ef8436333f72c/llvmlite-0.40.0.tar.gz")
    version("0.39.1", sha256="b43abd7c82e805261c425d50335be9a6c4f84264e34d6d6e475207300005d572", url="https://pypi.org/packages/14/27/1468111538f33bd9fb13c0b2c1534c7a487cec8fadf14e318d73be18e4e1/llvmlite-0.39.1.tar.gz")
    version("0.39.0", sha256="01098be54f1aa25e391cebba8ea71cd1533f8cd1f50e34c7dd7540c2560a93af", url="https://pypi.org/packages/48/fc/4d5aa9688b0b06fb77a8b61f10bf252fba483b23f542de2d7c440989b80c/llvmlite-0.39.0.tar.gz")
    version("0.38.1", sha256="0622a86301fcf81cc50d7ed5b4bebe992c030580d413a8443b328ed4f4d82561", url="https://pypi.org/packages/90/fc/313c916fb49495ac7c1f9ab213cd3d3285342691b860a2810a51c6c1a10e/llvmlite-0.38.1.tar.gz")
    version("0.38.0", sha256="a99d166ccf3b116f3b9ed23b9b70ba2415640a9c978f3aaa13fad49c58f4965c", url="https://pypi.org/packages/d8/e3/bd329a96549809598acd5daaccd35fd9d0883185cfe7f681a9e3e54beaa0/llvmlite-0.38.0.tar.gz")
    version("0.37.0", sha256="6392b870cd018ec0c645d6bbb918d6aa0eeca8c62674baaee30862d6b6865b15", url="https://pypi.org/packages/55/21/f7df5d35f3f5d0637d64a89f6b0461f2adf78e22916d6372486f8fc2193d/llvmlite-0.37.0.tar.gz")
    version("0.34.0", sha256="f03ee0d19bca8f2fe922bb424a909d05c28411983b0c2bc58b020032a0d11f63", url="https://pypi.org/packages/0b/96/07bfa93a103fb9e3e9ae7f9f7c6687ae714aee66b6f3000da3fad71e0aa2/llvmlite-0.34.0.tar.gz")
    version("0.33.0", sha256="9c8aae96f7fba10d9ac864b443d1e8c7ee4765c31569a2b201b3d0b67d8fc596", url="https://pypi.org/packages/71/4e/b1086722f4fa0b52cf8c0d4b2c985fb3f95d2f1be1b010259497b2464c1d/llvmlite-0.33.0.tar.gz")
    version("0.33.0-rc1", sha256="779d915f38b9034086ad97ddaf229295978996eb6eaae47ef4947ea370db51fb", url="https://pypi.org/packages/07/bb/73bc720db386c30156bdea83bd7aa13f4cf52b251bb51ff08d60e38ccf19/llvmlite-0.33.0rc1.tar.gz")
    version("0.32.1", sha256="41262a47b8cbba5a09203b15b65fbdf11192f92aa226c81e99115acdee8f3b8d", url="https://pypi.org/packages/50/cc/04526507e80d546be5688ce0246e40277b61e7949c3347c6609b6a4154cf/llvmlite-0.32.1.tar.gz")
    version("0.32.0", sha256="d65c645c32fae7b50852e80597eaef8369f826b75017d5c8d07c800e37eaed89", url="https://pypi.org/packages/dc/8f/5c6d0e8be1585247c4fd33b84dc66d1fa6449b77d27f42a51d45242307c9/llvmlite-0.32.0.tar.gz")
    version("0.31.0", sha256="22ab2b9d7ec79fab66ac8b3d2133347de86addc2e2df1b3793e523ac84baa3c8", url="https://pypi.org/packages/17/fc/da81203725cb22d53e4f819374043bbfe3327831f3cb4388a3c020d7a497/llvmlite-0.31.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.42:")
        depends_on("python@:3.10", when="@0.38")
        depends_on("python@:3.9", when="@0.36.0-rc2:0.37")
    # END DEPENDENCIES

