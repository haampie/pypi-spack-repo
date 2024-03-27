##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWget(PythonPackage):
    version("3.2", sha256="35e630eca2aa50ce998b9b1a127bb26b30dfee573702782aa982f875e3f16061", url="https://pypi.org/packages/47/6a/62e288da7bcda82b935ff0c6cfe542970f04e29c756b0e147251b2fb251f/wget-3.2.zip")
    version("3.1", sha256="edfd5a7ff662930e0a588f4b8ea1cc0e6f55228f64d0f65e23cb49e906ca54f0", url="https://pypi.org/packages/b2/44/0dadf6bd187f202ba0234e193456a29a6d2d96d52d3447e84e5e87ff031b/wget-3.1.zip")
    version("3.0", sha256="035e423361f24691920e6f36fa9d226bebb1e830848d059147af84b75c65f750", url="https://pypi.org/packages/0c/a9/144bb26c469ffeb2ff1e404546b18031ed612a0827e0a2880ff57e2816dd/wget-3.0.zip")
    version("2.2", sha256="8b903b559b516f2732a2b86abc4027213f4293676f17a78ac13f29a93e30bb44", url="https://pypi.org/packages/8f/b9/8c0e4a960b03af703618ab0d1dc01f45a6d1211b33a40b5707fee27415e8/wget-2.2.tar.gz")
    version("2.1", sha256="7b9b21345832dd30ad9ff5950c25b5c72e51edb0ccbf4a0087e73fbbebf7a195", url="https://pypi.org/packages/7f/66/6c9e4a9f6aa5e29bcbca8ea4f1699fdfadeb12be890c97d3f7692a8ad523/wget-2.1.zip")
    version("2.0", sha256="9a5f5ee72f2a7513886881b03acd0dddd138a64e5e80ee48b299d54e3ce1f257", url="https://pypi.org/packages/36/b9/bf6e205d6bfa5fe1a4f81bb17f60a7c2ff01cd9992f8c0168febf1396c77/wget-2.0.tar.gz")
    version("1.0", sha256="6805cc3c2ded5ddc71f606155a105812097e467939c78ae7afedf50ab661eec1", url="https://pypi.org/packages/fd/fb/5e8c6e160cbe52a548613f7a64feb68bdc30a188ae1e62065dd50f200719/wget-1.0.zip")
    version("0.9", sha256="ff9f286f31a9f002daf68fcd76d2f4593592f86ab964b72782ca6135f0c04f43", url="https://pypi.org/packages/92/48/ba1c6b17abb1fe45ec6e4ba8b74db6c75420c1bad979b46455c63595ba71/wget-0.9.zip")
    version("0.8", sha256="9e7657ae026ef590d2a6d8fdc835d36e612f62aae71572e12c73e12c3cc20f56", url="https://pypi.org/packages/76/a6/1166994cfee1ed683f42b01233a9f6f0f171739558ffa898f0c43cf0ff9c/wget-0.8.zip")
    version("0.7", sha256="aad51d9b7b8c1725b79d3c0ae87d81d2ae12342407ab5f3770e62234a15862ac", url="https://pypi.org/packages/a5/86/d6a280ccab404cc1981b73194403f35529e769cf4fced58a29e567f7b824/wget-0.7.zip")


