# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArmPyart(PythonPackage):
    # BEGIN VERSIONS
    version("1.12.7", sha256="b7b23ecef270c60b017d94603941f0c117de072a10125c5f58c0685d801f9161", url="https://pypi.org/packages/a6/16/ce7a4c720f178fa6984a966bcca8a6e2cab38f8556e174cd8b2ee9140710/arm_pyart-1.12.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cartopy", default=False, description="cartopy")
    variant("cylp", default=False, description="cylp")
    variant("gdal", default=False, description="gdal")
    variant("hdf5", default=False, description="hdf5")
    variant("rsl", default=False, description="rsl")
    variant("wradlib", default=False, description="wradlib")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

