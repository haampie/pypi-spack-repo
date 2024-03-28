# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGenshi(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.7", sha256="bed85e4015485a808bdd8d5bbb25cdc5fc093efab50776e2888be7b45b46f084", url="https://pypi.org/packages/3f/b3/3b75ecf6bab4bb52d6605af3a6e61ce3d393dfe349710c8a9425681dfc05/Genshi-0.7.7-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@0.7.4:")
    # END DEPENDENCIES

