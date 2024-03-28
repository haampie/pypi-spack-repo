# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGriddataformats(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.1", sha256="c2c45c9ea18f29ffd8fe311d5322b4cba4f4e4c76980ec4e2e9a7f296b208a46", url="https://pypi.org/packages/03/f7/a676afdb039c77eb012f4cdbed231e44555cc90025ce660d17cbeecdc9f9/GridDataFormats-1.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.0.2:")
        depends_on("py-mrcfile", when="@0.7:")
        depends_on("py-numpy@1.19.0:", when="@1:1.0.1")
        depends_on("py-scipy", when="@0.4.1:")
    # END DEPENDENCIES

