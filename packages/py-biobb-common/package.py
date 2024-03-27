##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiobbCommon(PythonPackage):
    version("4.1.0", sha256="07640bbd23529f978f07fd245e3f0619f7df076be4f99d750d07dfac10b06a5c", url="https://pypi.org/packages/f3/6c/2c5ec2166df63af7474b95649d33e7ba2ef3f8e38ff8b3beef0d4a425aeb/biobb_common-4.1.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@:3.10.0", when="@4:4.0")
        depends_on("python@:3.9", when="@3.9:3")
        depends_on("py-biopython", when="@0.0.4:0.0.8,4.1:")
        depends_on("py-pyyaml")
        depends_on("py-requests", when="@0.0.4:")

