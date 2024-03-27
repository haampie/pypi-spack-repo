##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrandalf(PythonPackage):
    version("0.7", sha256="0ba234b8962420a093af39de82e89b22e9152d54b05d2fa30953ce39fa52aea3", url="https://pypi.org/packages/8d/5c/badfda0c15bbae6401f5a48ed2adb6e75902ae796bf5f69385948255e9c1/grandalf-0.7-py3-none-any.whl")
    version("0.6", sha256="7471db231bd7338bc0035b16edf0dc0c900c82d23060f4b4d0c4304caedda6e4", url="https://pypi.org/packages/a2/3f/df0618a962a1744e932f2a4547cb786f5a93df7e2476c99e7f7dbd68039f/grandalf-0.6.tar.gz")

    with default_args(type="run"):
        depends_on("py-future", when="@:0.6")
        depends_on("py-pyparsing")

