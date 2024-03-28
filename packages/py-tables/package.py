# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTables(PythonPackage):
    # BEGIN VERSIONS
    version("3.9.0", sha256="27c9ca14c359d875caf945a6a527c12690e017650402dd17d8eb8b6caf6687d5", url="https://pypi.org/packages/a7/e4/0e26466476bbc5e23ff53d5c96270608f0f677b957fadcb9c9180c938b5e/tables-3.9.0.tar.gz")
    version("3.8.0", sha256="34f3fa2366ce20b18f1df573a77c1d27306ce1f2a41d9f9eff621b5192ea8788", url="https://pypi.org/packages/bc/42/07b37c0c64a13f005bfe95c8eec5f454fc8dd2caf85fa28add5b2a35b7ab/tables-3.8.0.tar.gz")
    version("3.7.0", sha256="e92a887ad6f2a983e564a69902de4a7645c30069fc01abd353ec5da255c5e1fe", url="https://pypi.org/packages/d2/55/fb95c1c82750f05eb0fd082cc95c25f56cc32a4fd3518794cce1914af1ff/tables-3.7.0.tar.gz")
    version("3.6.1", sha256="49a972b8a7c27a8a173aeb05f67acb45fe608b64cd8e9fa667c0962a60b71b49", url="https://pypi.org/packages/2b/32/847ee3f521aae6a0be380d923a736162d698586f444df1ac24b98c65025c/tables-3.6.1.tar.gz")
    version("3.5.2", sha256="b220e32262bab320aa41d33125a7851ff898be97c0de30b456247508e2cc33c2", url="https://pypi.org/packages/73/51/6dabb2b94826e5db3aa2542b80f1382780b96a0cd13e0cfb637b36ede5c5/tables-3.5.2.tar.gz")
    version("3.4.4", sha256="bdc5c073712af2a43babd139c4855fc99496bb2c3f3f5d1b4770a985e6f9ce29", url="https://pypi.org/packages/4d/53/8f34ce887c2a2ad80518980419a5f6f41defc85a287a355987e559ce9385/tables-3.4.4.tar.gz")
    version("3.3.0", sha256="8383ccf02e041a5d55494a09fc5514140b4653055a2732c981b5fd0f7408822c", url="https://pypi.org/packages/97/eb/ea2102f5a210a62f9f7387cf9912cb841f4a9089dbb232e642daa2626769/tables-3.3.0.tar.gz")
    version("3.2.2", sha256="3564b351a71ec1737b503b001eb7ceae1f65d5d6e3ffe1ea75aafba10f37fa84", url="https://pypi.org/packages/af/38/85a4581084ad2aaed4318b7f3a46c5bed3ecb32bae0929add5d7c752d8fc/tables-3.2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("bzip2", default=False)
    variant("lzo", default=False)
    variant("zlib", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.9.1:")
        depends_on("py-blosc2@2.2.8:", when="@3.9:3.9.1")
        depends_on("py-numexpr@2.6.2:", when="@3.6,3.9:")
        depends_on("py-numexpr@2.5.2:", when="@3.4.4:3.4")
        depends_on("py-numpy@1.19.0:", when="@3.9:")
        depends_on("py-numpy@1.9.3:", when="@3.6")
        depends_on("py-numpy@1.8:", when="@3.4.4:3.4")
        depends_on("py-packaging", when="@3.9:")
        depends_on("py-py-cpuinfo", when="@3.9:")
        depends_on("py-six@1.9:", when="@3.4.4:3.4")
    # END DEPENDENCIES

