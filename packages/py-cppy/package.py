# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCppy(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.1", sha256="c5b5eac3d3f42593a07d35275b0bc27f447b76b9ad8f27c62e3cfa286dc1988a", url="https://pypi.org/packages/31/5e/b8faf2b2aeb679c0f4359fd1a4716fe90d65f72f72639413ffb95f3c3b46/cppy-1.2.1-py3-none-any.whl")
    version("1.1.0", sha256="4eda6f1952054a270f32dc11df7c5e24b259a09fddf7bfaa5f33df9fb4a29642", url="https://pypi.org/packages/36/64/be592e84c443a70ea5dcfb1c30bfe6f10ba7d8eb05c2264c7ceca8498548/cppy-1.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.2.1:")
    # END DEPENDENCIES

