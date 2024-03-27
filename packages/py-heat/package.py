##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHeat(PythonPackage):
    version("1.3.0", sha256="d0551ca2a8cedb9c05002c076b747d85a5fd294c6bd63f5e390df1272eaaa6a3", url="https://pypi.org/packages/a6/b9/3d9dd4940b0a5b2f1ef81f982a4d608614c3e062cd079f12b0c342f36992/heat-1.3.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-mpi4py@3:", when="@0.4:")
        depends_on("py-numpy@1.20.0:", when="@1.3:")
        depends_on("py-pillow@6:", when="@1:")
        depends_on("py-scipy@0.14:", when="@0.5:")
        depends_on("py-torch@1.8:2.0", when="@1.3:")
        depends_on("py-torchvision@0.8:", when="@1:1.1.0,1.2:")

