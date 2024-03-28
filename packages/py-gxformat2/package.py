# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGxformat2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.16.0", sha256="3501d7f0c2f75efb3a49e0805fd7597db691c2640bce2cdd71d8d263a2607793", url="https://pypi.org/packages/11/3d/88016d9ed55ce46cb89d3d2d14ef9f138ee6520a1d3faaba8c76d718fb6e/gxformat2-0.16.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-bioblend", when="@:0.1.0.0,0.1.1:")
        depends_on("py-pyyaml", when="@:0.1.0.0,0.1.1:")
    # END DEPENDENCIES

