# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMotor(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.5.1", sha256="961fdceacaae2c7236c939166f66415be81be8bbb762da528386738de3a0f509", url="https://pypi.org/packages/ce/95/84c414596d902251fe295fa6c7062df85cdfb17eaf234f83264a44d0900a/motor-2.5.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pymongo@3.12:3", when="@2.5:2")
    # END DEPENDENCIES

