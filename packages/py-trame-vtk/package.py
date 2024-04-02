# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrameVtk(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.8.5", sha256="b89c6a164b6ec7e63b8a181547a7dda2a859f0fb16835e2686afc861d8c7b397", url="https://pypi.org/packages/80/40/edfb25e7088fa41d40fcfa04991b19e090aa00dcab5901c46fb1bbec51d5/trame_vtk-2.8.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-trame-client")
    # END DEPENDENCIES

