##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySmartsim(PythonPackage):
    version("0.5.0", sha256="35b36243dc84af62261a7f772bae92f0b3502faf01401423899cb2a48339858c", url="https://pypi.org/packages/c5/e2/08b54b07d069733960520aef1b2aacb69978719ea7d12dc59a3673121be0/smartsim-0.5.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@:3.11", when="@0.6.1:")
        depends_on("python@:3.10", when="@0.4.2:0.6.0")

