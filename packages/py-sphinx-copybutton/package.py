# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxCopybutton(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.12", sha256="517870030a931f313695705edbe14a8c30660829716100d3d24b379cf9257060", url="https://pypi.org/packages/8d/b7/aee2c0dc1c5e413fffd08d5f933f3de08d12d978583fe940c419d9eebc31/sphinx_copybutton-0.2.12-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx@1.8.0:", when="@0.2.9:")
    # END DEPENDENCIES

