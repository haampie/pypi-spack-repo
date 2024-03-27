##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySwaggerSpecValidator(PythonPackage):
    version("3.0.3", sha256="174b5de4ab0899df9a57d35c880aaa515511c4b8b578d9d519b09a9596537055", url="https://pypi.org/packages/ba/1f/bb111cbe837e3dde18aab6324379e0ec9f5fe5aa3f623f20ff8a705b36fd/swagger_spec_validator-3.0.3-py2.py3-none-any.whl")
    version("3.0.2", sha256="bf3af74e7e76539d89a44fd010f1e6edbf3e12df964bebbe73b8804cf2b0f1ff", url="https://pypi.org/packages/5c/0e/8b9a48c472891b35632a1c35252dbd7bcf688a6bd6436b75d22cd4356a8b/swagger_spec_validator-3.0.2-py2.py3-none-any.whl")
    version("3.0.1", sha256="5691531c9b692fa41eeb1c3d2e088f0ff3d5bdb40cc6e08995a625dea8f2ca5f", url="https://pypi.org/packages/a9/1b/fcaf974fe16a1c742622fbd1b92211d9b1555190ae060fa3eec321c7e4e2/swagger_spec_validator-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="84811dddd28c6c30f7ea3440d8ea9977e390667853cf2135accaf57289659a1e", url="https://pypi.org/packages/40/ed/e7725748ac87313c27776def7b75fcac703c8ea3c207fa4590a801f02de2/swagger_spec_validator-3.0.0-py2.py3-none-any.whl")
    version("2.7.6", sha256="ff55d671f4cf8a386e7ecda60267d6cdd2cfbe0b3521a8ccf09b0669cbb72ab6", url="https://pypi.org/packages/5b/0f/d7f6a7f610487a25583db19d2ce2808ad8be356e0067b4f2758d076af8a5/swagger_spec_validator-2.7.6-py2.py3-none-any.whl")
    version("2.7.5", sha256="f0d4e6e67475db4b92fdfa928907a092666c22b60e95b1902dd5150a2d46a51e", url="https://pypi.org/packages/6e/ca/e34dcbcfdaeac636facbf5035bce2a48d9ed3a89a1c121fc4b39b582d69b/swagger_spec_validator-2.7.5-py2.py3-none-any.whl")
    version("2.7.4", sha256="4e373a4db5262e7257fde17d84c5c0178327b8057985ab1be63f580bfa009855", url="https://pypi.org/packages/71/81/ffaceaa8da1a40f8c807382ffa705b15d293cac551b662586d4dea7ebeed/swagger_spec_validator-2.7.4-py2.py3-none-any.whl")
    version("2.7.3", sha256="d1514ec7e3c058c701f27cc74f85ceb876d6418c9db57786b9c54085ed5e29eb", url="https://pypi.org/packages/09/de/e78cefbf5838b434b63a789264b79821cb2267f1498fbed23ef8590133e4/swagger_spec_validator-2.7.3-py2.py3-none-any.whl")
    version("2.7.2", sha256="b651f881d718b0e3e867f19151bb47f7a50da611f285262f4d4aea092998347c", url="https://pypi.org/packages/39/c4/339a8d7a6a431ea3447fd0cee45d8570247cd19e29443be87748b0225909/swagger_spec_validator-2.7.2-py2.py3-none-any.whl")
    version("2.7.1", sha256="e7c928ffe676054358699f2559d665257b40f0165e7bd5f7d17f278148871115", url="https://pypi.org/packages/82/4e/89036e8d5b94c5c38b5e6305bb9ba587e8490180a8127f4e9f34427a4888/swagger_spec_validator-2.7.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jsonschema@:3", when="@2.7.5")
        depends_on("py-jsonschema", when="@1.0.12:1.0,1.1.1:2.0.2,2.2:2.7.4,2.7.6:")
        depends_on("py-pyyaml", when="@2.2:")
        depends_on("py-six", when="@1.0.12:1.0,1.1.1:2.0.2,2.2:2")
        depends_on("py-typing-extensions", when="@3.0.3:")

