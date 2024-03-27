##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUnyt(PythonPackage):
    version("2.9.2", sha256="77370720cb9edd898492bf5a735101c8eabac9d9a9259a43be25352007262b5d", url="https://pypi.org/packages/77/43/35fd177ee4d3353a0d42bb22214f492551548a51b97d4b9ed616c9936e39/unyt-2.9.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@3:")
        depends_on("py-numpy@1.17.5:", when="@:2")
        depends_on("py-sympy@1.5:", when="@:2")

