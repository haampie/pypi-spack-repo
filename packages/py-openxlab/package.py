# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenxlab(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.36", sha256="79a6136f6b47d6e7e9d52da28eb331734e5d558fd1543ef2324bf16df94ba74a", url="https://pypi.org/packages/a0/c3/f09a9e24deb5b6b8083e4e9ccd4417034df7da110765f88e721e790da61a/openxlab-0.0.36-py3-none-any.whl")
    version("0.0.35", sha256="22117376cfc1456acd5ebdb19aa74aa37ae615b9795d8342ee03b5daeabdb766", url="https://pypi.org/packages/bc/ea/33bbf0f9970a4af8a84b3890f6721a829aae1ae161585616b97928c1b6c0/openxlab-0.0.35-py3-none-any.whl")
    version("0.0.34", sha256="a7c7b31713ef809af996e0091269d1afde1e38ed5087a9b6fa7d63ce0d3aafb7", url="https://pypi.org/packages/0f/02/18fe3c9931969adb640b7a6409ddb42edb94bf1f28b96aceae55f35c9f76/openxlab-0.0.34-py3-none-any.whl")
    version("0.0.33", sha256="06e3a7769b29ae0526c7605af32756cd9a098e532fd4047f0dcde7a17a65dbee", url="https://pypi.org/packages/b4/98/e248ad9a13b60649ae2fc3c31515b97f10cc3b9fb842b628430c9461aef3/openxlab-0.0.33-py3-none-any.whl")
    version("0.0.32", sha256="e8bababbd765d395a05238e2d827b8a6507bacf12fb2c7652f94454f9e9cb76e", url="https://pypi.org/packages/5b/75/090abd2708bb4590da4e9bdd14a6cf0c495d90c930c82b5de65557486216/openxlab-0.0.32-py3-none-any.whl")
    version("0.0.31", sha256="a2a33048877ab93fb24c74448be14e5d4c483b983dc1f5673c8bc37eff85bb46", url="https://pypi.org/packages/30/68/b55c7f789619a6f3c323ff4f1641182dd0c06da7898b77c7e94437abe7f6/openxlab-0.0.31-py3-none-any.whl")
    version("0.0.30", sha256="c15e13c85ce594fd56d438db4f3275245954b68abaf96ab1b5e884c5263bd8cb", url="https://pypi.org/packages/75/95/d3deace7a97e51994f408465f4f8f07f9f6f2c2fc95dfac49ff8a33b00c1/openxlab-0.0.30-py3-none-any.whl")
    version("0.0.29", sha256="463e2c8ff16c41d9e4268e3d00f2c853053718ff062cda2a7ed20a7fbecd0fa3", url="https://pypi.org/packages/3a/76/7d97f6695c76dbed4aa4662c6f350edeb6e5e84b89bb71b803cd294bceb1/openxlab-0.0.29-py3-none-any.whl")
    version("0.0.28", sha256="e462a3c0de20def279bfb2cf899522a6020a96c7324b4ba738f706e7b06f1376", url="https://pypi.org/packages/74/10/7764d31a9745ab24b7c8054b7c8f1e8a0ee09e68eaaba329b19696215c76/openxlab-0.0.28-py3-none-any.whl")
    version("0.0.27", sha256="8c70b0ed865e3b84167476102a9d9a54837126f096d368e7a78c0fbde2ae385c", url="https://pypi.org/packages/5a/f8/8d50e7b957346b8141584736d555af77162a846bc12916f107f3d1f31bf1/openxlab-0.0.27-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-oss2@2.17", when="@0.0.9:0.0.10,0.0.12:")
        depends_on("py-pytz@2023.3:2023", when="@0.0.9:0.0.10,0.0.12:")
        depends_on("py-pyyaml@6.0:", when="@0.0.3:0.0.10,0.0.12:")
        depends_on("py-requests@2.28.2:2.28", when="@0.0.2:0.0.10,0.0.12:")
        depends_on("py-rich@13.4.2:13.4", when="@0.0.12:")
        depends_on("py-setuptools@60.2", when="@0.0.2:0.0.6,0.0.9:0.0.10,0.0.12:")
        depends_on("py-tqdm@4.65", when="@0.0.2:0.0.10,0.0.12:")
    # END DEPENDENCIES

