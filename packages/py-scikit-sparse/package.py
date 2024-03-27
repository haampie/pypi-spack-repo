##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitSparse(PythonPackage):
    version("0.4.12", sha256="e6502fea9ba561cfa5491eb222ed2c81c16263d8182a293950db20509c941166", url="https://pypi.org/packages/af/b0/2e132641b238abf0fc4ac53cc58299253b8278bdbefba6a39b9b72a82d39/scikit-sparse-0.4.12.tar.gz")
    version("0.4.11", sha256="64c61a8777b7c7ba8e1f2bf76bc767f740e6426f1cce2d90f1324b177618e1ca", url="https://pypi.org/packages/a0/66/59536cd9add9adf11d6310b154a4c85f12c9162875038812d23779fbed16/scikit-sparse-0.4.11.tar.gz")
    version("0.4.8", sha256="2a224c60da3ef951975242ea777478583d3265efc72db5cfb7861686521a4009", url="https://pypi.org/packages/b9/e8/1fe87f92779a1c0392eea70ddcd9f50bea9255b9b6dabc206467a2a15925/scikit-sparse-0.4.8.tar.gz")

    with default_args(type="run"):
        depends_on("python@:3.11", when="@0.4.11:0.4.12")
        depends_on("python@:3.10", when="@0.4.7:0.4.8")
        depends_on("python@:3.9", when="@0.4.5:0.4.6")

