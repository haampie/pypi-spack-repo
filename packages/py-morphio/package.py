# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMorphio(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.6", sha256="0f2e55470d92a3d89f2141ae905ee104fd16257b93dafb90682d90171de2f4e6", url="https://pypi.org/packages/2e/80/09d5c5474b66e6dec1d3a5fe5a9351e86ec069093f7af7e8815f7e689b36/MorphIO-3.3.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@3.3.3:3.3.6")
    # END DEPENDENCIES

