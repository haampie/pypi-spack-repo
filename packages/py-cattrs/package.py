##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCattrs(PythonPackage):
    version("23.2.3", sha256="0341994d94971052e9ee70662542699a3162ea1e0c62f7ce1b4a57f563685108", url="https://pypi.org/packages/b3/0d/cd4a4071c7f38385dc5ba91286723b4d1090b87815db48216212c6c6c30e/cattrs-23.2.3-py3-none-any.whl")
    version("23.2.2", sha256="66064e2060ea207c5a48d065ab1910c10bb8108c28f3df8d1a7b1aa6b19d191b", url="https://pypi.org/packages/23/da/2079794bebf663eb20e1c4974a0502c9486e2f3ec9b68631cd98227e4d5c/cattrs-23.2.2-py3-none-any.whl")
    version("23.2.1", sha256="c505344019b1a2708c775ffb1b8d092654d22a570799bb7b925c9effefc22703", url="https://pypi.org/packages/17/c3/df465011ff6a52663c64d3be45fe79bd9e48ff106c52c861ca1383c232ab/cattrs-23.2.1-py3-none-any.whl")
    version("23.2.0", sha256="9783f5afefc889b680a83b7afc88c53388ae89d05d4c199b35869beac1f77832", url="https://pypi.org/packages/19/29/f0b58e2dcdb2c2186a790410fabb66e3a0a70e0bea53b11bfa6ce7dca46c/cattrs-23.2.0-py3-none-any.whl")
    version("23.1.2", sha256="b2bb14311ac17bed0d58785e5a60f022e5431aca3932e3fc5cc8ed8639de50a4", url="https://pypi.org/packages/3a/ba/05df14efaa0624fac6b1510e87f5ce446208d2f6ce50270a89b6268aebfe/cattrs-23.1.2-py3-none-any.whl")
    version("23.1.1", sha256="6558a4ed415bffb202993cdc8ce0ba5b919c6eab19b996251a61a3329f900d62", url="https://pypi.org/packages/14/18/d55e2b298453250f162fbb6ad5a91daf2b1332bad14e14cefe276baf25a3/cattrs-23.1.1-py3-none-any.whl")
    version("23.1.0", sha256="9be29ab7041a3b9da67cad5daee578c511bcd52495ed85a6f8be3cf9d7c922d3", url="https://pypi.org/packages/a6/e3/ec670b59a31414fddaa73070bd6b2b9aa2ef913774f29ad8ed544601bb99/cattrs-23.1.0-py3-none-any.whl")
    version("23.1.0-rc0", sha256="1c7afd4b8de19315809262bc1344b14557debc7c5017fa928e3423c38add749a", url="https://pypi.org/packages/41/f0/b30004b7e654efbbbb399c2adc53dc474fd88dcba5cbe1930d7379dd4a9a/cattrs-23.1.0rc0-py3-none-any.whl")
    version("22.2.0", sha256="bc12b1f0d000b9f9bee83335887d532a1d3e99a833d1bf0882151c97d3e68c21", url="https://pypi.org/packages/43/3b/1d34fc4449174dfd2bc5ad7047a23edb6558b2e4b5a41b25a8ad6655c6c7/cattrs-22.2.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-attrs@23:", when="@23.2:")
        depends_on("py-attrs@20:", when="@1.8:23.1")
        depends_on("py-exceptiongroup@1.1.1:", when="@23.2: ^python@:3.10")
        depends_on("py-exceptiongroup", when="@22.2:23.1 ^python@:3.10")
        depends_on("py-exceptiongroup", when="@22:22.1 ^python@:3.10.0")
        depends_on("py-typing-extensions@4.1:4.6.2,4.7:", when="@23.2: ^python@:3.10")
        depends_on("py-typing-extensions@4.1:", when="@23.1.2:23.1 ^python@:3.10")
        depends_on("py-typing-extensions", when="@23.1.1 ^python@:3.10")
        depends_on("py-typing-extensions", when="@23:23.1.0 ^python@:3.9")

