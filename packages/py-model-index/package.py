##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyModelIndex(PythonPackage):
    version("0.1.11", sha256="a2a4d4431cd44e571d31e223cc4b0432663a62689de453bdb666e56a514b0e07", url="https://pypi.org/packages/0f/a6/4d4cbbef704f186d143e2859296a610a355992e4eae71582bd598093b36a/model_index-0.1.11-py3-none-any.whl")
    version("0.1.10", sha256="f5e0cd14904e73ed5c98e3d01b357bb1b091049d092f74f799915e1c4a7af928", url="https://pypi.org/packages/43/a2/dfaff5269ffca0c0b4840df59ef7d308129686bb175c9ec406d5ff52f0d8/model_index-0.1.10-py3-none-any.whl")
    version("0.1.9", sha256="a6aff0e16e77fd6110d85e4189fef6fcfa0c85e11daf5e73cea7a94007f9d777", url="https://pypi.org/packages/16/f9/f157948c396863629fa7c9772923dcbfc59c38d58187345d45cf9846789c/model_index-0.1.9-py3-none-any.whl")
    version("0.1.8", sha256="1e6e18ba4743248f9751b7e4fbffcc45b698f4add701461329526187e3aba69a", url="https://pypi.org/packages/a8/82/ad6152d6e1f6bb132bf9bea7e09bb13d65c8fb57ed5d25b75fd661c34141/model_index-0.1.8-py3-none-any.whl")
    version("0.1.7", sha256="027d7f2f331b861570ab78c131afbfc742027714652d212c81b44e845f3a2753", url="https://pypi.org/packages/6c/59/83e76aa82c60e769f56751d0fe93576ce471f2e23e9e78ae858a3fc62383/model_index-0.1.7-py3-none-any.whl")
    version("0.1.6", sha256="80cf7cb98ae32980c5bd6eae2304210c5dffc923bc71d262748ac383a781d3a2", url="https://pypi.org/packages/b0/e3/a4b632a6805ab5edfc34aee0c1ad908cefc94436b5a007fada6f124d1895/model_index-0.1.6-py3-none-any.whl")
    version("0.1.4", sha256="47808a434a23e2733f06e6afdf1809e404d8875a1cdbbf66ebd8fa4529b19d6a", url="https://pypi.org/packages/5d/8d/5146c6c22d4b4d8a7dd867dec1d443fedc12d1df21c4f081fa358f80ed72/model_index-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="2cedee7ed29986c24aa42adba5d22b67532cacb9be44c74166308dd41f505142", url="https://pypi.org/packages/7d/50/7b1e895e3b941c8f46e7b74e914fa90aaa09996053e5a363da0dbf7016e9/model_index-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="68db0787ec769e397dfceb1da81d79b235ca3c6a957bc41ce64a536f978393a4", url="https://pypi.org/packages/5a/35/df2608b50267286d578adf384ff538bf1146e8a2c4c1354f875577cc9690/model_index-0.1.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-click")
        depends_on("py-markdown")
        depends_on("py-ordered-set")
        depends_on("py-pyyaml")

