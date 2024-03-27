##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMaturin(PythonPackage):
    version("1.4.0", sha256="2979175a7eee837dc3a6931980b37ddc86b9ced54d600856668fc074ca2530ef", url="https://pypi.org/packages/18/a0/8a5a3a61aaf27052420c2d06ada05b4502838362d4edf5466a2b1e2b639e/maturin-1.4.0-py3-none-win_arm64.whl")
    version("1.1.0", sha256="a36efcca897b356deee56c7a3c399c595201518a892ec0f20f0f20abb3064ccb", url="https://pypi.org/packages/de/98/ae4ac485289773c826bdc4ba3c09a1762b26ca389734d0c4eda3f46859f2/maturin-1.1.0-py3-none-win_arm64.whl")
    version("0.14.17", sha256="abfd98529cfab59deb59639962d93df72121013d5151a5f01c66cda19d9c88a9", url="https://pypi.org/packages/d4/35/082c64295692273c3869ac3073e61e32680d63ac3309461bd836b86d3d89/maturin-0.14.17-py3-none-win_arm64.whl")
    version("0.13.7", sha256="8c6225e7eba2885a0cd82a6cf898e74bb720796a5744e0450f3b1340d1ca97af", url="https://pypi.org/packages/ed/7e/48f284850bbc4c169986fea7dd6e7d95f38d6aabd5cc22fadc202d9a0428/maturin-0.13.7-py3-none-win_arm64.whl")

    with default_args(type="run"):
        depends_on("py-tomli@1.1:", when="@0.12.10-beta4: ^python@:3.10")

