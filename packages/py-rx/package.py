##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRx(PythonPackage):
    version("3.2.0", sha256="922c5f4edb3aa1beaa47bf61d65d5380011ff6adcd527f26377d05cb73ed8ec8", url="https://pypi.org/packages/e2/a9/efeaeca4928a9a56d04d609b5730994d610c82cf4d9dd7aa173e6ef4233e/Rx-3.2.0-py3-none-any.whl")
    version("3.1.1", sha256="0e0f2715a3452e95dcb5d6ea28ffe5742e832592bbcc67a48f394ef8ba871e6f", url="https://pypi.org/packages/90/6c/5f1839d9ae2a8c85d119c51acaff1f1382f68691cb0f1cb3d0c9fdd32a93/Rx-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="aaf409848e24dd514926eb8467e2764762bfd258325717fca4628d32d8721252", url="https://pypi.org/packages/28/0e/50160479e1afba49e2c860f8fbd022f115acd2c64da9b6460c949adb0b01/Rx-3.1.0.tar.gz")
    version("3.0.1", sha256="00c4ab3ecd1ab9a55f310d05e20ae7f93d3cdd1150de5c56347e67a1ecd73963", url="https://pypi.org/packages/5b/ad/d93165ba4d6e02f6f6c7e84262444b62b646d5dd7d3a27f16530a2b1a8e5/Rx-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="7ad01944a6b86ed2ef9f38d785c61d5074c40bbb0d60c72c55aaf6da13af1475", url="https://pypi.org/packages/e3/54/fbaa34bd80d3da115f70b399761c60a91bdbad7a329541558e5b1594f636/Rx-3.0.0-py3-none-any.whl")
    version("3.0.0-beta5", sha256="4f37952a4095658e23a8055428e7f7ac335a21dd1680825f9f761641564624fd", url="https://pypi.org/packages/b7/32/150a0e791d28eacadfdf902b8370f6aa3900be6a53eef3109e7dbf81ac08/Rx-3.0.0b5-py3-none-any.whl")
    version("3.0.0-beta4", sha256="30aacb634ee3ec16473cd38ff0725c28b5ee6fb61e39a24c1cccef5b4d7c4077", url="https://pypi.org/packages/0b/f2/15d136bfe8314ce9c6829a6658f82a0c1a1661824ca2d8d060a695a4aa61/Rx-3.0.0b4-py3-none-any.whl")
    version("1.6.3", sha256="ca71b65d0fc0603a3b5cfaa9e33f5ba81e4aae10a58491133595088d7734b2da", url="https://pypi.org/packages/3c/51/d37235bad8df7536cc950e0d0a26e94131a6a3f7d5e1bed5f37f0846f2ef/Rx-1.6.3.tar.gz")
    version("1.6.1", sha256="7357592bc7e881a95e0c2013b73326f704953301ab551fbc8133a6fadab84105", url="https://pypi.org/packages/33/0f/5ef4ac78e2a538cc1b054eb86285fe0bf7a5dbaeaac2c584757c300515e2/Rx-1.6.1-py2.py3-none-any.whl")
    version("1.6.0", sha256="ad793d79843feba2ea25c0c01be245f3163d5d469418279d4019737b93d88c78", url="https://pypi.org/packages/90/19/08cd1ee825d11f65ee999de30911c1947ffe4196b920061065194a2225c7/Rx-1.6.0-py2.py3-none-any.whl")
    version("1.5.9", sha256="f09c9f6cd54f368174738408af899756a777655baaac605353ad64c2766d3e70", url="https://pypi.org/packages/db/43/1a96e3bb1ca0f7454d1f4843f26c6ff8d0eee71aaf6aabc687e82980d68f/Rx-1.5.9-py2.py3-none-any.whl")
    version("1.5.8", sha256="4f7571878450878179d095c5fb048318ab47911cb95353d6fd29c016ee3433d6", url="https://pypi.org/packages/32/3c/64d95b4aaece3c1db4e9015620021f6464b4d4db6bdd890fecdf850aebc8/Rx-1.5.8-py2.py3-none-any.whl")
    version("1.5.7", sha256="a1b73a3fae48133d7603a472ae0c1cbd54920a629507352e040035d5a734526f", url="https://pypi.org/packages/65/b2/0a7436291662932d75aec4818a0443a851db6e648e7eab7a88306c93ef70/Rx-1.5.7-py2.py3-none-any.whl")
    version("1.5.6", sha256="e8dd8140492dae752891e566c125b6f8e41d14d04a54793cb7c1ee1ffaeb74ca", url="https://pypi.org/packages/aa/01/44dbc5df06e1771dd2956731f852efbea0a2010679c4776e028cfb0f1e7f/Rx-1.5.6-py2.py3-none-any.whl")
    version("1.5.5", sha256="ae34ffb0a3df2d596e651349d817b10ee978ff5ff62975467317483c849be33f", url="https://pypi.org/packages/ea/45/f9d5f695bc2cb02f429909049c080f04ca2bc54edbe0b35d4b471c5fe582/Rx-1.5.5-py2.py3-none-any.whl")
    version("1.5.4", sha256="fb0cbb21b67eedbd0428df504dc8fe501b2bbac35a5243a0c3723bba13340315", url="https://pypi.org/packages/cd/ef/bcc494857c17dcb02b2d7a4a5b87e54db48c71bc40c2f7fedcd15e7633b1/Rx-1.5.4-py2.py3-none-any.whl")
    version("1.5.3", sha256="ef1889716eeec6daec581c6ad4a2b11aa1e5af33fac1846fd982603102d9bb03", url="https://pypi.org/packages/ce/ed/1938211aec2fe7fdd48ee3ab8d6bd00a2940c72888ac83eb13be08cfbbe9/Rx-1.5.3-py2.py3-none-any.whl")


