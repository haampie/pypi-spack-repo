##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAgate(PythonPackage):
    version("1.9.1", sha256="1cf329510b3dde07c4ad1740b7587c9c679abc3dcd92bb1107eabc10c2e03c50", url="https://pypi.org/packages/d1/53/89b197cb472a3175d73384761a3413fd58e6b65a794c1102d148b8de87bd/agate-1.9.1-py2.py3-none-any.whl")
    version("1.9.0", sha256="7421257311d6e6a41462949cd643fd0ac2a061ac1ee9d7df72b0f9d03452a19c", url="https://pypi.org/packages/9d/37/d20ef28bcbfa56484a519a1314b1d821138d17d7296de5928f59bec408ca/agate-1.9.0-py2.py3-none-any.whl")
    version("1.8.0", sha256="89bdd92369d335be7aec53a1c6517b89c9665ca3d68d05cb223ec3a0d8a09b0d", url="https://pypi.org/packages/ed/50/ff4cb8e8f5f7eb75687e4703e79564fb3dde6bdefa01f9ac94e5f5b11156/agate-1.8.0-py2.py3-none-any.whl")
    version("1.7.1", sha256="23f9f412f74f97b72f82b1525ab235cc816bc8c8525d968a091576a0dbc54a5f", url="https://pypi.org/packages/20/6e/bbebad0213fce2081902cf7565322b42a5a991c550857cfbb4741f69b8f6/agate-1.7.1-py2.py3-none-any.whl")
    version("1.7.0", sha256="ad529c80fe6943906ab3d3bc59c12307e1181d35993e6055db59fa72dc79a6bd", url="https://pypi.org/packages/a8/ea/69637dc96ded12c43d0b058548f75d707bf7dbb867e0aabe865dd432d29c/agate-1.7.0-py2.py3-none-any.whl")
    version("1.6.3", sha256="2d568fd68a8eb8b56c805a1299ba4bc30ca0434563be1bea309c9d1c1c8401f4", url="https://pypi.org/packages/90/95/6e3fe3ddcc64e5f7de7fd7cd14c26a588aeaa7aea2d58a3bb61a150cebd9/agate-1.6.3-py2.py3-none-any.whl")
    version("1.6.2", sha256="8dbd4a57a2cffecfa2d8109ef5993ec4be12a8a7c81fbc0c8c79d96d4c4399ed", url="https://pypi.org/packages/da/ec/73bf438732d6e38b380fab9e4dcdfa2b227a984e50c3b56cc9a128fbae9b/agate-1.6.2.tar.gz")
    version("1.6.1", sha256="c93aaa500b439d71e4a5cf088d0006d2ce2c76f1950960c8843114e5f361dfd3", url="https://pypi.org/packages/d4/1c/99fb34c81c68012c71e8d35a1f16a6b25952322e23c911c81327c8464be8/agate-1.6.1.tar.gz")
    version("1.6.0", sha256="1547eb66a4caaea08cc247077e5b3740629be6724a047c94be0ecbbfa52ceb0a", url="https://pypi.org/packages/72/37/48192f2cb18c7ebe413f7410783b64a6236d20a4461f5c36f5efcb793f89/agate-1.6.0.tar.gz")
    version("1.5.5", sha256="2861da5ef44a442a2225f0945a8ddce67ba4653622bf55b22f793a7b7fd95265", url="https://pypi.org/packages/97/0e/94c67e9a788c5bb5a83b8a46ac7b2a59ae627af93e4e3fb16dd4cfbae591/agate-1.5.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-babel@2:", when="@1.6.3:")
        depends_on("py-isodate@0.5.4:", when="@1.6.3:")
        depends_on("py-leather@0.3.2:", when="@1.6.3:")
        depends_on("py-parsedatetime@2.1:2.4,2.6:", when="@1.7.1:")
        depends_on("py-parsedatetime@2.1:2.4", when="@1.6.3:1.7.0")
        depends_on("py-python-slugify@1.2.1:", when="@1.6.3:")
        depends_on("py-pytimeparse@1.1.5:", when="@1.6.3:")
        depends_on("py-six@1.9:", when="@1.6.3:1.6")
        depends_on("py-tzdata@2023.3:", when="@1.8: platform=windows")

