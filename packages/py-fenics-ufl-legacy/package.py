# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFenicsUflLegacy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2022.3.0", sha256="c909fcb4e837dd755b13541b274fe4c5e4147ce26c31e9dd209db36c3010f18f", url="https://pypi.org/packages/c4/ea/8de7b587715fb690ef872687eee8b9d39630af010adbd449d55053ac38ad/fenics_ufl_legacy-2022.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:")
        depends_on("py-numpy")
    # END DEPENDENCIES

