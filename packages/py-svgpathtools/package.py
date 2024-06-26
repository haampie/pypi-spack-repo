# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySvgpathtools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.3", sha256="7f7bdafe2c03b312178460104705e1d554d8cf36c898bec41bdce9fed3504746", url="https://pypi.org/packages/71/96/cc91050f3b53c2cea0eda18f371d0584e7f43713ce606738384e8001a877/svgpathtools-1.3.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.3.2:")
        depends_on("py-svgwrite", when="@1.3.2:")
    # END DEPENDENCIES

