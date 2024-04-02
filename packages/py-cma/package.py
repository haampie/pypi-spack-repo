# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCma(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.3.0", sha256="5cc571b1e2068fcf1c538be36f8f3a870107456fed22ce81c1345a96329e61db", url="https://pypi.org/packages/77/70/da60edd6a12a8b4af07e583076c8f039f2a2792a0f0d9219d84522d23493/cma-3.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("constrained_solution_tracking", default=False, description="constrained_solution_tracking")
    variant("plotting", default=False, description="plotting")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib", when="@3:3.0,3.2:+plotting")
        depends_on("py-numpy", when="@3:3.0,3.2:")
    # END DEPENDENCIES

