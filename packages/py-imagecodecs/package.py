# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyImagecodecs(PythonPackage):
    # BEGIN VERSIONS
    version("2022.2.22", sha256="062bef6b003290a8163abed2744b406854238208dfdd41cf7165253c6e01c0bd", url="https://pypi.org/packages/59/2d/344eaece340a87945b22dff57afb954487772394b801486c01184c4684ce/imagecodecs-2022.2.22.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2022:2023.3")
    # END DEPENDENCIES

