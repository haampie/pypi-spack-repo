##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLibcst(PythonPackage):
    version("1.2.0", sha256="71dd69fff76e7edaf8fae0f63ffcdbf5016e8cd83165b1d0688d6856aa48186a", url="https://pypi.org/packages/48/af/b243be2e6aaddd2b9e8f78817fc8f2ef5874753b01c2e07e75c109b102e8/libcst-1.2.0.tar.gz")
    version("1.1.0", sha256="0acbacb9a170455701845b7e940e2d7b9519db35a86768d86330a0b0deae1086", url="https://pypi.org/packages/81/ef/610498b5e982d9dd64f2af8422ece1be44a946a8dbda15d08087e0e1ff08/libcst-1.1.0.tar.gz")
    version("1.0.1", sha256="37187337f979ba426d8bfefc08008c3c1b09b9e9f9387050804ed2da88107570", url="https://pypi.org/packages/f4/b2/dd6fcf70dc59281e6de7c4b2f6150d07c26db127262dd5cba16fde1464ed/libcst-1.0.1.tar.gz")
    version("1.0.0", sha256="aaf3471c11a7dfc76c46d0b80e64bde5d066d88393fe14b79bcaeb6753744bae", url="https://pypi.org/packages/3f/bd/abf98f4a8fb2ae7e4857057c2a07165ed91f2543697af9d5cee9e7c6b57d/libcst-1.0.0.tar.gz")
    version("0.4.10", sha256="b98a829d96e8b209fb761b00cd1bacc27c70eae77d00e57976e5ae2c718c3f81", url="https://pypi.org/packages/a4/1a/f5bae3c178d44f9cad1e6ab4ed9b240b080e323a87b6b3e0ef7a7429aab6/libcst-0.4.10.tar.gz")
    version("0.4.9", sha256="01786c403348f76f274dbaf3888ae237ffb73e6ed6973e65eba5c1fc389861dd", url="https://pypi.org/packages/fa/4d/366f6fede5c5121fdda08db85a79f8b602a24378394cd9f87c917232d578/libcst-0.4.9.tar.gz")
    version("0.4.8", sha256="9c60bc726f6e6f9f05addeaf1a4f4cf27c2efc02bb2b4b0338b09f9dab8a8d65", url="https://pypi.org/packages/09/e8/3e6cc21f4fe3651a051f387ae7696366c4705ef3399ba6ac78132298fedb/libcst-0.4.8.tar.gz")
    version("0.4.7", sha256="95c52c2130531f6e726a3b077442cfd486975435fecf3db8224d43fba7b85099", url="https://pypi.org/packages/90/6b/ef2d7c86a61c6b6ae4eb48b832ba96897d4ba9743e9ece40f66625b11d60/libcst-0.4.7.tar.gz")
    version("0.4.6", sha256="80f6982db27907f07d47575c50fc878923646437160fb2680c685b8565590446", url="https://pypi.org/packages/3c/30/1a5d11ba4366218e3b1d2d84789643ec063f1c64c50641181d2881bf29d1/libcst-0.4.6.tar.gz")
    version("0.4.5", sha256="a17442b62a22bef6ce0734ff33801378575ab8a9f9a33dbafe236270cdbcdb3c", url="https://pypi.org/packages/12/87/453d2d6f24050d3734be02b4bec1e18e9d059ffdb7c5ff89096d8b26781c/libcst-0.4.5.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.2:")
        depends_on("py-pyyaml@5.2:", when="@0.3.1:0.3,1.1:")
        depends_on("py-typing-extensions@3.7.4.2:", when="@0.3.7:0.3,1.1:")
        depends_on("py-typing-inspect@0.4:", when="@0.3.1:0.3,1.1:")

