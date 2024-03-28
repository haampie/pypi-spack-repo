# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonSotools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.0", sha256="19b9e89d9489d08063f008fb8a9c41114c1953b1df5dc81a6f456081596265a1", url="https://pypi.org/packages/0d/ec/e13991b717dea200e8e49a4b6d997bd901ea5619e747862499bcea3ec91d/python_sotools-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyelftools", when="@0.0.3:")
    # END DEPENDENCIES

