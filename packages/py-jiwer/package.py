# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJiwer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.3", sha256="190d8238cb0262346781267d94f74c4fc8fc5094cf215a3d5d8317fb0954b842", url="https://pypi.org/packages/0d/4f/ee537ab20144811dd99321735ff92ef2b3a3230b77ed7454bed4c44d21fc/jiwer-3.0.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:3", when="@2.4:")
        depends_on("py-click@8.1.3:", when="@2.6:")
        depends_on("py-rapidfuzz@3:", when="@3.0.3:")
    # END DEPENDENCIES

