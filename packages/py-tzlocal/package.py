# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTzlocal(PythonPackage):
    # BEGIN VERSIONS
    version("5.2", sha256="49816ef2fe65ea8ac19d19aa7a1ae0551c834303d5014c6d5a62e4cbda8047b8", url="https://pypi.org/packages/97/3f/c4c51c55ff8487f2e6d0e618dba917e3c3ee2caae6cf0fbb59c9b1876f2e/tzlocal-5.2-py3-none-any.whl")
    version("5.1", sha256="2938498395d5f6a898ab8009555cb37a4d360913ad375d4747ef16826b03ef23", url="https://pypi.org/packages/1c/af/343114b3ed9500b46108b56569b31a3108d3669d4fd063d9640e2c36cd57/tzlocal-5.1-py3-none-any.whl")
    version("5.0.1", sha256="f3596e180296aaf2dbd97d124fe76ae3a0e3d32b258447de7b939b3fd4be992f", url="https://pypi.org/packages/84/d2/730a87f0dbf184760394a85088d0d2366a5a8a32bc32ffd869a83f1de854/tzlocal-5.0.1-py3-none-any.whl")
    version("5.0", sha256="c640e3fdccbb6fee1172ce211cefd3c3c04eaf2b0fbf676f0ac7958c41f373e4", url="https://pypi.org/packages/0a/93/55e34fba4b61fd4ba30e9341edb313f474d0e18006e8400b05e36b71a7bd/tzlocal-5.0-py3-none-any.whl")
    version("4.3.1", sha256="67d7e7f4ce0a98e9dfde2e02474c60fe846ed032d78b555c554c2e9cba472d84", url="https://pypi.org/packages/55/a6/a75af44665e5e77e52f6789eef4f8bc056c8e039d96c804b975806942580/tzlocal-4.3.1-py3-none-any.whl")
    version("4.3", sha256="b44c4388f3d34f25862cfbb387578a4d70fec417649da694a132f628a23367e2", url="https://pypi.org/packages/d4/46/e8002faae3d1df7d7a0a3aa0cb4b2ccd805c3a71fb507b06446012b28790/tzlocal-4.3-py3-none-any.whl")
    version("4.2", sha256="89885494684c929d9191c57aa27502afc87a579be5cdd3225c77c463ea043745", url="https://pypi.org/packages/31/b7/3bc2c1868f27677139b772e4fde95265b93151912fd90eb874827943bfcf/tzlocal-4.2-py3-none-any.whl")
    version("4.1", sha256="28ba8d9fcb6c9a782d6e0078b4f6627af1ea26aeaa32b4eab5324abc7df4149f", url="https://pypi.org/packages/ac/29/0daef8da885f35b3c8a54ac45378d4829a7f787ec55475b541bed3df6a36/tzlocal-4.1-py3-none-any.whl")
    version("4.0.2", sha256="9d0bb4c2640616f4965bb229eaf53a9e4c4c69cec3e6ab08eb2a55712e2fe1d3", url="https://pypi.org/packages/f3/af/6cc05ca4a582553d058c7bd58e27e175a5343cf86a1a12a3978527a4314f/tzlocal-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="3689a33e855912057028c41e31c5e27e6aa97658c58e35b76d58d0c301993b6d", url="https://pypi.org/packages/ac/ec/9cdd5609ba1cdc63e81757dda760c8745318d8fa0ff4da2a36d9ea743cb7/tzlocal-4.0.1-py3-none-any.whl")
    version("2.1", sha256="e2cb6c6b5b604af38597403e9852872d7f534962ae2954c7f35efcb1ccacf4a4", url="https://pypi.org/packages/5d/94/d47b0fd5988e6b7059de05720a646a2930920fff247a826f61674d436ba4/tzlocal-2.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="11c9f16e0a633b4b60e1eede97d8a46340d042e67b670b290ca526576e039048", url="https://pypi.org/packages/ef/99/53bd1ac9349262f59c1c421d8fcc2559ae8a5eeffed9202684756b648d33/tzlocal-2.0.0-py2.py3-none-any.whl")
    version("1.3", sha256="d160c2ce4f8b1831dabfe766bd844cf9012f766539cf84139c2faac5201882ce", url="https://pypi.org/packages/d3/64/e4b18738496213f82b88b31c431a0e4ece143801fb6771dddd1c2bf0101b/tzlocal-1.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-backports-zoneinfo", when="@3.0: ^python@:3.8")
        depends_on("py-pytz", when="@2")
        depends_on("py-pytz-deprecation-shim", when="@4.0-beta3:4")
        depends_on("py-tzdata", when="@3.0: platform=windows")
    # END DEPENDENCIES

