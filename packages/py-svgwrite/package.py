##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySvgwrite(PythonPackage):
    version("1.4.3", sha256="bb6b2b5450f1edbfa597d924f9ac2dd099e625562e492021d7dd614f65f8a22d", url="https://pypi.org/packages/84/15/640e399579024a6875918839454025bb1d5f850bb70d96a11eabb644d11c/svgwrite-1.4.3-py3-none-any.whl")
    version("1.4.2", sha256="ca63d76396d1f6f099a2b2d8cf1419e1c1de8deece9a2b7f4da0632067d71d43", url="https://pypi.org/packages/cb/f3/5e44c3c6f36387afca7db6b6afbd47ea1e040ba362a6b9508d23123cc35f/svgwrite-1.4.2-py3-none-any.whl")
    version("1.4.1", sha256="4b21652a1d9c543a6bf4f9f2a54146b214519b7540ca60cb99968ad09ef631d0", url="https://pypi.org/packages/74/e8/5289be72545cd7eeacd67c9240995ce6513128b1fed66368f0137b0eddf5/svgwrite-1.4.1-py3-none-any.whl")
    version("1.4", sha256="fa842fb3129a9399d19b5e9602a022fcc7f2f3f24713550e765c488ffafd743d", url="https://pypi.org/packages/1c/85/1dc25b36c3ac4f3fe285d33065fc0f2ea7bdfb9209d6369e01a3e8ef6252/svgwrite-1.4-py3-none-any.whl")
    version("1.3.1", sha256="50fec23dc3fd49103808f0d672124f8c573ec5899da5686df734f856b8d3b737", url="https://pypi.org/packages/4f/2e/f36cfec1da6162055b884e6366074cff18475a9538559ceae0c0bc58e186/svgwrite-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="e6a141b662f4bd83bcbfb99c4efb38fbe2898ac944917e6162e1e05f842065e1", url="https://pypi.org/packages/e4/35/d21469e2e18d5a4afae9d1816c9618a8429bb516eda7b77709d777505ff5/svgwrite-1.3.0-py2.py3-none-any.whl")
    version("1.2.1", sha256="72ef66c9fe367989823cb237ab7f012ac809dd3ba76c1b5ebd9aa61580e2e75e", url="https://pypi.org/packages/a5/b8/0a9d25dfaea196ecba2c8eb58a1ee6f337320e8ecbbe5254729dae36b60c/svgwrite-1.2.1.zip")
    version("1.2.0", sha256="d72c04031f621a71e08d6360eb31a86193f9df321b72f895d83936b11b3ded56", url="https://pypi.org/packages/28/8d/2f76c90478ccd6d7cbadb40c7041ecbd14c3975b5e0a99699dbc36a25ff0/svgwrite-1.2.0.zip")
    version("1.1.12", sha256="968c99f193f34f0fa7f0b3e82f49b93789c7c45cd89ce190480f16020d41ab79", url="https://pypi.org/packages/a6/e1/8d592fc801e1dc2958fe0c84c733ed729d4020daa1826c58978f9d601bb4/svgwrite-1.1.12.zip")
    version("1.1.11", sha256="451c7f16220d654be0cfdbd13cc6f23aca69e6fd3ca19254e80b5f6d9ca6af5a", url="https://pypi.org/packages/69/a5/c5edc66eb5bd9259589b3a379c8aac4084a92cad48fc688b07c1108da272/svgwrite-1.1.11.zip")

    with default_args(type="run"):
        depends_on("py-pyparsing@2.0.1:", when="@1.3-beta2:1.4-alpha0")

