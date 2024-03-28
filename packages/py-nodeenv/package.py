# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNodeenv(PythonPackage):
    # BEGIN VERSIONS
    version("1.8.0", sha256="df865724bb3c3adc86b3876fa209771517b0cfe596beff01a92700e0e8be4cec", url="https://pypi.org/packages/1a/e6/6d2ead760a9ddb35e65740fd5a57e46aadd7b0c49861ab24f94812797a1c/nodeenv-1.8.0-py2.py3-none-any.whl")
    version("1.7.0", sha256="27083a7b96a25f2f5e1d8cb4b6317ee8aeda3bdd121394e5ac54e498028a042e", url="https://pypi.org/packages/96/a8/d3b5baead78adadacb99e7281b3e842126da825cf53df61688cfc8b8ff91/nodeenv-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="621e6b7076565ddcacd2db0294c0381e01fd28945ab36bcf00f41c5daf63bef7", url="https://pypi.org/packages/54/73/56c89b343befb9c63e8117294d265458f0ff726fa2abcdc6bb5ec5e66a1a/nodeenv-1.6.0-py2.py3-none-any.whl")
    version("1.5.0", sha256="5304d424c529c997bc888453aeaa6362d242b6b4631e90f3d4bf1b290f1c84a9", url="https://pypi.org/packages/ae/d0/efdf54539948315cc76e5a66b709212963101d002822c3b54369dbf9b5e0/nodeenv-1.5.0-py2.py3-none-any.whl")
    version("1.4.0", sha256="4b0b77afa3ba9b54f4b6396e60b0c83f59eaeb2d63dc3cc7a70f7f4af96c82bc", url="https://pypi.org/packages/0d/54/538edbe88c87f6cd71f009145a56264622de84508f6ad1ae4d76976f47be/nodeenv-1.4.0-py2.py3-none-any.whl")
    version("1.3.5", sha256="5b2438f2e42af54ca968dd1b374d14a1194848955187b0e5e4be1f73813a5212", url="https://pypi.org/packages/08/43/86ff33286c83f7b5e8903c32db01fe122c5e8a9d8dc1067dcaa9be54a033/nodeenv-1.3.5-py2.py3-none-any.whl")
    version("1.3.4", sha256="561057acd4ae3809e665a9aaaf214afff110bbb6a6d5c8a96121aea6878408b3", url="https://pypi.org/packages/18/04/2683fe139a9be4d5df02e696f2ed0318ded368feb9e9bbe581611c47e337/nodeenv-1.3.4-py2.py3-none-any.whl")
    version("1.3.3", sha256="ad8259494cf1c9034539f6cced78a1da4840a4b157e23640bc4a0c0546b0cb7a", url="https://pypi.org/packages/00/6e/ed417bd1ed417ab3feada52d0c89ab0ed87d150f91590badf84273e047c9/nodeenv-1.3.3.tar.gz")
    version("1.3.2", sha256="aa040ab5189bae17d272175609010be6c5b589ec4b8dbd832cc50c9e9cb7496f", url="https://pypi.org/packages/36/ca/1a635c6cd6049105fadfdc05c8de364f368fcc7aebad3081dd8ccb0c5c7f/nodeenv-1.3.2.tar.gz")
    version("1.3.1", sha256="0611c726af1b252908646787f4d49811aa69cd92ec19644ded06ad9d3162f88e", url="https://pypi.org/packages/e0/89/dbda906ff83360c3fe33d5d11102c39036614ee8ef943317a95cbe691136/nodeenv-1.3.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@1.7:")
    # END DEPENDENCIES

