# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReportlab(PythonPackage):
    # BEGIN VERSIONS
    version("4.0.4", sha256="3dcda79ce04baf70721e2ec54854722644262cac2feec3d5c4c5e77015504cb0", url="https://pypi.org/packages/db/8a/68ad8fb26592f1749c19b6e651296eeffb808a81f56be3dc09a739120676/reportlab-4.0.4-py3-none-any.whl")
    version("3.6.12", sha256="b13cebf4e397bba14542bcd023338b6ff2c151a3a12aabca89eecbf972cb361a", url="https://pypi.org/packages/b8/ac/10d68a650b321bd8c4d8cbefd9994e7727d57b381c9bdb0a013273011e62/reportlab-3.6.12.tar.gz")
    version("3.4.0", sha256="5beaf35e59dfd5ebd814fdefd76908292e818c982bd7332b5d347dfd2f01c343", url="https://pypi.org/packages/87/f9/53b34c58d3735a6df7d5c542bf4de60d699cfa6035e113ca08b3ecdcca3f/reportlab-3.4.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:3", when="@3.6.9:")
        depends_on("py-pillow@9:", when="@4:")
    # END DEPENDENCIES

