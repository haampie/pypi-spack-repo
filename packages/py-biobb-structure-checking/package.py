# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiobbStructureChecking(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.13.4", sha256="ddafd434f0f8e711fff56898b5eba41458f4cd00a5c31543c50eba2c92dd33ef", url="https://pypi.org/packages/42/30/c3abd1652f1ab2f01b9ea438b0398bb247f9d85e4cf193abcb38b68f4ef6/biobb_structure_checking-3.13.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@3.13.4:")
        depends_on("py-biopython@1.79:", when="@3.13.2:")
        depends_on("py-numpy")
        depends_on("py-psutil")
    # END DEPENDENCIES

