# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFenicsFiat(PythonPackage):
    # BEGIN VERSIONS
    version("2019.1.0", sha256="6bf99374ed320017f853a573a21fe31763cba14b9c0459f4000edb12f83731ba", url="https://pypi.org/packages/05/54/e463570ef224ca199c2baf0b77f10b8de44ce9b40374c0fc229d108e6c26/fenics_fiat-2019.1.0-py3-none-any.whl")
    version("2018.1.0", sha256="b97aa09d3dd9bbc04c23247d91587d3072b736b96af1058e39e2ce44b654f911", url="https://pypi.org/packages/3f/fe/d1f86aab439678c204b61d5d4b9f6a36009493dcc31f9ae2061a828c3a5e/fenics_fiat-2018.1.0-py3-none-any.whl")
    version("2017.2.0", sha256="a5afaecca1287be5774017601615d1bedb5cd8328a37926f38eb676b56715277", url="https://pypi.org/packages/60/43/9bbb3fd2f47732ec9d7760bd8b907c3587c43eaf222ecb99d6ed8aa21172/fenics-fiat-2017.2.0.tar.gz")
    version("2017.1.0.post1", sha256="4ceace13762eae6f5748bfc146bf6c8f5c5ac4a0c5320d8d136cef5fcd12fdbd", url="https://pypi.org/packages/bc/09/14695e8aaeadbbded3a7198755e5f6befd96207a566f38960fbeeac31c1f/fenics-fiat-2017.1.0.post1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@2018:")
        depends_on("py-sympy", when="@2018:")
    # END DEPENDENCIES

