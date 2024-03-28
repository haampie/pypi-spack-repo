# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHealpy(PythonPackage):
    # BEGIN VERSIONS
    version("1.14.0", sha256="2720b5f96c314bdfdd20b6ffc0643ac8091faefcf8fd20a4083cedff85a66c5e", url="https://pypi.org/packages/52/bb/21e57f6b3a4c2a3bb59fb2a284fccf6ea15241a180e86ace1f9b891e251b/healpy-1.14.0.tar.gz")
    version("1.13.0", sha256="d0ae02791c2404002a09c643e9e50bc58e3d258f702c736dc1f39ce1e6526f73", url="https://pypi.org/packages/26/74/0c8592686027a8196e275cb81999e8aae88d0416c223fa55a7f0cb5bdd26/healpy-1.13.0.tar.gz")
    version("1.7.4", sha256="3cca7ed7786ffcca70e2f39f58844667ffb8521180ac890d4da651b459f51442", url="https://pypi.org/packages/6a/cf/bbbfd1d300e35ca7b5e005f4d3872b392a36618705f0029ccc8155277117/healpy-1.7.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.16.6:")
    # END DEPENDENCIES

