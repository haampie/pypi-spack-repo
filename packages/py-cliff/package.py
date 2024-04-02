# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCliff(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.6.0", sha256="58a90e87738b9a7df672a5f9627bcd668564d01d8e567170dfe2d3a0026adb31", url="https://pypi.org/packages/e4/71/8506c160225ac44041eb1edcd90dd456878a41915c130b6b854f5eb31ef6/cliff-4.6.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@4:")
        depends_on("py-autopage@0.4:", when="@3.9:")
        depends_on("py-cmd2@1:")
        depends_on("py-importlib-metadata@4.4:", when="@4.5: ^python@:3.9")
        depends_on("py-prettytable@0.7.2:")
        depends_on("py-pyyaml@3.12:")
        depends_on("py-stevedore@2.0.1:")
    # END DEPENDENCIES

