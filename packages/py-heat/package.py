# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHeat(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.0", sha256="d0551ca2a8cedb9c05002c076b747d85a5fd294c6bd63f5e390df1272eaaa6a3", url="https://pypi.org/packages/a6/b9/3d9dd4940b0a5b2f1ef81f982a4d608614c3e062cd079f12b0c342f36992/heat-1.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("dev", default=False)
    variant("docutils", default=False)
    variant("examples", default=False)
    variant("hdf5", default=False)
    variant("netcdf", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils@0.16:", when="@1:+docutils")
        depends_on("py-h5py@2.8.0:", when="@0.4:+hdf5")
        depends_on("py-matplotlib@3.1.0:", when="@1.2:+examples")
        depends_on("py-mpi4py@3:", when="@0.4:")
        depends_on("py-netcdf4@1.5.6:", when="@1:+netcdf")
        depends_on("py-numpy@1.20.0:", when="@1.3:")
        depends_on("py-pillow@6:", when="@1:")
        depends_on("py-pre-commit@1.18.3:", when="@0.4:+dev")
        depends_on("py-scikit-learn@0.24.0:", when="@1.2:+examples")
        depends_on("py-scipy@0.14:", when="@0.5:")
        depends_on("py-torch@1.8:2.0", when="@1.3:")
        depends_on("py-torchvision@0.8:", when="@1:1.1.0,1.2:")
    # END DEPENDENCIES

