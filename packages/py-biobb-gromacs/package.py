# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiobbGromacs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.1", sha256="698f0bdb6f6f5c896513b47669d2b2c6f6b7c0c753039df61a82fb1ca57c2f80", url="https://pypi.org/packages/83/29/ba77b856d70014284b072f30499704544fff363802a87e370306e0076e2d/biobb_gromacs-4.1.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.10.0", when="@4:4.0")
        depends_on("python@:3.9", when="@3.9:3")
        depends_on("py-biobb-common@4.1:", when="@4.1:")
    # END DEPENDENCIES

