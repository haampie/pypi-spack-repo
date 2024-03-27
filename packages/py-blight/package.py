##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBlight(PythonPackage):
    version("0.0.47", sha256="6c2c5e4d630992b23fd4165e89af5036662ea62339e97f1df977db86b5203365", url="https://pypi.org/packages/36/62/ce130d11c8ee839897851636e9d5de7be46208c30fbd54227b31c12acd3e/blight-0.0.47-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-click@7.1:", when="@0.0.38:")
        depends_on("py-pydantic@1.7:1", when="@0.0.35:")
        depends_on("py-typing-extensions", when="@0.0.35:")

