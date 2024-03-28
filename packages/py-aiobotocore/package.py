# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAiobotocore(PythonPackage):
    # BEGIN VERSIONS
    version("2.12.1", sha256="6a9a3d646cf422f45fdc1e4256e78563ebffba64733bc9b8ca9123614e8ba9af", url="https://pypi.org/packages/4d/be/52c4181235cad3e462ac163ae714de37d36bed291efdb4e6591fde119219/aiobotocore-2.12.1-py3-none-any.whl")
    version("2.5.0", sha256="9a2a022d7b78ec9a2af0de589916d2721cddbf96264401b78d7a73c1a1435f3b", url="https://pypi.org/packages/91/01/d04cc1e4cc29fcafbca4ca746bf33e03dd5eb51c958738596be7d76a2022/aiobotocore-2.5.0-py3-none-any.whl")
    version("2.4.2", sha256="4acd1ebe2e44be4b100aa553910bda899f6dc090b3da2bc1cf3d5de2146ed208", url="https://pypi.org/packages/90/eb/9902c7ea808d1753a4fd0d5e1a4a87e3bbd609277983c20fa7cd2e6084e5/aiobotocore-2.4.2-py3-none-any.whl")
    version("1.2.1", sha256="58cc422e65fc89f7cb78eca740d241ac8e15f39f6b308cc23152711e8a987d45", url="https://pypi.org/packages/f9/a4/6c6687571b79fe792c627b6fbc31f3437eaf255388f384b5c4853b2b781c/aiobotocore-1.2.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@3.7.4.post:3", when="@2.6:")
        depends_on("py-aiohttp@3.3.1:", when="@0.9.2:1.1,2.1.2:2.1,2.3.4:2.5.0")
        depends_on("py-aioitertools@0.5.1:", when="@0.12:1.1,2.1.2:2.1,2.3.4:")
        depends_on("py-botocore@1.34.41:1.34.51", when="@2.12:")
        depends_on("py-botocore@1.29.76", when="@2.5:2.5.0")
        depends_on("py-botocore@1.27.59", when="@2.4")
        depends_on("py-wrapt@1.10.10:", when="@0.3.2:0.8,0.9.1:1.1,2.1.2:2.1,2.3.4:")
    # END DEPENDENCIES

