# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAmici(PythonPackage):
    # BEGIN VERSIONS
    version("0.16.0", sha256="1a2d6633ec34241d8d8b496d18d4318482cffe125e9ddf3ca6cac5d36d235f38", url="https://pypi.org/packages/19/d5/6ff3dd6fccab5f6688621161e3ed2f0fee1d5bf50048cf0f6602ce58004f/amici-0.16.0.tar.gz")
    version("0.11.28", sha256="a8ddda70d8ebdc40600b4ad2ea02eb26e765ca0e594b957f61866b8c84255d5b", url="https://pypi.org/packages/7c/d5/0b3718f6550960dab5af8c8dc8cfe64e0b5f4ff91439ec010483a4ae0b01/amici-0.11.28.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("boost", default=False, description="boost")
    variant("hdf5", default=False, description="hdf5")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.11.24:0.16")
    # END DEPENDENCIES

