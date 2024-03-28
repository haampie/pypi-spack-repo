# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPysam(PythonPackage):
    # BEGIN VERSIONS
    version("0.22.0", sha256="ab7a46973cf0ab8c6ac327f4c3fb67698d7ccbeef8631a716898c6ba01ef3e45", url="https://pypi.org/packages/35/22/3d01778c13f1103401313f1232c1c0596d97aaee21c1d60564640f3049bd/pysam-0.22.0.tar.gz")
    version("0.21.0", sha256="5c9645ddd87668e36ff0a1966391e26f9c403bf85b1bc06c53fe2fcd592da2ce", url="https://pypi.org/packages/16/1c/a4999d93d6fd7791349f0822e1674b39971fe30d3b99638209ae6de3dfc7/pysam-0.21.0.tar.gz")
    version("0.20.0", sha256="7cc250148ba0ffc9bdc38db6988b91e13b75db0d11c18cf1336467d1c97dd312", url="https://pypi.org/packages/e3/ad/b300abaf0de2834104b671db5aebe71616d7a36fa09a2b8a03068eb7e932/pysam-0.20.0.tar.gz")
    version("0.19.1", sha256="dee403cbdf232170c1e11cc24c76e7dd748fc672ad38eb0414f3b9d569b1448f", url="https://pypi.org/packages/a0/10/f6d705984838f8620ff597dd99d3904aea7727b4824bee22de8f44b4ebd4/pysam-0.19.1.tar.gz")
    version("0.19.0", sha256="dcc052566f9509fd93b2a2664f094a13f016fd60cdd189e05fb4eafa0c89505b", url="https://pypi.org/packages/ee/95/aef9a843807c00bb6b4e6c0cad0e69aa161ecc0591f3ece985fd24298f21/pysam-0.19.0.tar.gz")
    version("0.18.0", sha256="1d6d49a0b3c626fae410a93d4c80583a8b5ddaacc9b46a080b250dbcebd30a59", url="https://pypi.org/packages/15/79/00249a37089a6aecb70a4080f8af8d88e7005e2019c71e505c3ad3a0a018/pysam-0.18.0.tar.gz")
    version("0.17.0", sha256="5d140da81ca42f474006f5cc0fd66647f1b08d559af7026bbe9f01fab029bffd", url="https://pypi.org/packages/bf/a6/b1802ac26bb501ce8dada6f41dd83cdf591ecc834f2c208b07c6d97eba84/pysam-0.17.0.tar.gz")
    version("0.16.0.1", sha256="d428a9768691d5ea3c28cc52a949c920ae691aa4c110a8b7328dc4d165ef1ad6", url="https://pypi.org/packages/99/5a/fc440eb5fffb5346e61a38b49991aa552e4b8b31e8493a101d2833ed1e19/pysam-0.16.0.1.tar.gz")
    version("0.16.0", sha256="07c9d3a772f90e9907a68bc3f495e2c608018a92888b9cf9f1197cb3a35aa9c3", url="https://pypi.org/packages/18/74/69018650a6ec9dae2eb2f710e158fa395134ce579c605f152e41890e7f3c/pysam-0.16.0.tar.gz")
    version("0.15.4", sha256="a535e15cbd6e27f4ab74cabca30ca1df7eea283cb91d3b536d47fe113fee066f", url="https://pypi.org/packages/25/7e/098753acbdac54ace0c6dc1f8a74b54c8028ab73fb027f6a4215487d1fea/pysam-0.15.4.tar.gz")
    version("0.15.3", sha256="a98dd0a164aa664b1ab30a36f653752f00e93c13deeb66868597f4b2a30f7265", url="https://pypi.org/packages/15/e7/2dab8bb0ac739555e69586f1492f0ff6bc4a1f8312992a83001d3deb77ac/pysam-0.15.3.tar.gz")
    version("0.15.2", sha256="d049efd91ed5b1af515aa30280bc9cb46a92ddd15d546c9b21ee68a6ed4055d9", url="https://pypi.org/packages/15/f6/ce0611aaa1865a616f7dc164fbf046eaf38f2b17c6d404403c56250beb93/pysam-0.15.2.tar.gz")
    version("0.15.1", sha256="658421124c2f3de1b7445e03ca8413df0077f67ea9980abdaab0d1b5f7a8936f", url="https://pypi.org/packages/73/59/c319f1bde3019bbce4583cecb12b9e3e52ffcfbe2c96d8b1fb131c0d4fb7/pysam-0.15.1.tar.gz")
    version("0.14.1", sha256="2e86f5228429d08975c8adb9030296699012a8deba8ba26cbfc09b374f792c97", url="https://pypi.org/packages/fc/9b/4bb8d016406dcff47e2866e14d3dcb10741ec3920649e8c521996830944f/pysam-0.14.1.tar.gz")
    version("0.7.7", sha256="c9f3018482eec99ee199dda3fdef2aa7424dde6574672a4c0d209a10985755cc", url="https://pypi.org/packages/46/b5/877f40fbb84f588b69b4afcb1409b8bdeed7ef980113d3e8ef69bab26e09/pysam-0.7.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

