# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNetcdf4(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.5", sha256="824881d0aacfde5bd982d6adedd8574259c85553781e7b83e0ce82b890bfa0ef", url="https://pypi.org/packages/da/f2/b7307966bf174559c80c0bdaaccebe1538efa3aef8e996d18229b01e9760/netCDF4-1.6.5.tar.gz")
    version("1.6.4", sha256="66da6542cbc7a6045cd1d979397dfd5a3f6c880c76d52b8f98bb108c82ee8c6e", url="https://pypi.org/packages/8f/39/f8c4b2f3a4d78164e9850bb0924e1fd490e0bf8a8366b9b42cd295d7bbee/netCDF4-1.6.4.tar.gz")
    version("1.6.3", sha256="8c98a3a8cda06920ee8bd24a71226ddf0328c22bd838b0afca9cb45fb4580d99", url="https://pypi.org/packages/8b/92/ff3b18a2f5fe03ffc2807c2ac8b55bee2c8ee730d1100b79bc8a7ab96134/netCDF4-1.6.3.tar.gz")
    version("1.6.2", sha256="0382b02ff6a288419f6ffec85dec40f451f41b8755547154c575ddd9f0f4ae53", url="https://pypi.org/packages/a6/f9/12f43c2e31d1c7aae0827820ae747fa4c7cc382b38dab11e8c11575d3af6/netCDF4-1.6.2.tar.gz")
    version("1.6.1", sha256="ba8dc5d65293a99f1afb8c2acf588d903fdfdc1963a62545b677fa2734262a78", url="https://pypi.org/packages/ce/07/9d35ed96257250db30d4c6c632343c08581f1023af9b25b2e0e031839211/netCDF4-1.6.1.tar.gz")
    version("1.6.0", sha256="95efa373d9a3e1cd0df7193e76e6680d9eca28e60097ca8139afea8a4346ba63", url="https://pypi.org/packages/f9/94/f23af3c2c7b6e1250898ca9e3408821702889d35f5cfb05f427354df728f/netCDF4-1.6.0.tar.gz")
    version("1.5.8", sha256="ca3d468f4812c0999df86e3f428851fb0c17ac34ce0827115c246b0b690e4e84", url="https://pypi.org/packages/e4/09/c7582134adb67b2ef136b954344d0522e9e3e1c7a292004eec0e8f8b1f0d/netCDF4-1.5.8.tar.gz")
    version("1.5.7", sha256="d145f9c12da29da3922d8b8aafea2a2a89501bcb28a219a46b7b828b57191594", url="https://pypi.org/packages/df/e7/0eb5a6788502f0a1843f6b45a273c786a52d80c88003ce3d135a8c6da1bf/netCDF4-1.5.7.tar.gz")
    version("1.5.6", sha256="7577f4656af8431b2fa6b6797acb45f81fa1890120e9123b3645e14765da5a7c", url="https://pypi.org/packages/79/0d/caa957cc1b42b718ce4b9b3e849e6f7aa99faad2d522d8f2d7a33500fba0/netCDF4-1.5.6.tar.gz")
    version("1.5.5.1", sha256="d957e55a667d1fc651ddef22fea10ded0f142b7d9dbbf4d08c0012d32f445abd", url="https://pypi.org/packages/9f/e2/686d0d937f979e7ee0eb6bb4821448da6d2910789f4928c12b070f424b6a/netCDF4-1.5.5.1.tar.gz")
    version("1.5.3", sha256="2a3ca855848f4bbf07fac366da77a681fcead18c0a8813d91d46302f562dc3be", url="https://pypi.org/packages/cd/ee/b7734f8fb94c9671b6966f158903cd3b67cb60d245c6f2196bcf1f8b13b5/netCDF4-1.5.3.tar.gz")
    version("1.4.2", sha256="b934af350459cf9041bcdf5472e2aa56ed7321c018d918e9f325ec9a1f9d1a30", url="https://pypi.org/packages/eb/aa/b067f3b1a2561f29f5c282d8a0f0f4bba5b13e9bdaa5fcd29005d226c448/netCDF4-1.4.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mpi", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cftime", when="@1.4:1.5.3")
        depends_on("py-numpy@1.7:", when="@1.3:1.5.3")
    # END DEPENDENCIES

