# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonGitlab(PythonPackage):
    # BEGIN VERSIONS
    version("3.15.0", sha256="8f8d1c0d387f642eb1ac7bf5e8e0cd8b3dd49c6f34170cee3c7deb7d384611f3", url="https://pypi.org/packages/38/51/3c7dd08272658e5490d0c0b6c94af15bd0c0649e7ad23c9ed0db1d276143/python_gitlab-3.15.0-py3-none-any.whl")
    version("3.9.0", sha256="ce941f99bf88b6918eea82500ca6206806117f4afe26d4705f4ded2284b35c69", url="https://pypi.org/packages/ea/67/1b00b2fe6942a1c388a40462455f8bb05ab01f5c8b8417186cfcfd523b6c/python_gitlab-3.9.0-py3-none-any.whl")
    version("2.10.1", sha256="581a219759515513ea9399e936ed7137437cfb681f52d2641626685c492c999d", url="https://pypi.org/packages/1b/90/eed6dd7eda176cb6e7300e27f9f7f94ac917df9dc1bb1553924af271f01a/python_gitlab-2.10.1-py3-none-any.whl")
    version("1.8.0", sha256="a6b03bc53f6e2e22b88d5ff9772b1bb360570ec82752f1def3d6eb60cda093e7", url="https://pypi.org/packages/e4/79/7cccb27a38e866a8bb16f7780c96a20d1744d8f2b9d900b60ad31447d569/python-gitlab-1.8.0.tar.gz")
    version("0.19", sha256="88b65591db7a10a0d9979797e4e654a113e2b93b3a559309f6092b27ab93934a", url="https://pypi.org/packages/7e/b5/61d3b2176fac8eda67f10da6407884103d78f5cb5eb04001c2d947ec6717/python-gitlab-0.19.tar.gz")
    version("0.18", sha256="d60d67c82fedd8c3e4f0bb8b5241bf2df32307c98fdf2f02a94850e21db2d804", url="https://pypi.org/packages/35/1a/b78fcf198d55d4eed08b3980d3eec0dd88b419a960c023cbbc8f33be7962/python-gitlab-0.18.tar.gz")
    version("0.17", sha256="f79337cd8b2343195b7ac0909e0483624d4235cca78fc76196a0ee4e109c9a70", url="https://pypi.org/packages/e9/fa/912c190310afbefef565d315ffc30fd8fbbdd86be419945c69d7450c26b1/python-gitlab-0.17.tar.gz")
    version("0.16", sha256="2c50dc0bd3ed7c6b1edb6e556b0f0109493ae9dfa46e3bffcf3e5e67228d7d53", url="https://pypi.org/packages/f4/b9/88e6550bc2d7c7d9d24a76b87b16d6701826c53c45489b1d05da702250d7/python-gitlab-0.16.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@3")
        depends_on("py-requests@2.25:", when="@2.10.1:")
        depends_on("py-requests@2.4.2:", when="@1.8:1")
        depends_on("py-requests-toolbelt@0.10.1:", when="@3.13:")
        depends_on("py-requests-toolbelt@0.9.1:", when="@2.6:3.12")
        depends_on("py-six", when="@1.8:1")
        depends_on("py-typing-extensions@4:", when="@3.14:3 ^python@:3.7")
    # END DEPENDENCIES

