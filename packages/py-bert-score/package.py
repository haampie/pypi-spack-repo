##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBertScore(PythonPackage):
    version("0.3.13", sha256="bbbb4c7fcdaa46d7681aff49f37f96faa09ed74e1b150e659bdc6b58a66989b9", url="https://pypi.org/packages/c6/8c/bc5457de4c004b1a623b31f7bc8d0375fb699b7d67df11879098b4b7b7c8/bert_score-0.3.13-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-packaging@20.9:", when="@0.3.12:")
        depends_on("py-pandas@1.0.1:", when="@0.3.1:")
        depends_on("py-requests")
        depends_on("py-torch@1:", when="@0.2:")
        depends_on("py-tqdm@4.31.1:", when="@0.1.2:")
        depends_on("py-transformers@3:", when="@0.3.5:")

