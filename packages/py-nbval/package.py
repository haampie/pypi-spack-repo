# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbval(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.6", sha256="4f9b780997d8942408853513f2c5ee6c1863de193559fc3f95e1c1cde8110439", url="https://pypi.org/packages/b0/92/23d60d4593b6e69f2114caf6fec238ce461233a8633dcbef6f619ad339c9/nbval-0.9.6-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-coverage", when="@0.9:0.9.3,0.9.5:")
        depends_on("py-ipykernel", when="@:0.3.2,0.4.1:")
        depends_on("py-jupyter-client", when="@:0.3.2,0.3.6:")
        depends_on("py-nbformat", when="@:0.3.2,0.3.6:")
        depends_on("py-pytest@2.8:", when="@0.5:0.10")
        depends_on("py-six", when="@:0.3.2,0.3.6:0.9")
    # END DEPENDENCIES

