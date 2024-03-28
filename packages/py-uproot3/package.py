# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUproot3(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.14.4", sha256="d0b513aed4af17278d582a4879eff7037efe0752c7e2154683ac4c4f083c30c0", url="https://pypi.org/packages/9c/69/d893c6eba0dd0d8f82d841d4b85b6e63c52a1b472aec7cf7ae0efedf5a92/uproot3-3.14.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-awkward0")
        depends_on("py-cachetools")
        depends_on("py-numpy@1.13.1:")
        depends_on("py-uproot3-methods", when="@3.14.1:")
    # END DEPENDENCIES

