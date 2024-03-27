##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTiktoken(PythonPackage):
    version("0.6.0", sha256="ace62a4ede83c75b0374a2ddfa4b76903cf483e9cb06247f566be3bf14e6beed", url="https://pypi.org/packages/3a/7b/a8f49a8fb3f7dd70c77ab1d90b0514ab534db43cbcf8ac0a7ece57c64d87/tiktoken-0.6.0.tar.gz")
    version("0.5.2", sha256="f54c581f134a8ea96ce2023ab221d4d4d81ab614efa0b2fbce926387deb56c80", url="https://pypi.org/packages/a7/e8/0dc09862a2a7dddbd8578dbde80cff77a2efec8ecf476eaeab1dc75dffac/tiktoken-0.5.2.tar.gz")
    version("0.5.1", sha256="27e773564232004f4f810fd1f85236673ec3a56ed7f1206fc9ed8670ebedb97a", url="https://pypi.org/packages/bd/ef/91777d3310589c55da4bf0fafa10fdc8ddefa30aa7dfa67b2fc8825bc1f1/tiktoken-0.5.1.tar.gz")
    version("0.5.0", sha256="c8dfd3280f5fca0d8ed2ec18c0f11f7cba305af48faaf4b914c71b7d221f39ed", url="https://pypi.org/packages/a7/92/4a48603fc2ad535a50fbf4471fb5014ce6e13b3acd0959ce4384ccb58262/tiktoken-0.5.0.tar.gz")
    version("0.4.0", sha256="59b20a819969735b48161ced9b92f05dc4519c17be4015cfb73b65270a243620", url="https://pypi.org/packages/9f/88/77a86f915a81449156375b7538c94105a34bebf00838462c9d3fced490e9/tiktoken-0.4.0.tar.gz")
    version("0.3.3", sha256="97b58b7bfda945791ec855e53d166e8ec20c6378942b93851a6c919ddf9d0496", url="https://pypi.org/packages/8e/3a/20704b89b271cfebb1c981ef9f172fb18cb879b5c5cfc3b209083f71b229/tiktoken-0.3.3.tar.gz")
    version("0.3.2", sha256="a51b5449e883e409cf2f4a846a6a97962d5656a354a5532c330811c833ac3b37", url="https://pypi.org/packages/91/ed/c6596b42188c03b671ea4d8b6912c1f280ac2991664235039d3a18069d6a/tiktoken-0.3.2.tar.gz")
    version("0.3.1", sha256="8295912429374f5f3c6c6bf053a091ce1de8c1792a62e3b30d4ad36f47fa8b52", url="https://pypi.org/packages/fb/d9/c38fee002c5979f29c182aee8e28c31538eabf40022e304f97ff82324199/tiktoken-0.3.1.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.1.1")
        depends_on("py-regex@2022:", when="@0.5:")
        depends_on("py-requests@2.26:", when="@0.5:")

