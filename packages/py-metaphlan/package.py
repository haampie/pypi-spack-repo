##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMetaphlan(PythonPackage):
    version("4.0.2", sha256="9c475996fa6d36f3c6b6c097e358dcb1fcd065318fb5507d8cef823d0fe33943", url="https://pypi.org/packages/72/0c/df689a520a778c62f71b61df0ade45dc8c246c9ffc6cda1391b9aa3ab1da/MetaPhlAn-4.0.2-py3-none-any.whl")
    version("3.1.0", sha256="5d2990c75e2f332009b1ede14161ad1afbd83a9b512913a165caaa5d4dd0c44f", url="https://pypi.org/packages/75/a2/d73d8409366b7195052dccfd6e15b12ef0f86919c9f6f4a0fa509078054d/MetaPhlAn-3.1.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-biom-format", when="@3.0.1:")
        depends_on("py-biopython", when="@3.0.1:")
        depends_on("py-cmseq", when="@3.0.1:4.0")
        depends_on("py-dendropy", when="@3.0.1:")
        depends_on("py-h5py", when="@3.0.1:")
        depends_on("py-hclust2", when="@4.0.2:")
        depends_on("py-numpy", when="@3.0.1:")
        depends_on("py-pandas", when="@3.0.1:")
        depends_on("py-phylophlan", when="@3.0.1:")
        depends_on("py-pysam", when="@3.0.1:")
        depends_on("py-requests", when="@3.0.1:")
        depends_on("py-scipy", when="@3.0.1:")
