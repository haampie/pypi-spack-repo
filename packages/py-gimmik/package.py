##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGimmik(PythonPackage):
    version("3.2.1", sha256="c99a0461699297b568aff95bab585f996502df8b0407e7882fb141322b95e737", url="https://pypi.org/packages/93/01/29808394f21b322dfd3644ffe5d0ad85eb66820fe5f8ddedbe0375fd8137/gimmik-3.2.1-py3-none-any.whl")
    version("3.1.1", sha256="9087b735133cceb7750829c85948dcee6c7f4ee493ff83e3ca0ac828f1c0ebe8", url="https://pypi.org/packages/86/00/ee1e92babb2e54d03cf9656d570403d886c13654e6b95cd6aee7c274f235/gimmik-3.1.1-py3-none-any.whl")
    version("3.1", sha256="b6c8ea68bc263aeab6751ec3c723d449e8bb8633ce5fa748203f1c9d471ca317", url="https://pypi.org/packages/9c/cc/c467ac1badc47551ab8e0057edf25f27ffb1c493ba4b955e32157d7fdd82/gimmik-3.1-py3-none-any.whl")
    version("3.0", sha256="370c998d127fac64b216e0b3bdc66d27c26b406cb99713f5d52d10eaae87bc1d", url="https://pypi.org/packages/77/3a/4909f22d9240d998930c806b109d0b5e448910d63631afd924ffc95d4156/gimmik-3.0-py3-none-any.whl")
    version("2.3", sha256="ed4fac8dc39e47bd3090e1618bd909b9b1f83fad7234ab65c715d87b90d5c0c6", url="https://pypi.org/packages/fb/76/95b9cf397804a9a9223fd34f531b77cb7a7b4261708fd524156929de9a2c/gimmik-2.3-py3-none-any.whl")
    version("2.2", sha256="87a49e02ba1e8d3db55d85ca25ac2604722c87f7252e165f7a9820d20f37908b", url="https://pypi.org/packages/e9/0b/c11506535150ed2efbc9bd1e2c5a26c9bc5846f328583dda0c3b1ac6a175/gimmik-2.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-mako", when="@2.2:")
        depends_on("py-numpy@1.7:", when="@2.2:")

