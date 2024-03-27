##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMacs3(PythonPackage):
    version("3.0.0-beta3", sha256="caa794d4cfcd7368447eae15878505315dac44c21546e8fecebb3561e9cee362", url="https://pypi.org/packages/5f/ca/d5a64e33e643f2b9eb5f48571c48655999a0a2c22e5baf3cc815d729cad7/MACS3-3.0.0b3.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.0.0-beta2:")

