##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHtseq(PythonPackage):
    version("2.0.3", sha256="c7e7eb29bdc44e80d2d68e3599fa8a8f1d9d6475624dcf1b9644285a8a9c0fac", url="https://pypi.org/packages/83/61/05ce20ed21cedf9c31a0bc20cdffb66012e6ac202609ea1207322895c301/HTSeq-2.0.3.tar.gz")
    version("0.11.2", sha256="65c4c13968506c7df92e97124df96fdd041c4476c12a548d67350ba8b436bcfc", url="https://pypi.org/packages/b1/55/3612dc17fe2a85c9f0a4b98b97aa8a9850d0930e2ad89deaf9c5e1271e97/HTSeq-0.11.2.tar.gz")
    version("0.9.1", sha256="af5bba775e3fb45ed4cde64c691ebef36b0bf7a86efd35c884ad0734c27ad485", url="https://pypi.org/packages/fd/94/b7c8c1dcb7a3c3dcbde66b8d29583df4fa0059d88cc3592f62d15ef539a2/HTSeq-0.9.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@0.9:0.12")
        depends_on("py-pysam", when="@0.9.1:0.9,0.12")
        depends_on("py-pysam@0.9:", when="@0.9:0.9.0,0.11")

