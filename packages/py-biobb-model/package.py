# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiobbModel(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.0", sha256="c5d4dcd866733ef385e8597f955ab44a3449e21b52cb8fdb607601878961f0c9", url="https://pypi.org/packages/63/7d/2b2c20c9cd4471851136d030489aacab158a4c5985c43cccb927e5ab10c6/biobb_model-4.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.10.0", when="@4:4.0.0")
        depends_on("python@:3.9", when="@4.0.1:4.0")
        depends_on("py-biobb-common@4.1:", when="@4.1:")
        depends_on("py-biobb-structure-checking@3.13.4:", when="@4.1:")
        depends_on("py-xmltodict", when="@3.8.1:")
    # END DEPENDENCIES

