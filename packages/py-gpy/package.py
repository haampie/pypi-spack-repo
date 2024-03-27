##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGpy(PythonPackage):
    version("1.10.0", sha256="a2b793ef8d0ac71739e7ba1c203bc8a5afa191058b42caa617e0e29aa52aa6fb", url="https://pypi.org/packages/ce/4a/43d6f07b8b493bc216ecf1d5c447809e8c9d0b1b18b0b9db496dfadd87ea/GPy-1.10.0.tar.gz")
    version("1.9.9", sha256="04faf0c24eacc4dea60727c50a48a07ddf9b5751a3b73c382105e2a31657c7ed", url="https://pypi.org/packages/67/95/976598f98adbfa918a480cb2d643f93fb555ca5b6c5614f76b69678114c1/GPy-1.9.9.tar.gz")
    version("0.8.8", sha256="e135d928cf170e2ec7fb058a035b5a7e334dc6b84d0bfb981556782528341988", url="https://pypi.org/packages/0a/f1/33da69f4df7d69cef5e7ac5241d1d418c7ce2291744e1f7ae673d7ad1635/GPy-0.8.8.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.13:")
        depends_on("py-numpy@1.7:", when="@1.0.1:1.0.6,1.2:1.8.3,1.8.5:1.9")
        depends_on("py-paramz@0.9:", when="@1.9")
        depends_on("py-scipy@0.16:", when="@1.0.1:1.0.6,1.2:1.8.3,1.8.5:1.9")
        depends_on("py-six", when="@1.0.1:1.0.6,1.2:1.8.3,1.8.5:1.9")

