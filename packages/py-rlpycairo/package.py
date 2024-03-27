##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRlpycairo(PythonPackage):
    version("0.3.0", sha256="f6ec712a76914f78c1491351e1d79eeb1a40d072accf5d36075e399963c17b17", url="https://pypi.org/packages/3d/d6/0f52d7f85e14429124651a3e4db8b50b1ec860b674648e34a8d5e0861771/rlPyCairo-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="a88bce206c45d2180f944b8754c6e2e9245f80506c90fdfb94c7fbdd27805c25", url="https://pypi.org/packages/12/b7/a659c64433ae732fc9e372e79eeaf9fd29c9bc324a4e4101f2d3171086fa/rlPyCairo-0.2.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-freetype-py@2.3:", when="@0.2:")
        depends_on("py-pycairo@1.20:", when="@:0.0.6,0.0.8:")

