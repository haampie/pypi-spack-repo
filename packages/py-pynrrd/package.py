# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPynrrd(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.0", sha256="65e5a61920d2f01ecf321eb41b0472940e181e4ba5e8a32f01ef5499d4192db5", url="https://pypi.org/packages/ee/43/1be50fe04e6a5df8cfdafa62151035a9358a768e26a5b9f33fc417e10bc6/pynrrd-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-nptyping", when="@1:")
        depends_on("py-numpy@1.11.1:", when="@0.3:")
        depends_on("py-typing-extensions", when="@1:")
    # END DEPENDENCIES

