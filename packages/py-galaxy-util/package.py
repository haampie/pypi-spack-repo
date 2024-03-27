##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGalaxyUtil(PythonPackage):
    version("23.2.1", sha256="ae9c090da74f66c09e8d65f002b614ed314b6517478f77c476f84e3a3006cd92", url="https://pypi.org/packages/ff/b3/a099d984ffce5e026e6471f96d74d89f532cefa8fcf2b386e154b06582d0/galaxy_util-23.2.1-py3-none-any.whl")
    version("23.1.4", sha256="5dcf1e99f7f53e953a6f163393dfd0fe78439e34835006ad1c6efd75440ca6ee", url="https://pypi.org/packages/14/6b/062b766cd8d7fdfeb36af63bb3287ccae34efa5b489bdbf4956df82a838a/galaxy_util-23.1.4-py3-none-any.whl")
    version("23.1.3", sha256="43581a8f1c2a6616f74250fbbd28d251dc586492b15fc245578028bb833c4a73", url="https://pypi.org/packages/c4/29/9dab086a735ba31e563d9eff32a51b614cc925936dc21737ad4471cb55e2/galaxy_util-23.1.3-py3-none-any.whl")
    version("23.1.2", sha256="469d6b09131afd34a4bd367975f303b8c9c045e9cd4276856e561ef43a9a0372", url="https://pypi.org/packages/a9/3f/003e3176b830efe8420ad2e28270f819aad074f50956a07413fcd4b42ffc/galaxy_util-23.1.2-py3-none-any.whl")
    version("23.1.1", sha256="83baaa48692d159f02551120e727fdbebe5b36cc9a96205e81e80d106021bc7a", url="https://pypi.org/packages/35/58/3597766abdec662de287a568533899b3a975f668cd5683474ce35bb458ba/galaxy_util-23.1.1-py3-none-any.whl")
    version("23.0.6", sha256="58a710f27cb8326766884adbfad418b35d1be6b9e2b1870d2103a00bf484cdb1", url="https://pypi.org/packages/df/33/311a686ba6f8f33ecb2540e3f12839b1b848dab9d3dcc42f8129bc7f2b00/galaxy_util-23.0.6-py3-none-any.whl")
    version("23.0.5", sha256="1fbabd56a641df1d8fbfc2013dfeded6ee55c2a39f58275ce457d011b76b4f95", url="https://pypi.org/packages/b6/8a/83f8ce97f9e144a706a39ebeffc42a689a058d5e9164aec9def0936ded0b/galaxy_util-23.0.5-py3-none-any.whl")
    version("23.0.4", sha256="c35b12faf8ee352caf18178f7b2308d8d4a02c6b43b921434b02714ee86cedac", url="https://pypi.org/packages/75/4c/3e24eee0cb466f2832eb26d5b40e9bb433b115d84a0de789725cc5ef347b/galaxy_util-23.0.4-py3-none-any.whl")
    version("23.0.3", sha256="329dd9094b990fddec3d54c5aaa73b908a5b0be922f6e9dd941d30fe67b2856d", url="https://pypi.org/packages/d2/bd/3304a7cf3535da8ece3daaa27e892f955c5b8a50d7751226f79866288ccd/galaxy_util-23.0.3-py3-none-any.whl")
    version("23.0.2", sha256="0217868c87e3492837b56d270239f081a36ab33c05a327672a1a5590c067295d", url="https://pypi.org/packages/7a/88/aeaa4a1d4bf0dbc5cb4c4f563cdb94d9f6f77ab09bc594a41114f2876374/galaxy_util-23.0.2-py3-none-any.whl")
    version("22.1.2", sha256="23c9ea814244dfb020e30ea3284d6dacfd9ba4119fb76c1cc2b3ab379463f43c", url="https://pypi.org/packages/c6/6b/ca93c7a73a1d9c2153592007fd8264a357cb277de8d980ab6aa91c9cc8d1/galaxy_util-22.1.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-bleach")
        depends_on("py-boltons")
        depends_on("py-cheetah3", when="@19.9.0.dev:19.9.0.dev1")
        depends_on("py-docutils")
        depends_on("py-importlib-resources", when="@22:")
        depends_on("py-markupsafe", when="@:22.5.0.dev0")
        depends_on("py-packaging@:21", when="@22.1.2:23.0")
        depends_on("py-packaging", when="@:22.1.1,23.1:")
        depends_on("py-pycryptodome", when="@21.9:22.5.0.dev0")
        depends_on("py-pyparsing", when="@22.1.2:")
        depends_on("py-pyyaml")
        depends_on("py-requests", when="@20.5:")
        depends_on("py-routes")
        depends_on("py-typing-extensions", when="@22:")
        depends_on("py-zipstream-new", when="@21:")

