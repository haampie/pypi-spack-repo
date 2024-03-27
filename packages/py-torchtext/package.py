##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchtext(PythonPackage):
    version("0.6.0", sha256="100c6633d76c33eca10cf4a97ba20f95aff02efaa870032ef15b7a6a9f2fd77d", url="https://pypi.org/packages/f2/17/e7c588245aece7aa93f360894179374830daf60d7ed0bbb59332de3b3b61/torchtext-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="1caed2e155c45b4885daedb735b0f41e2f86ecd9dc788f75f824683bf1645f67", url="https://pypi.org/packages/79/ef/54b8da26f37787f5c670ae2199329e7dccf195c060b25628d99e587dac51/torchtext-0.5.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy", when="@0.3:")
        depends_on("py-requests", when="@:0.2.1,0.3:")
        depends_on("py-sentencepiece", when="@0.5:")
        depends_on("py-six", when="@0.4:")
        depends_on("py-torch", when="@0.3:")
        depends_on("py-tqdm", when="@:0.2.1,0.3:")

