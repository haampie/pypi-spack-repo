##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyerfa(PythonPackage):
    version("2.0.1.1", sha256="dbac74ef8d3d3b0f22ef0ad3bbbdb30b2a9e10570b1fa5a98be34c7be36c9a6b", url="https://pypi.org/packages/4e/09/aaa59a4b4c22574fbe08e58e181933f19e455aef9b1a21a4eca026cd7d8f/pyerfa-2.0.1.1.tar.gz")
    version("2.0.1", sha256="c8572fd24ac779f067209dce1f2f6996d0701359724ecb89422ceb431632d554", url="https://pypi.org/packages/29/13/549e8a929ca49e690fa608e71b04611e7b2bf19ea082ed4e4418c7c748da/pyerfa-2.0.1.tar.gz")
    version("2.0.0.3", sha256="d77fbbfa58350c194ccb99e5d93aa05d3c2b14d5aad8b662d93c6ad9fff41f39", url="https://pypi.org/packages/a7/51/b1b8770853d82726dfa5d1079de29c32f144e10eb65b3852b1cd2b39f341/pyerfa-2.0.0.3.tar.gz")
    version("2.0.0.2", sha256="05370b7f0b4ca5a0caa845a1b6047259ba14d5608d1a18cd180049fff8c74b12", url="https://pypi.org/packages/0a/4c/54091d8b456c006dc0797c31cf7d7bbc1bf9929f79022ff3b480ee4d7764/pyerfa-2.0.0.2.tar.gz")
    version("2.0.0.1", sha256="2fd4637ffe2c1e6ede7482c13f583ba7c73119d78bef90175448ce506a0ede30", url="https://pypi.org/packages/78/fd/0148f0e54f0c6f48a141409df65d74a5f1dae2e139f23d50a43c58c16098/pyerfa-2.0.0.1.tar.gz")
    version("2.0.0", sha256="f904231e1a570f94440e06140799590895107f942847b52a753ce81c9609162d", url="https://pypi.org/packages/03/71/47b58cbbf8350209f0be27177d9ecc15df8956bbf00af74cb9cd2abc5df1/pyerfa-2.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.0.1:")
        depends_on("py-numpy@1.19.0:", when="@2.0.1:")

