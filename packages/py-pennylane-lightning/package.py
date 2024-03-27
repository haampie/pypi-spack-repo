##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPennylaneLightning(PythonPackage):
    version("0.35.1", sha256="bc35d0d6c586dfc90791189fc1ed554bb88888b7bd2189b5970870c3a20aeb30", url="https://pypi.org/packages/3c/a3/277a7b8132ce4d7b774a207b93dbd4f23742ac41ba0e04d3c0a5b34d7818/PennyLane_Lightning-0.35.1.tar.gz")
    version("0.35.0", sha256="c36b6e598594d42f08fdc40e83a159d246cdb9aa5f5e58ced729ef16872559c1", url="https://pypi.org/packages/e4/30/00f5a2711bc9807c907288d6d06b0279c196e8c5014d384fe44b76d7846f/PennyLane_Lightning-0.35.0.tar.gz")
    version("0.34.0", sha256="e39624d7c9b6de66b149fc1538546d5f743b073a935262471277101a0d39a22b", url="https://pypi.org/packages/e8/0d/ce0b76740e1211710b7403c61b9e483147ca8da3cffbdd22ca9fc29ace01/PennyLane_Lightning-0.34.0.tar.gz")
    version("0.33.1", sha256="2ee1a2c2503d438c320923dd17a8bc988385d6264c09d596ec91126c00519b1b", url="https://pypi.org/packages/71/6f/39e986149a9efec4780fc972c48c318e3be706c82bf4c77fd55c7a160035/PennyLane_Lightning-0.33.1.tar.gz")
    version("0.33.0", sha256="f86746af318393334cc62990fafcfff9765437ecf967ffbea3c08f7f8075ad28", url="https://pypi.org/packages/f6/f5/1cc059bddbf70302e5cde09939b39787dfbee44e4daca2bf84e47d4f4636/PennyLane_Lightning-0.33.0.tar.gz")
    version("0.32.0", sha256="fc7e2e3432cf45ff739d8b0651263975c45a25ef78118d5fe1d5cd64155bc279", url="https://pypi.org/packages/99/a1/cda69a7bfad3733ed043e5378c1c7aaf2a5aa565151fe77f2f42255d1232/PennyLane_Lightning-0.32.0.tar.gz")
    version("0.31.0", sha256="8c8772a6a516ddeedf0b29b58a492f29b3aaf176fb9f89b678e001fe825898af", url="https://pypi.org/packages/12/98/fbcc98af988c4fdc2d4b01fe383f846caaebb309404c66f1c8f24a12b001/PennyLane-Lightning-0.31.0.tar.gz")
    version("0.30.0", sha256="e02615b8d89d970a5b4669faaf7ab29bdd58ed181b6f518fb325b27144f31e0c", url="https://pypi.org/packages/60/37/5f96dfc2d9cf01255aad9ece197b74f06064f2d1f0c10a6b47cf23d2af43/PennyLane-Lightning-0.30.0.tar.gz")
    version("0.29.0", sha256="d9cb0886f78c71923b6be2e0001ed368763af565f82e8fa529e3fe80425344cb", url="https://pypi.org/packages/ad/4b/4ba11d66fa3ac57655d6fd7b6cd0c0d9cab6ae9e077f0da62af11162ad49/PennyLane-Lightning-0.29.0.tar.gz")
    version("0.28.2", sha256="06c8575609e3e7f4de5b6d71affec7963fc9cc159ef576ce36b21d511bded374", url="https://pypi.org/packages/6e/f8/7d2d3152ccce669a920061dfe3f7a4b32ef99ddf1409f90b84b3cb9fcfcd/PennyLane-Lightning-0.28.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-pennylane@0.34:", when="@0.35:")
        depends_on("py-pennylane@0.33:", when="@0.34")

