##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySimplejson(PythonPackage):
    version("3.19.2", sha256="9eb442a2442ce417801c912df68e1f6ccfcd41577ae7274953ab3ad24ef7d82c", url="https://pypi.org/packages/79/79/3ccb95bb4154952532f280f7a41979fbfb0fbbaee4d609810ecb01650afa/simplejson-3.19.2.tar.gz")
    version("3.19.1", sha256="6277f60848a7d8319d27d2be767a7546bc965535b28070e310b3a9af90604a4c", url="https://pypi.org/packages/c0/5c/61e2afbe62bbe2e328d4d1f426f6e39052b73eddca23b5ba524026561250/simplejson-3.19.1.tar.gz")
    version("3.18.4", sha256="6197cfebe659ac802a686b5408494115a7062b45cdf37679c4d6a9d4f39649b7", url="https://pypi.org/packages/00/cd/62392cee6e24da6768a578651907c8e08ae316fc931d09ba98e5114d561d/simplejson-3.18.4.tar.gz")
    version("3.18.3", sha256="ebb53837c5ffcb6100646018565d3f1afed6f4b185b14b2c9cbccf874fe40157", url="https://pypi.org/packages/b1/86/a67f6f595c5da14fa80bb4a8f7084c391ac1bfd3208ea4906307afc2b181/simplejson-3.18.3.tar.gz")
    version("3.18.2", sha256="663e9109d0a2f883472080b776ec4a4a66f8931efa4cfe4714021dbc8ef7d0d6", url="https://pypi.org/packages/0e/4d/bc45300f0c6ae36462166faec34b62827b8e0a9f71c987ee36e7e5435294/simplejson-3.18.2.tar.gz")
    version("3.18.1", sha256="746086e3ef6d74b53599df31b491d88a355abf2e31c837137dd90f8c4561cafa", url="https://pypi.org/packages/0f/a0/79d2bec499cb53678bc20d41f9706ca02777f0876efa9b29a69fb3d55dfd/simplejson-3.18.1.tar.gz")
    version("3.18.0", sha256="58a429d2c2fa80834115b923ff689622de8f214cf0dc4afa9f59e824b444ab31", url="https://pypi.org/packages/17/3d/b8bfe1f40558f6a16f70c349adf97480dc71a7d11b2b1a5dc0824a87faa0/simplejson-3.18.0.tar.gz")
    version("3.17.6", sha256="cf98038d2abf63a1ada5730e91e84c642ba6c225b0198c3684151b1f80c5f8a6", url="https://pypi.org/packages/7a/47/c7cc3d4ed15f09917838a2fb4e1759eafb6d2f37ebf7043af984d8b36cf7/simplejson-3.17.6.tar.gz")
    version("3.17.5", sha256="91cfb43fb91ff6d1e4258be04eee84b51a4ef40a28d899679b9ea2556322fb50", url="https://pypi.org/packages/01/52/41c71718f941c9a5abebfaa24e3c14e3c0229327b7ebd21348989845ed8f/simplejson-3.17.5.tar.gz")
    version("3.17.4", sha256="2af85e028714c4b6cb2eb6fc03aa91f39ffd654f2eb2f6f8f860e14aeefa6be1", url="https://pypi.org/packages/0b/d1/d1cbd62baf1f1a635a4cd45c8349d235f1d87129e5f9bd9957a2308c424d/simplejson-3.17.4.tar.gz")
    version("3.17.2", sha256="75ecc79f26d99222a084fbdd1ce5aad3ac3a8bd535cd9059528452da38b68841", url="https://pypi.org/packages/49/45/a16db4f0fa383aaf0676fb7e3c660304fe390415c243f41a77c7f917d59b/simplejson-3.17.2.tar.gz")
    version("3.16.0", sha256="b1f329139ba647a9548aa05fb95d046b4a677643070dc2afc05fa2e975d09ca5", url="https://pypi.org/packages/e3/24/c35fb1c1c315fc0fffe61ea00d3f88e85469004713dab488dee4f35b0aff/simplejson-3.16.0.tar.gz")
    version("3.10.0", sha256="953be622e88323c6f43fad61ffd05bebe73b9fd9863a46d68b052d2aa7d71ce2", url="https://pypi.org/packages/40/ad/52c1f3a562df3b210e8f165e1aa243a178c454ead65476a39fa3ce1847b6/simplejson-3.10.0.tar.gz")
    version("3.9.0", sha256="e9abeee37424f4bfcd27d001d943582fb8c729ffc0b74b72bd0e9b626ed0d1b6", url="https://pypi.org/packages/81/b6/9a4d0107b1a8929c77f88bb816c64da25aacba6ef1ac080d39e46d8f1307/simplejson-3.9.0.tar.gz")
    version("3.8.2", sha256="d58439c548433adcda98e695be53e526ba940a4b9c44fb9a05d92cd495cdd47f", url="https://pypi.org/packages/f0/07/26b519e6ebb03c2a74989f7571e6ae6b82e9d7d81b8de6fcdbfc643c7b58/simplejson-3.8.2.tar.gz")
    version("3.8.1", sha256="428ac8f3219c78fb04ce05895d5dff9bd813c05a9a7922c53dc879cd32a12493", url="https://pypi.org/packages/70/b0/c8169f6c2b7927614bea25636485992248ae0b1d7bc83858a9185461f57b/simplejson-3.8.1.tar.gz")
    version("3.8.0", sha256="217e4797da3a9a4a9fbe6722e0db98070b8443a88212d7acdbd241a7668141d9", url="https://pypi.org/packages/36/c9/746cec37ec357c9882011d1d4ed06e6fe27bea48c4272ebbbc7512bcb7da/simplejson-3.8.0.tar.gz")
    version("3.3.0", sha256="7a8a6bd82e111976aeb06138316ab10847adf612925072eaff8512228bcf9a1f", url="https://pypi.org/packages/fc/7c/f9cec79ab9c8fc190821c69fdbcb15ecba438ff35f13b3f8d9675efcfd0d/simplejson-3.3.0.tar.gz")


