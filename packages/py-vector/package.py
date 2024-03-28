# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVector(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.5", sha256="fccc2095edc93e2356dde116f37fa239b6268901dd98e35585f74480a31c4b17", url="https://pypi.org/packages/e8/d0/6b0e698190a47c8dea2800c114711b6badceef3d6c4db6c50c57b8e3aa9f/vector-0.8.5-py3-none-any.whl")
    version("0.8.4", sha256="4d42865b08202850f58b21126fe8c3c884add75999985f70e7974cbed6f2e966", url="https://pypi.org/packages/70/f2/058cde3474ff40a866050e71e2fc47fd22e33ceb5cd0ac90b02f8e9e3f2b/vector-0.8.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.13.3:", when="@0.8:")
        depends_on("py-packaging@19:", when="@0.8.2:")
    # END DEPENDENCIES

