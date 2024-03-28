# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCpat(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.4", sha256="d477beebd3a5ff06faec3b7bcfec550c3953b8af2e764037ca67ae0abd6329ec", url="https://pypi.org/packages/ba/78/50b5a87adb16578e8e39f16fb8a494f3c45959836d8af4f50a9a2056ddf4/CPAT-3.0.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-pysam")
    # END DEPENDENCIES

