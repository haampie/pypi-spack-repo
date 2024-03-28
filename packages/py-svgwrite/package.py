# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySvgwrite(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.3", sha256="bb6b2b5450f1edbfa597d924f9ac2dd099e625562e492021d7dd614f65f8a22d", url="https://pypi.org/packages/84/15/640e399579024a6875918839454025bb1d5f850bb70d96a11eabb644d11c/svgwrite-1.4.3-py3-none-any.whl")
    version("1.4.2", sha256="ca63d76396d1f6f099a2b2d8cf1419e1c1de8deece9a2b7f4da0632067d71d43", url="https://pypi.org/packages/cb/f3/5e44c3c6f36387afca7db6b6afbd47ea1e040ba362a6b9508d23123cc35f/svgwrite-1.4.2-py3-none-any.whl")
    version("1.4.1", sha256="4b21652a1d9c543a6bf4f9f2a54146b214519b7540ca60cb99968ad09ef631d0", url="https://pypi.org/packages/74/e8/5289be72545cd7eeacd67c9240995ce6513128b1fed66368f0137b0eddf5/svgwrite-1.4.1-py3-none-any.whl")
    version("1.4", sha256="fa842fb3129a9399d19b5e9602a022fcc7f2f3f24713550e765c488ffafd743d", url="https://pypi.org/packages/1c/85/1dc25b36c3ac4f3fe285d33065fc0f2ea7bdfb9209d6369e01a3e8ef6252/svgwrite-1.4-py3-none-any.whl")
    version("1.3.1", sha256="50fec23dc3fd49103808f0d672124f8c573ec5899da5686df734f856b8d3b737", url="https://pypi.org/packages/4f/2e/f36cfec1da6162055b884e6366074cff18475a9538559ceae0c0bc58e186/svgwrite-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="e6a141b662f4bd83bcbfb99c4efb38fbe2898ac944917e6162e1e05f842065e1", url="https://pypi.org/packages/e4/35/d21469e2e18d5a4afae9d1816c9618a8429bb516eda7b77709d777505ff5/svgwrite-1.3.0-py2.py3-none-any.whl")
    version("1.2.1", sha256="3a3ffd9cea9323ca53afd2e5049c2be174590078d306ea5fe3e2dce037a29343", url="https://pypi.org/packages/87/ce/3259f75aebb12d8c7dd9e8c479ad4968db5ed18e03f24ee4f6be9d9aed23/svgwrite-1.2.1-py2.py3-none-any.whl")
    version("1.2.0", sha256="19954fba837bec30d532f2c316324a367d5936f022f4bc5adf309ec1ecdff521", url="https://pypi.org/packages/83/35/df2ecc1afe36d25c86db81e43bd96320a0174aed490e9641bf260f69deb5/svgwrite-1.2.0-py2.py3-none-any.whl")
    version("1.1.12", sha256="4e84a0cd48bb116d26fa6f157e5902271bd1efb5ac5c6157d9811fda5a3d95a3", url="https://pypi.org/packages/9f/27/a29fc710b5fc4dc8031d55e903c1352a194df4014dccf8b507049dd754e6/svgwrite-1.1.12-py2.py3-none-any.whl")
    version("1.1.11", sha256="679507bb71c4eefb0d6c15643dbb8489ed0e3088330f46df30d7dc2abd897a82", url="https://pypi.org/packages/f6/92/60aa8a2953412060799f125d5b0de6417e7d507f3d6af606503cf1fd10d8/svgwrite-1.1.11-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyparsing@2.0.1:", when="@1.3-beta2:1.4-alpha0")
    # END DEPENDENCIES

