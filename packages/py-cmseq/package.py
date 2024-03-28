# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCmseq(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.4", sha256="7165869f81ad668a94dd1f1dd243aedb1bccc50f1547f67355737d9570954d73", url="https://pypi.org/packages/5c/2f/0d4effb9b71f4b78ad4fc0d4e5d433cfb2a6bbf1b26ba2c4164be352b7c0/CMSeq-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="7cbccebecd204995f6c915bfe1e214bd9b130881e3896e9a0e53ddcaaf3e8ad6", url="https://pypi.org/packages/1b/ff/0d89f6d71781abc1eb6fc710d360d8fb364185d2120ede1bf2d27edcde8d/CMSeq-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="b73cedc15c94f54576bb76bb4a59350b9100ac0f0a9869a032cdb996ff507175", url="https://pypi.org/packages/84/1a/8500f7c9ea4a7442edcde97b483a827e0c03cf21f6d1ddec5af70489e929/CMSeq-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="c2d86c02857a3344f03244b9f2515a97bd7a6bd7cd88c4d52b8bdff97d207ef1", url="https://pypi.org/packages/e1/d4/be9b733d9255754bfd5fb1866765471050b969cdb8cedc1cb72bb18a3f0c/CMSeq-1.0.1.tar.gz")
    version("1.0.0", sha256="7f4aef0912f96a6846075fdc691dfffa0f6e6d20aa841fc6f554d2d2757e961f", url="https://pypi.org/packages/a2/0c/a2fad3f82d2850b82bb99e68d5a0754afea38a8a48543c9ffdb97ffc9938/CMSeq-1.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-bcbio-gff", when="@1.0.2:")
        depends_on("py-biopython", when="@1.0.2:")
        depends_on("py-numpy", when="@1.0.2:")
        depends_on("py-pandas", when="@1.0.2:")
        depends_on("py-pysam", when="@1.0.2:")
        depends_on("py-scipy", when="@1.0.2:")
    # END DEPENDENCIES

