# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnndata(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.0", sha256="2a929360c3c893370865e8ee3d3b9d95ee93239da91bafc5bf5f3c306796746e", url="https://pypi.org/packages/46/7f/ffe1546142d98ed55e7bb70eaedad92861d8e2ab07398ef7f06f4f46d06d/anndata-0.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.10:")
        depends_on("py-h5py@3.0.0:", when="@0.8:0.10.5")
        depends_on("py-natsort", when="@0.5:0.5.1,0.6.1:0.6.4,0.6.15,0.6.18,0.6.22-rc1,0.7-rc1,0.7:")
        depends_on("py-numpy@1.16.5:", when="@0.7.6:0.10.5")
        depends_on("py-packaging@20:", when="@0.7.6:")
        depends_on("py-pandas@1.1.1:", when="@0.7.6:0.9.1")
        depends_on("py-scipy@1.4.1:", when="@0.7.6:0.10.5")
    # END DEPENDENCIES

