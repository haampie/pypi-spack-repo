##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstropyHealpix(PythonPackage):
    version("1.0.2", sha256="056fa6ed9396bedc771d374d877cde83d9460a3f62a78fe05dbf9ba03940323a", url="https://pypi.org/packages/89/83/d61648337c65147289c467e487db311c263f9e36aa9dbb3d4841bc2173ae/astropy_healpix-1.0.2.tar.gz")
    version("1.0.1", sha256="ef8938bdf729757c380a8c1734794d7374ad00e0767fc4a2fa63a66bef126242", url="https://pypi.org/packages/be/0a/cee3218b2c3b3882468e9342c85c9613f6691599114444c8e13c3b983096/astropy_healpix-1.0.1.tar.gz")
    version("1.0.0", sha256="f482ef62a10e686303f38c66f08df17b9ddee5ad82219c23571ee80d76abeea3", url="https://pypi.org/packages/c4/c7/7a0f624901675b0e5d6fd886ff87ea1bae2c0642b1adc3d3a6195c5c87d8/astropy_healpix-1.0.0.tar.gz")
    version("0.7", sha256="88c384eb4322997a58de8938e91ac9ff90f6a2b6cb2ae23e2169c7405add3ad8", url="https://pypi.org/packages/f2/a7/e657b8029efe8b1fe0c1050c8888d6734645f23e2ce0e071ea66ecace90f/astropy_healpix-0.7.tar.gz")
    version("0.6", sha256="409a6621c383641456c074f0f0350a24a4a58e910eaeef14e9bbce3e00ad6690", url="https://pypi.org/packages/0e/7b/b6c1feecd3a23cb1a873eacfee7cbd3c3ff75001f6bb45662a4a400f3282/astropy_healpix-0.6.tar.gz")
    version("0.5", sha256="5ae15da796a840f221fb83e25de791e827b6921bc21a365d99bc1a59c7c0cdad", url="https://pypi.org/packages/99/13/603db11e5107638cc68e101ccab75ab5632b395dc414e088ca2f8148c9fc/astropy-healpix-0.5.tar.gz")
    version("0.4", sha256="8c9709ac923759c92eca6d2e623e734d0f417eed40ba835b77d99dec09e51aa2", url="https://pypi.org/packages/74/b3/0d5c12ec78a5b002b16b17f540d3371522a1dbcac7ad580bc002a42d6cbb/astropy-healpix-0.4.tar.gz")
    version("0.3.1", sha256="d699b2a94b3235c1d4d3bf7a993b6684b08d55d453028748b2df6b2c6e92f21c", url="https://pypi.org/packages/4d/83/ed4f17e48d813dea98a2b736e13dcb26490dfda42adcb08405ef11de7538/astropy-healpix-0.3.1.tar.gz")
    version("0.3", sha256="516a369de9d904864fb35d81ec660d3aab4b4767e4ad42c13275fb674309ec9f", url="https://pypi.org/packages/85/04/d03682c1c9ffaffad457982175823b5d98e68fd5b4c059b99c218639c7b8/astropy-healpix-0.3.tar.gz")
    version("0.2.1", sha256="c578f6ec0dfbc8bc73ad2bb64720a35fdfa0fb8bb7b481a180b616431b80a904", url="https://pypi.org/packages/81/f1/f1085849c77af493b7deb45714453bee69d8be90cff1dcdd3469563fc93b/astropy-healpix-0.2.1.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1:")
        depends_on("py-astropy@3.0:", when="@1.0.1:")
        depends_on("py-numpy@1.19.0:", when="@1.0.1:")

