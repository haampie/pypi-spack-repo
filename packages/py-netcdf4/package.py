# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNetcdf4(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.5", sha256="824881d0aacfde5bd982d6adedd8574259c85553781e7b83e0ce82b890bfa0ef", url="https://pypi.org/packages/da/f2/b7307966bf174559c80c0bdaaccebe1538efa3aef8e996d18229b01e9760/netCDF4-1.6.5.tar.gz")
    version("1.6.2", sha256="0382b02ff6a288419f6ffec85dec40f451f41b8755547154c575ddd9f0f4ae53", url="https://pypi.org/packages/a6/f9/12f43c2e31d1c7aae0827820ae747fa4c7cc382b38dab11e8c11575d3af6/netCDF4-1.6.2.tar.gz")
    version("1.5.8", sha256="ca3d468f4812c0999df86e3f428851fb0c17ac34ce0827115c246b0b690e4e84", url="https://pypi.org/packages/e4/09/c7582134adb67b2ef136b954344d0522e9e3e1c7a292004eec0e8f8b1f0d/netCDF4-1.5.8.tar.gz")
    version("1.5.3", sha256="2a3ca855848f4bbf07fac366da77a681fcead18c0a8813d91d46302f562dc3be", url="https://pypi.org/packages/cd/ee/b7734f8fb94c9671b6966f158903cd3b67cb60d245c6f2196bcf1f8b13b5/netCDF4-1.5.3.tar.gz")
    version("1.4.2", sha256="b934af350459cf9041bcdf5472e2aa56ed7321c018d918e9f325ec9a1f9d1a30", url="https://pypi.org/packages/eb/aa/b067f3b1a2561f29f5c282d8a0f0f4bba5b13e9bdaa5fcd29005d226c448/netCDF4-1.4.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mpi", default=False, description="mpi")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.6.3:")
        depends_on("py-cftime", when="@1.4:1.5.3")
        depends_on("py-numpy@1.7:", when="@1.3:1.5.3")
    # END DEPENDENCIES

