##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFenicsUfl(PythonPackage):
    version("2023.2.0", sha256="5965f5c393622f3ca8f073d86b1b5cf6492a2cd1ca1568b5e3d9f589d6baf97c", url="https://pypi.org/packages/a5/e3/de52e710c31e3a8b6dcfe5b91904a194341eac8677b8ddce486e683fb662/fenics_ufl-2023.2.0-py3-none-any.whl")
    version("2023.1.1.post0", sha256="4fb09b26f93fef663409054cd455ed2360b97ec96be11cae45a39cf2c9f3597c", url="https://pypi.org/packages/5f/c5/513129e2760cfb86c63c85ac2beb80073420d48b9745cdaaaf601315b8b7/fenics_ufl-2023.1.1.post0-py3-none-any.whl")
    version("2023.1.0", sha256="459e1c7e2268d679dc54316411fe0e6ae9b264e65ff52786cbbbb5ba61585a4f", url="https://pypi.org/packages/a6/c3/6df0cfc0e5f7ff1d03e89740f82f4b651d331e7ccfcb2522ea8c497a513a/fenics_ufl-2023.1.0-py3-none-any.whl")
    version("2022.2.0", sha256="46361202ec0d62c84560f5a4358f79cebd86e78a5c0842b4a29ef05e8958b8b8", url="https://pypi.org/packages/3b/d2/aa6a6f45ebf0612609693ef41214d7b6111d65eeb5409c0dd2dbf8a056c3/fenics_ufl-2022.2.0-py3-none-any.whl")
    version("2022.1.0.post0", sha256="337e3d6f6efbdd39d4d7eacd0b5d9e29f418f3138b1024ec7c7682ffcfc52b6f", url="https://pypi.org/packages/d0/4c/f97d735582cedf4e7794f11ec4fa7c4a495d26999da975fb14afb07f6de6/fenics_ufl-2022.1.0.post0-py3-none-any.whl")
    version("2019.1.0", sha256="a7de887a71c1643494ab84af67d837f8e0210f64fcf7ef7fc7309c25a0990d9c", url="https://pypi.org/packages/59/cd/e102c234b8be3bcff5395c555182caf2d1662e24e0417b0005e5f05ec33c/fenics_ufl-2019.1.0-py3-none-any.whl")
    version("2018.1.0", sha256="20d7b0ee7cf8d9458fd15f84ea7c800415e2801f1bd3b63ac926f1bedc8ed509", url="https://pypi.org/packages/52/7e/e59fb844975c1df32b376e3b7ddd9e7a001ca99d83a02f01c451c37405a8/fenics_ufl-2018.1.0-py3-none-any.whl")
    version("2017.2.0", sha256="743f5aca78c28b31245ec17c3eb0b6c39ed05152f2f2bf4b253cffdfb06946bb", url="https://pypi.org/packages/e1/ae/4b4f0823f4ae8eeb67b455c94e35edb49fe57c6edaedd5d220d9888c6500/fenics-ufl-2017.2.0.tar.gz")
    version("2017.1.0.post1", sha256="708fc63cfc4e7e0d51e41b0f5eb8f1b3de58729e7059572036e012c650005bfb", url="https://pypi.org/packages/23/82/56eb9b1a28c0ef5e7b70a948ee55c880728b3d00e94722ca25acb864e68a/fenics-ufl-2017.1.0.post1.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@2018:")

