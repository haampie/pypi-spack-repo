# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTokenizers(PythonPackage):
    # BEGIN VERSIONS
    version("0.15.0", sha256="10c7e6e7b4cabd757da59e93f5f8d1126291d16f8b54f28510825ef56a3e5d0e", url="https://pypi.org/packages/9f/17/1df113d77dab378cb02fcee438893610e055621d3994b51d5ffe315170e4/tokenizers-0.15.0.tar.gz")
    version("0.13.3", sha256="2e546dbb68b623008a5442353137fbb0123d311a6d7ba52f2667c8862a75af2e", url="https://pypi.org/packages/29/9c/936ebad6dd963616189d6362f4c2c03a0314cf2a221ba15e48dd714d29cf/tokenizers-0.13.3.tar.gz")
    version("0.13.1", sha256="3333d1cee5c8f47c96362ea0abc1f81c77c9b92c6c3d11cbf1d01985f0d5cf1d", url="https://pypi.org/packages/3d/66/5296f3610be7a4aaefa0b602351f63115f3945f725b5e37c2634c578a293/tokenizers-0.13.1.tar.gz")
    version("0.10.3", sha256="1a5d3b596c6d3a237e1ad7f46c472d467b0246be7fd1a364f12576eb8db8f7e6", url="https://pypi.org/packages/48/2b/b99184cacb1a743edc18290e9127d1b0e658c0c46f2ab5290b27fe865ff4/tokenizers-0.10.3.tar.gz")
    version("0.6.0", sha256="1da11fbfb4f73be695bed0d655576097d09a137a16dceab2f66399716afaffac", url="https://pypi.org/packages/42/82/71bbc4eff999a3e397373b9ccb43f82dad7d6d0865f2ce858d09add2dca6/tokenizers-0.6.0.tar.gz")
    version("0.5.2", sha256="b5a235f9c71d04d4925df6c4fa13b13f1d03f9b7ac302b89f8120790c4f742bc", url="https://pypi.org/packages/f5/d7/a3882b2d36991f613b749fc5e305cccc345ec9d6ab0621ad7e7bf1be8691/tokenizers-0.5.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.14:")
        depends_on("py-huggingface-hub@0.16.4:", when="@0.15:")
    # END DEPENDENCIES

