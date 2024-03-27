##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySourmash(PythonPackage):
    version("4.8.2", sha256="cb8dce43b7c73061b988f01c7af60839eb4706845121fa9f690bd8370a24f5f6", url="https://pypi.org/packages/a4/cc/00eabd390efd38ffba026640a4dbef810db28077e7af47dc8f1a802cb489/sourmash-4.8.2-py3-none-musllinux_1_1_x86_64.whl")

    with default_args(type="run"):
        depends_on("python@3.10:", when="@4.8.5:")
        depends_on("py-bitstring@3.1.9:", when="@4.6:")
        depends_on("py-cachetools@4:", when="@4.4:")
        depends_on("py-cffi@1.14:", when="@3.3.1:")
        depends_on("py-deprecation@2.0.6:", when="@3.2.2,3.3.1:")
        depends_on("py-importlib-metadata@3.6:", when="@4.8:4.8.4 ^python@:3.9")
        depends_on("py-matplotlib", when="@3.2.2,3.3.1:")
        depends_on("py-numpy", when="@3.2.2,3.3.1:")
        depends_on("py-scipy", when="@3.2.2,3.3.1:")
        depends_on("py-screed@1.1.2:", when="@4.8:")

