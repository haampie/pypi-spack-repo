##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHyperopt(PythonPackage):
    version("0.2.5", sha256="dc5c7cceaf33c125b727cf92709e70035d94dd507831dae66406ac762a18a253", url="https://pypi.org/packages/a6/07/bd524635d218adae139be320eeac87fb4fbbd45c63b0bd58930c9e91f1fc/hyperopt-0.2.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-cloudpickle", when="@0.2:")
        depends_on("py-future", when="@0.1.2:")
        depends_on("py-networkx@2.2:", when="@0.2.4:")
        depends_on("py-numpy", when="@0.1.2:")
        depends_on("py-pymongo", when="@0.1.2:0.1")
        depends_on("py-scipy", when="@0.1.2:")
        depends_on("py-six", when="@0.1.2:")
        depends_on("py-tqdm", when="@0.1.2:")

