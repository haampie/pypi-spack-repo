# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRiver(PythonPackage):
    # BEGIN VERSIONS
    version("0.13.0", sha256="9d068b7a9db32302fbd581af81315681dfe61774a5d777fb3d5982d3c3061340", url="https://pypi.org/packages/eb/74/cd1a44b330fb2def81f8376b4b95328aed44deb3e829788d22c1bf58c161/river-0.13.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.11:0.19")
    # END DEPENDENCIES

