##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPhanotate(PythonPackage):
    version("1.5.0", sha256="589e441d2369e5550aef98b8d99fd079d130363bf881a70ac862fc7a8e0d2c88", url="https://pypi.org/packages/5f/6d/14ec8bb4095c67c3ec6c8e4ceb4b378e6d5afecef679fe1ab9535f452b01/phanotate-1.5.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-fastpath@1.3:", when="@1.5:1.5.0,1.6:")

