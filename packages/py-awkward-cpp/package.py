# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAwkwardCpp(PythonPackage):
    # BEGIN VERSIONS
    version("30", sha256="5be94ca7351d8e421cb9478a9b71016fa7673621fa122d477d0b07bb68aa7d4c", url="https://pypi.org/packages/38/de/a8df67cfe8fac16282854c96915906b6d29d6ce2182325cf67a17297e5d8/awkward-cpp-30.tar.gz")
    version("29", sha256="af4b7891b78b903171bce341e88d2add84059fa167f08e8a993005999d1b9d1b", url="https://pypi.org/packages/92/66/6a568a041c59c4c84502c27e3a78c83110fe1314761746a733e7be347ee4/awkward-cpp-29.tar.gz")
    version("28", sha256="304ebbf900c577368fd3c491a4ddfe6a5790bdec76a2b06bdcc4728176264592", url="https://pypi.org/packages/0e/fb/8e7db64da16a40558e3103a6d9bda0e84953a6f60041f28831b7d75cf224/awkward-cpp-28.tar.gz")
    version("27", sha256="3c196518bfcce709766d63878041317a4914b62f8083e1a3e03b4fd6ea6f3c8d", url="https://pypi.org/packages/dc/4c/1da5e387a2ec963dfc1004af1a2e404488097f1cea3279a0d79fa11f9333/awkward-cpp-27.tar.gz")
    version("26", sha256="a37c08f89126b637d4733454a1bf3f28b18d9f7947d21dc6ba12037d883b1c66", url="https://pypi.org/packages/14/b3/08bea6c701ba178d012ccb5ec7f05c34e1be466c8f57fbf6085c7f347752/awkward-cpp-26.tar.gz")
    version("25", sha256="161aba5d4b79098cff97e2dff567029edf6bb376f2310210b3b8457b1af6b633", url="https://pypi.org/packages/cc/11/a15183b532795a37a08a0930fdd7587598393e50760e3c419fe0dfa54dea/awkward-cpp-25.tar.gz")
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
        depends_on("py-importlib-resources", when="@23: ^python@:3.8")
        depends_on("py-numpy@1.18.0:", when="@20:30")
        depends_on("py-numpy@1.17.0:", when="@12:19")
        depends_on("py-numpy@1.14.5:", when="@3:11")
        depends_on("py-numpy@1.13.1:", when="@1:2")
    # END DEPENDENCIES

