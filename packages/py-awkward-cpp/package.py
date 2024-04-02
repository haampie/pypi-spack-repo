# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAwkwardCpp(PythonPackage):
    # BEGIN VERSIONS
    version("12", sha256="429f7fcc37a671afa67fe9680f2edc3a123d1c74d399e5889c654f9529f9f8f2", url="https://pypi.org/packages/3b/2c/bbda35611aa640735de0ae056ad083bc70f82259eb7113a35f5668af05f9/awkward-cpp-12.tar.gz")
    version("11", sha256="02d719a4da7487564b29b8e8b78925a32ac818b6f5572c2f55912b4e0e59c7a4", url="https://pypi.org/packages/19/47/fbcb248e16b711018b8b49e2b0f12d088511227f4aa291b07812b1a87682/awkward-cpp-11.tar.gz")
    version("10", sha256="d1c856cb6ef5cf3d4f67506a7efc59239f595635865cc9f4ab18440b8bfb11c6", url="https://pypi.org/packages/2c/76/943901d54c6dc417674ce49e2a20d606361e1d8cc719651f429b4951bf0f/awkward-cpp-10.tar.gz")
    version("9", sha256="db1c91c21f88b89a39b46176edc67a08b37f7283c16a2ed5159e3c874613c61a", url="https://pypi.org/packages/5c/ed/9ea65e3121ca03b329734a45c17b4ba0cda78345f533ba43a30dc9fd4dd8/awkward-cpp-9.tar.gz")
    version("8", sha256="a51b554490b3197fc5433822becb2e8208bf78fca82ffa314d839b72b3cc4169", url="https://pypi.org/packages/aa/f5/64adc43fa8ade78ad35bf90276c8741d996c40c25626e9900d611f752446/awkward-cpp-8.tar.gz")
    version("7", sha256="dde733575b2a5ae5b946fe8667b4ae842d937d3b36ebb383d53dc53ea86ea65d", url="https://pypi.org/packages/8a/7e/2538c66fcf43ca00d19eea80e02afb98bc1acec6da56dbb2a0748e1549b4/awkward-cpp-7.tar.gz")
    version("6", sha256="58e32afa8aa44c365e764f4b5d07637c79a79be2da7cfbaa3469d8bd26b0bfa2", url="https://pypi.org/packages/f4/3e/204b96439344b3e715a0d9a3ea0d0ff3590951d053220f58489da795236b/awkward-cpp-6.tar.gz")
    version("5", sha256="e5d6a90d98a14dab36598015e69243b9f83b8851556104cbe778ca9c79923656", url="https://pypi.org/packages/0b/56/0d5d5b9574221c91aa846072bbc0823e2da3fe8e1deddd6edcd796b26be1/awkward-cpp-5.tar.gz")
    version("4", sha256="fbc4b5e552873e00ffb6286941efc7b629e4fbc4752e28afb9b54854128937f7", url="https://pypi.org/packages/30/f7/829945455a818abb8eef82d9a9a8db5ec71cd1dc726a2d08bbdb0c5a3da9/awkward-cpp-4.tar.gz")
    version("3", sha256="6070557762bd95d3642ad9c585609db51f899a1e79ce4f41568835efd7d6e066", url="https://pypi.org/packages/c4/17/f0ef5a90be73db62e81e04bf798535f51b17a7f236d3e43936f1dd4cb045/awkward-cpp-3.tar.gz")
    version("2", sha256="5e63f43e3135f76db81e0924a74ecf4870f585c11a9f432568b377c04028868c", url="https://pypi.org/packages/d0/e2/b0df75c750fc6bf98eda8974033bead2e7893bc640996af33c18a791c718/awkward-cpp-2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1:19")
        depends_on("py-numpy@1.17.0:", when="@12:19")
        depends_on("py-numpy@1.14.5:", when="@3:11")
        depends_on("py-numpy@1.13.1:", when="@1:2")
    # END DEPENDENCIES

