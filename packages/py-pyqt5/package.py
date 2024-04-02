# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyqt5(PythonPackage):
    # BEGIN VERSIONS
    version("5.15.10", sha256="d46b7804b1b10a4ff91753f8113e5b5580d2b4462f3226288e2d84497334898a", url="https://pypi.org/packages/4d/5d/b8b6e26956ec113ad3f566e02abd12ac3a56b103fcc7e0735e27ee4a1df3/PyQt5-5.15.10.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@5.15.7:")
        depends_on("py-pyqt5-sip@12.13:", when="@5.15.10:")
    # END DEPENDENCIES

