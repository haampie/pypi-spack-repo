# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLpips(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.4", sha256="fd537af5828b69d2e6ffc0a397bd506dbc28ca183543617690844c08e102ec5e", url="https://pypi.org/packages/9b/13/1df50c7925d9d2746702719f40e864f51ed66f307b20ad32392f1ad2bb87/lpips-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="b3a1c336f8d88c265e46a97f33cca656538cf4a0f9cae72c2c402d5995b5acf8", url="https://pypi.org/packages/21/de/774d9cdb601bb938b6a501f1aeaa64288a763ebbafbeef227a3da86150d9/lpips-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="6b3a5f73faff3469be638e137aea74833c4a817abf1aef143365d1488ddfc913", url="https://pypi.org/packages/40/d6/01eb029a00cc02bd22972085fbbd5b4f6524dfeb198ea22b4b24de09b673/lpips-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="d3da531c626cca1aa8e51f83a59a5d4a272905a2a008a185b14dc0fa3b0ad64c", url="https://pypi.org/packages/30/a8/6b58b405bdd35ab156b5017e9835fa52db5133a073776dc5446e0b58837d/lpips-0.1.1-py3-none-any.whl")
    version("0.1", sha256="1d7bc2fa4f598f593cc070ac0f619cde5fe014e38151c639da28846a1b435eca", url="https://pypi.org/packages/3b/b1/c3f632fdecd5e2aef794969b16d849bae462cbdd2a564de3c0c7957733fc/lpips-0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.14.3:", when="@0.1.4:")
        depends_on("py-scipy@1.0.1:", when="@0.1.4:")
        depends_on("py-torch@0.4:", when="@0.1.4:")
        depends_on("py-torchvision@0.2.1:", when="@0.1.4:")
        depends_on("py-tqdm@4.28.1:", when="@0.1.4:")
    # END DEPENDENCIES

