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
    variant("cartopy", default=False)
    variant("cylp", default=False)
    variant("gdal", default=False)
    variant("hdf5", default=False)
    variant("rsl", default=False)
    variant("wradlib", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.14.6:")
    # END DEPENDENCIES

