# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnsimarkup(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.0", sha256="51ab9f3157125c53e93d8fd2e92df37dfa1757c9f2371ed48554e111c7d4401a", url="https://pypi.org/packages/60/99/878823a360a0bd9ae034d39fe37f8fdd976de8da642c2ec608f093efc273/ansimarkup-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="7edbfc6fc9cbf67589bc510ff5502aa34a2de8db9ceed61b186864af6426a70e", url="https://pypi.org/packages/28/a5/746c844af06b87993edea2a215e6a3ce8da75a28fbb4998ab39ac3902ce6/ansimarkup-2.0.0-py3-none-any.whl")
    version("1.5.0", sha256="3146ca74af5f69e48a9c3d41b31085c0d6378f803edeb364856d37c11a684acf", url="https://pypi.org/packages/22/09/3ad81e40d752ef51a9a8c320c9385de0d98a4dad68c0e4f793befc610f56/ansimarkup-1.5.0-py2.py3-none-any.whl")
    version("1.4.1", sha256="2ea88deb1900e9446922a17cf3583fd04351f9a7f1d056dba783cb5c824bfcd5", url="https://pypi.org/packages/c0/b3/9ac6cc9cd8addb3464987bec4fa95045983fcfb720bb175b268b373ee33f/ansimarkup-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="06365e3ef89a12734fc408b2449cb4642d5fe2e603e95e7296eff9e98a0fe0b4", url="https://pypi.org/packages/8f/3b/be9c9da51fc950c58f64221676f5d2972a4003dc4ac05642cb6d279a281a/ansimarkup-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="1ed2f2551b63eb7847a3635d421a9f77e269dffa1eaf21529f689ea1ec162e97", url="https://pypi.org/packages/90/92/0a6a328ee09bd3cc57705769d0fcb2c9afb4c84ef9df3b7ee2d700793ad0/ansimarkup-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="6ee4cf2b35a2db6a408f95b5f778ffea314749dc3387eccc5285c967e6e70a9a", url="https://pypi.org/packages/1b/72/513e46fe5e6c4350aba0b8efb69568e8b3770ad85ba4f7b39404d2626833/ansimarkup-1.2.0-py2.py3-none-any.whl")
    version("1.1.0", sha256="e3d9216d01aea8a9a6a4d4f1f943c732705f0a01e13ab72bd66aac4c499a51da", url="https://pypi.org/packages/1a/4d/2faa9cd5f6063904b6d3fa49abecf2d9f78843c3c6091fcf6d222b77473e/ansimarkup-1.1.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="3b24274ad3d7009a18fe78ff13b6d3122edd02e64fb86a167d67f150862d5779", url="https://pypi.org/packages/1b/51/fcb5891ddbd77d90450202d1ec9636b76ae9b6c28dd95db9337d51357280/ansimarkup-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama", when="@1.4.1:")
    # END DEPENDENCIES

