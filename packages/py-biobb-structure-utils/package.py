# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiobbStructureUtils(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.0", sha256="34a9c0fb0756a55ad79080af041f577cb690c23260f9d4f260d52db820c64ad3", url="https://pypi.org/packages/1a/69/2838e416913da3e99c79c18697e7171282ce7890cdeeb6cf16f1b2d39637/biobb_structure_utils-4.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.10.0", when="@4:4.0")
        depends_on("python@:3.9", when="@3.9:3")
        depends_on("py-biobb-common@4.1:", when="@4.1:")
        depends_on("py-biobb-structure-checking@3.13.4:", when="@4.1:")
    # END DEPENDENCIES

